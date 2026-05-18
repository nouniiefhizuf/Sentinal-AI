<div align="center">

# 🛡️ Sentinal AI

### *AI-Powered Code Creation — Write Better Code, Faster.*

[![GitHub Stars](https://img.shields.io/github/stars/nouniiefhizuf/Sentinal-AI?style=for-the-badge&color=gold)](https://github.com/nouniiefhizuf/Sentinal-AI/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/nouniiefhizuf/Sentinal-AI?style=for-the-badge&color=blue)](https://github.com/nouniiefhizuf/Sentinal-AI/network)
[![License](https://img.shields.io/github/license/nouniiefhizuf/Sentinal-AI?style=for-the-badge&color=green)](LICENSE)
[![Issues](https://img.shields.io/github/issues/nouniiefhizuf/Sentinal-AI?style=for-the-badge&color=red)](https://github.com/nouniiefhizuf/Sentinal-AI/issues)
[![Last Commit](https://img.shields.io/github/last-commit/nouniiefhizuf/Sentinal-AI?style=for-the-badge&color=purple)](https://github.com/nouniiefhizuf/Sentinal-AI/commits/main)

</div>

---

# SentinelAI: AI Cybersecurity Command Center

SentinelAI is a modern Streamlit-based cybersecurity analytics platform for visualizing AI model performance, cybersecurity experiment results, detection telemetry, incident queues, and dataset insights.

The project transforms raw cybersecurity datasets and experiment outputs into a clean, interactive, SaaS-style dashboard with authentication, analytics, export tools, and a polished user interface.

---

## Overview

This project focuses on evaluating and presenting AI performance across cybersecurity tasks such as:

- Phishing detection
- Malware analysis
- Intrusion detection
- Vulnerability discovery
- Phishing generation
- Attack planning

It provides a professional dashboard interface for understanding how different AI models perform on defensive and offensive cybersecurity tasks.

---

## Key Features

### Secure Authentication

- User login system
- Account creation
- Password hashing
- Cookie-based sessions
- Local account storage using YAML
- Protected dashboard access

### Dashboard

- KPI cards for model performance
- Detection telemetry chart
- Daily detections and risk score visualization
- Activity feed
- Incident queue
- Model ranking
- Evidence tables

### Analytics

- Interactive experiment result tables
- CSV export functionality
- Published result figures
- Dataset and result exploration

### Modern UI/UX

- Streamlit frontend
- Custom CSS design system
- Dark SaaS-style interface
- Glassmorphism-inspired cards
- Responsive layouts
- Sidebar navigation
- Professional typography and spacing

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Frontend dashboard framework |
| Pandas | Data loading and analysis |
| NumPy | Numerical operations |
| Plotly | Interactive visualizations |
| Streamlit Authenticator | Login and account authentication |
| PyYAML | Local account configuration |
| Custom CSS | UI styling and layout polish |

---

## Project Structure

```text
SentinelAI/
│
├── app.py
├── requirements.txt
├── README.md
├── run_streamlit.ps1
│
├── src/
│   ├── components/
│   │   └── ui.py
│   │
│   ├── pages/
│   │   ├── home.py
│   │   ├── dashboard.py
│   │   ├── analytics.py
│   │   ├── settings.py
│   │   └── login.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   └── data_loader.py
│   │
│   ├── styles/
│   │   └── main.css
│   │
│   └── utils/
│       ├── formatting.py
│       └── state.py
│
├── datasets/
│   ├── phishing_dataset.csv
│   ├── malware_dataset.csv
│   └── nslkdd_dataset.csv
│
├── results/
│   ├── experiment_scores.csv
│   ├── master_results_summary.csv
│   └── generated figures/results
│
├── config/
│   └── auth.example.yaml
│
└── .streamlit/
    └── config.toml

DatasetsThe project uses three cybersecurity datasets:
Dataset	Description
phishing_dataset.csv	Phishing detection data
malware_dataset.csv	Malware analysis data
nslkdd_dataset.csv	Intrusion detection data
Together, the datasets are approximately 44 MB.
How Detection Telemetry WorksThe Detection Telemetry chart shows two daily values:
DetectionsThe number of suspicious cybersecurity events detected per day.
Examples:
phishing emails
malware-like files
suspicious logins
intrusion signals
abnormal network behavior
Risk ScoreA calculated score that represents how serious the overall security situation is.
The risk score can be based on:
number of detections
severity of alerts
confidence of the AI model
affected systems
repeated suspicious behavior
In the current version, this telemetry uses synthetic demo data to demonstrate the dashboard experience.
Installation1. Clone the Repositorybash



git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY

2. Create a Virtual Environmentbash



python -m venv myenv

3. Activate the EnvironmentOn Windows:
bash



myenv\Scripts\activate

On macOS/Linux:
bash



source myenv/bin/activate

4. Install Dependenciesbash



pip install -r requirements.txt

5. Run the Appbash



streamlit run app.py

Authentication SetupThis project uses streamlit-authenticator.
For GitHub, do not upload real user accounts. Instead, include:
Add to chat
config/auth.example.yaml

Example:
yaml



credentials:
  usernames: {}
cookie:
  expiry_days: 7
  key: change-this-cookie-key-before-deploying
  name: sentinelai_auth
preauthorized:
  emails: []

When running locally, the app can create and save accounts in:
Add to chat
config/auth.yaml

This file should not be committed to GitHub.
Security NotesDo not upload:
Add to chat
.env
env
myenv/
config/auth.yaml
.streamlit/secrets.toml
API keys
saved user accounts

Passwords are hashed before being saved, but account files should still remain private.
Main PagesHomeIntroduces the platform and shows high-level project metrics, dataset inventory, and feature cards.
DashboardDisplays model performance, security telemetry, activity feed, incident queue, and evidence tables.
AnalyticsAllows users to inspect experiment results, view generated figures, and export data.
SettingsProvides profile, theme, model, notification, and configuration controls.
LoginProvides secure access using account creation and username/password login.
AI Model EvaluationThe project compares AI models across defensive and offensive cybersecurity tasks.
Defensive tasks include:
phishing detection
malware analysis
intrusion detection
Offensive tasks include:
phishing generation
vulnerability discovery
attack planning
LLMs tend to perform better on offensive tasks because those tasks are more language-based and generative, while defensive tasks require more precise classification and detection accuracy.
Example Presentation SummarySentinelAI is an AI cybersecurity dashboard built with Streamlit. It visualizes cybersecurity datasets, AI model performance, detection telemetry, incident queues, and analytics. The app includes secure login, hashed account storage, interactive charts, exportable tables, and a modern SaaS-style interface.
Future ImprovementsPlanned improvements include:
Real-time security log integration
Database-backed user accounts
Role-based access control
Cloud authentication
Live model inference
Audit logs
Deployment with HTTPS
Admin user management
More advanced model comparison tools

</div>
