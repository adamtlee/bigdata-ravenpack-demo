import requests
import json
from dotenv import load_dotenv
import os
   
# Load environment variables from .env file
load_dotenv()
   
# Access the API key
my_api_key = os.getenv('BIGDATA_API_KEY')
endpoint = "https://agents.bigdata.com/v1/research-agent"

research_prompt = "You are a Senior Portfolio Manager analyzing companies for institutional investors. Write a concise financial analysis of NVIDIA (NVDA) in Markdown. Include: 1) Company overview, 2) Recent financial performance, 3) Key growth drivers, 4) Valuation vs peers, 5) Main risks, and 6) Your investment outlook. Use a professional, data-driven tone with first-person plural ('we believe'). Structure as: # NVIDIA Financial Analysis ## Overview ## Financials ## Outlook ## Risks and Conclusion."

payload = {
    "message": research_prompt,
    "research_effort": "standard"
}

headers = {
    "X-API-KEY": my_api_key,
    "Content-Type": "application/json",
}

# Stream and print research response in real-time
print("🔍 Starting research analysis...")

with requests.post(endpoint, headers=headers, json=payload, stream=True, timeout=60) as r:
    r.raise_for_status()
    for raw_line in r.iter_lines(decode_unicode=True):
        if not raw_line:
            continue
        if raw_line.startswith("data: "):
            data = raw_line[6:].strip()
            try:
                event = json.loads(data)
                message_type = event.get("message", {}).get("type")
                
                # Print ANSWER content as it comes
                if message_type == "ANSWER":
                    content = event.get("message", {}).get("content", "")
                    if content:
                        print(content, end="", flush=True)
                
                # Signal completion
                elif message_type == "COMPLETE":
                    print("\n🎯 Research complete!")
                    
            except json.JSONDecodeError:
                # ignore malformed/keep
                pass