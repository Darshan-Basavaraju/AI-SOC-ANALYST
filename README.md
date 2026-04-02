# AI SOC Analyst 🔍

An AI-powered SOC (Security Operations Center) analysis tool that processes log data and generates structured incident insights.

---

## 🚀 Features
- Log ingestion from file  
- AI-generated incident summaries  
- Severity classification (Low, Medium, High)  
- Confidence scoring  
- Key indicator extraction (IOCs)  
- Actionable remediation recommendations  
- Structured JSON output for automation  

---

## 🧠 Use Case
This tool simulates a SOC analyst by automatically analyzing logs and providing incident context, helping security teams triage alerts faster.

---

## 💻 Tech Stack
- Python  
- OpenAI API (gpt-4o-mini)  

---

## 📥 Example Input

```
Failed login from 192.168.1.10
Failed login from 185.23.44.12
Successful login from 192.168.1.15
```

---

## 📤 Example Output

```json
{
  "incident_summary": "Multiple failed login attempts detected from both internal and external IP addresses, followed by a successful login from an internal IP address. The failed attempts could potentially indicate a brute-force attack or unauthorized access attempts.",
  "severity": "Medium",
  "confidence": "Medium",
  "key_indicators": [
    "3 failed login attempts from two different IP addresses",
    "1 successful login from a different internal IP address"
  ],
  "recommended_actions": [
    "Monitor the account associated with the successful login for unusual activity.",
    "Perform a password policy review and consider implementing account lockout mechanisms to mitigate brute-force attempts.",
    "Investigate the source of the failed login attempts, particularly from the external IP address."
  ]
}
```

---

## ⚙️ How to Run

```bash
python analyzer.py logs.txt
```

---
