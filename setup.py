#!/usr/bin/env python
"""
Setup script for the AI Chatbot application
"""
import subprocess
import sys
import os
from pathlib import Path

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False

def check_api_key():
    """Check if Together API key is set"""
    api_key = os.getenv("TOGETHER_API_KEY")
    if not api_key:
        print("❌ TOGETHER_API_KEY environment variable not set!")
        print("\nPlease set your Together AI API key:")
        print("Windows PowerShell: $env:TOGETHER_API_KEY='your_api_key_here'")
        print("Windows CMD: set TOGETHER_API_KEY=your_api_key_here")
        print("\nOr create a .env file with: TOGETHER_API_KEY=your_api_key_here")
        return False
    else:
        print("✅ API key found!")
        return True

def run_app():
    """Run the Streamlit application"""
    print("Starting the chatbot application...")
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error running application: {e}")

def main():
    print("🤖 AI Chatbot Setup")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("app.py").exists():
        print("❌ app.py not found. Please run this script from the project directory.")
        return
    
    # Install requirements
    if not install_requirements():
        return
    
    # Check API key
    if not check_api_key():
        return
    
    print("\n🚀 Setup complete! Starting the application...")
    print("The app will open in your browser at http://localhost:8501")
    print("Press Ctrl+C to stop the application\n")
    
    # Run the app
    run_app()

if __name__ == "__main__":
    main()
