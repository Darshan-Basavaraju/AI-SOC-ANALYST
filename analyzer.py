import sys
from openai import OpenAI

client = OpenAI()

# Read input file
if len(sys.argv) > 1:
    with open(sys.argv[1], "r") as file:
        logs = file.read()
else:
    logs = "No logs provided"

prompt = f"""
You are a SOC analyst.

Analyze the logs and STRICTLY return output in JSON format with this structure:

{{
  "incident_summary": "...",
  "severity": "Low | Medium | High",
  "confidence": "Low | Medium | High",
  "key_indicators": [],
  "recommended_actions": []
}}

Logs:
{logs}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    response_format={"type": "json_object"} 
)

print("\n🔍 AI SOC Analysis:\n")
print(response.choices[0].message.content)