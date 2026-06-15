import os
import sys
from google import genai

def analyze_logs_with_ai(log_file_path):
    # 1. Initialize the client (automatically uses GEMINI_API_KEY from environment)
    try:
        client = genai.Client()
    except Exception as e:
        print("Error: Could not initialize AI client. Did you set GEMINI_API_KEY?")
        sys.exit(1)

    # 2. Read the log file
    if not os.path.exists(log_file_path):
        print(f"Error: Could not find {log_file_path}")
        return

    with open(log_file_path, "r") as file:
        raw_logs = file.read()

    print("🤖 AI SRE Assistant is analyzing the logs...\n")

    # 3. Create the prompt instruction
    prompt = f"""
    You are an Expert L3 Cloud DevOps Engineer. 
    Analyze the following raw server logs and provide a quick operational runbook.
    
    Raw Logs:
    {raw_logs}
    
    Format your response exactly like this:
    1. **Root Cause**: Briefly explain what crashed.
    2. **Immediate Fix**: Give me the exact Linux shell commands to fix this right now.
    3. **Prevention**: How do we stop this in the future?
    """

    # 4. Call the AI model
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        print("🚨 INCIDENT REPORT GENERATED 🚨")
        print("-" * 40)
        print(response.text)
        print("-" * 40)
    except Exception as e:
        print(f"Failed to reach AI API: {e}")

if __name__ == "__main__":
    analyze_logs_with_ai("production_error.log")
