# 🤖 AI-Driven SRE Operations Analyzer

An automated AIOps utility built with **Python** and the **Google GenAI SDK** designed to ingest raw Linux/Cloud middleware logs, perform instant Root Cause Analysis (RCA), and generate immediate remediation runbooks. 

## 🎯 The Business Problem
During critical production outages, Site Reliability Engineers (SREs) and Cloud Ops teams spend valuable time manually parsing thousands of lines of logs across Tomcat, Nginx, and system kernels. This manual triage increases Mean Time to Resolution (MTTR) and impacts SLA compliance.

## 💡 The Solution
This project acts as a proof-of-concept for **AIOps integration**. It programmatically feeds failing server logs into an LLM via an API, utilizing a highly tuned system prompt to force the AI to act as an L3 Cloud DevOps Engineer. 

**The script automatically outputs:**
1. A clear Root Cause Analysis (RCA).
2. The exact Linux/CLI commands required for immediate system restoration.
3. Long-term architectural prevention strategies.

## 🛠️ Technologies Used
* **Programming:** Python 3
* **AI/ML:** Google Generative AI SDK (`gemini-2.5-flash`)
* **Infrastructure Context:** Linux, Nginx, Apache Tomcat, Core Networking

## 🚀 How to Run Locally

1. **Clone the repository:**
   bash
   	git clone [https://github.com/YourUsername/ai-ops-analyzer.git](https://github.com/YourUsername/ai-ops-analyzer.git)
   	cd ai-ops-analyzer
2. Set up the virtual environment:
  '''bash
	python3 -m venv venv
	source venv/bin/activate
	pip install google-genai
3. Set up the virtual environment:
	Bash

	python3 -m venv venv
	source venv/bin/activate
	pip install google-genai

4. Export your AI API Key securely:
	Bash

	export GEMINI_API_KEY="your_actual_api_key_here"

5. Execute the SRE Log Analyzer:
	Bash

	python ai_analyzer.py
