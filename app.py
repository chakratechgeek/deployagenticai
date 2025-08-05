import streamlit as st
from together import Together
import os
from dotenv import load_dotenv

# Load environment variables from .env.example file
load_dotenv('.env.example')

# Configure Streamlit page
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Initialize Together client
@st.cache_resource
def init_together_client():
    api_key = os.getenv("TOGETHER_API_KEY")
    if not api_key:
        st.error("Please set your TOGETHER_API_KEY environment variable")
        st.stop()
    return Together(api_key=api_key)

# Function to check if query is AWS RDS related
def is_aws_rds_related(query):
    aws_rds_keywords = [
        'aws', 'rds', 'amazon rds', 'relational database service', 'database',
        'mysql', 'postgresql', 'oracle', 'sql server', 'mariadb', 'aurora',
        'db instance', 'database instance', 'vpc', 'subnet group', 'security group',
        'parameter group', 'option group', 'backup', 'snapshot', 'restore',
        'multi-az', 'read replica', 'endpoint', 'connection string',
        'deploy', 'deployment', 'setup', 'configure', 'installation',
        'cloudformation', 'terraform', 'cdk', 'cli', 'console'
    ]
    query_lower = query.lower()
    return any(keyword in query_lower for keyword in aws_rds_keywords)

# Function to get AI response
def get_ai_response(client, messages):
    try:
        # Check if the latest user message is AWS RDS related
        is_rds_query = False
        if messages and messages[-1]["role"] == "user":
            user_query = messages[-1]["content"]
            is_rds_query = is_aws_rds_related(user_query)
        
        # Add system message based on query type
        if is_rds_query:
            system_message = {
                "role": "system", 
                "content": "You are an AWS RDS deployment specialist. Provide detailed, helpful information about Amazon RDS setup, configuration, deployment, database management, and troubleshooting. Be thorough and technical when needed."
            }
        else:
            system_message = {
                "role": "system", 
                "content": "You are a helpful AI assistant. For general topics, provide brief, concise responses (1-2 sentences) unless explicitly asked for more details. Always keep responses short and to the point initially."
            }
        
        # Insert system message at the beginning
        chat_messages = [system_message] + messages
        
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
            messages=chat_messages,
            max_tokens=800 if is_rds_query else 300,  # More tokens for RDS questions
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Main app
def main():
    st.title("☁️ AWS RDS Assistant")
    st.markdown("Your specialized AI assistant for AWS RDS deployment and database management!")
    
    # Initialize the Together client
    client = init_together_client()
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
        # Accept user input
    if prompt := st.chat_input("Ask me about AWS RDS deployment or any general question!"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_ai_response(client, st.session_state.messages)
                st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Sidebar with options
    with st.sidebar:
        st.header("Chat Options")
        
        if st.button("Clear Chat History"):
            st.session_state.messages = []
            st.rerun()
        
        st.markdown("---")
        st.markdown("### About")
        st.markdown("This AI assistant specializes in AWS RDS deployment and database management. It also provides brief answers to general questions.")
        
        st.markdown("### Instructions")
        st.markdown("""
        1. **AWS RDS Questions**: Get detailed help with deployment, setup, configuration
        2. **General Questions**: Brief answers unless you ask for more details
        3. **Database Help**: MySQL, PostgreSQL, Aurora, and more
        4. **Ask for specifics**: "Tell me more" for detailed explanations
        """)

if __name__ == "__main__":
    main()
