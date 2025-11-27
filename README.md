*Project Overview*

This project is a Proof of Concept (POC) designed to automate the Investment Due Diligence (IDD) process using Python.
It bridges the gap between raw financial data and actionable risk analysis, simulating the logic used in RegTech solutions.

*Key Features*

Live Data Extraction: Connects to the Yahoo Finance API ("yfinance") to fetch real-time company news.

Risk Detection (NLP): Uses Natural Language Processing ("TextBlob") to analyze the sentiment of news headlines.

Automated Reporting: Generates a risk score and a compliance recommendation (High Risk / Low Risk) based on a defined threshold.

Resilience: Implements error handling for missing data or API connection issues.

*Tech Stack*

Language:Python 3.11
Libraries:
- "yfinance" (Financial Data) 
- "textblob" (Sentiment Analysis) 
- "datetime" (Reporting)

 *How to Run*

1. Clone the repository.
2. Install dependencies: 
```bash 
pip install yfinance textblob
