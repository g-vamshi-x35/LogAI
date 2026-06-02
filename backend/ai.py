import os
from groq import Groq
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Connect to Groq AI
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_log(log_text):
    # Send log to AI and get analysis
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """You are LogAI assistant. 
                Analyze log files and explain:
                1. What errors were found
                2. How serious they are
                3. How to fix them
                Keep explanation simple and clear."""
            },
            {
                "role": "user",
                "content": f"Analyze this log file:\n{log_text}"
            }
        ]
    )
    return response.choices[0].message.content

# Test
if __name__ == "__main__":
    test_log = """
    ERROR: Database connection failed
    ERROR: NullPointerException at line 42
    WARNING: Memory usage at 90%
    FATAL: Server crashed
    """
    result = analyze_log(test_log)
    print("AI Analysis:")
    print(result)
