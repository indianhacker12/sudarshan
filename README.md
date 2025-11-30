Below is the **fully polished, cleanly structured, GitHub-ready `README.md` file** for your **SUDARSHAN AI Security Scanner**.
Tum isko seedha **README.md me paste karo**, GitHub par **perfect render hoga**, koi alignment issue nahi aayega.

---

# **README.md (FINAL VERSION)**

**(Copy–Paste ready with perfect GitHub formatting)**

---

````md
<div align="center">
  <img src="logo.png" width="130">

# SUDARSHAN AI Security Scanner
Professional AI-Powered Web Application Security Testing Platform
</div>

---

## Table of Contents
- [What is SUDARSHAN?](#what-is-sudarshan)
- [Key Features](#key-features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Usage Examples](#usage-examples)
- [Scan Modes](#scan-modes)
- [Troubleshooting](#Troubleshooting)
- [Help & Support](#help--support)
- [Legal Notice](#legal-notice)
- [Author](#author)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

# What is SUDARSHAN?

SUDARSHAN (Advanced Security Testing & Risk Assessment with Vulnerability Analysis)  
Ek AI-powered professional-grade web application security scanner hai:

- Security Engineers  
- Pentesters  
- Developers  
- Organizations  
- Students  

ke liye specially designed.

### Highlights
- AI-Powered testing using LLaMA 3.2  
- Deep vulnerability scanning  
- OWASP Top 10 2021 coverage  
- Modern GUI + CLI  
- Detailed HTML/JSON Reports  

---

# Key Features

## AI-Powered Intelligence
- LLaMA 3.2 based intelligent analysis  
- Smart exploit payload generation  
- Multi-step chain attack detection  
- Business-impact based risk scoring  
- Executive summaries  

## OWASP Top 10 Coverage
| ID | Category | Tests |
|----|----------|--------|
| A01 | Broken Access Control | IDOR, Escalation, Traversal |
| A02 | Cryptographic Failures | SSL/TLS weakness |
| A03 | Injection | SQL, NoSQL, LDAP, XXE |
| A04 | Insecure Design | Logic flaws |
| A05 | Misconfiguration | Default creds, open configs |
| A06 | Vulnerable Components | Outdated versions |
| A07 | Auth Failures | Password/session issues |
| A08 | Data Integrity | Deserialization |
| A09 | Logging | Log tampering |
| A10 | SSRF | Server-side request forgery |

## GUI Features
- Burp Suite inspired interface  
- Live vulnerability feed  
- Color-coded severity  
- Real-time console  
- HTML/JSON report export  

---

# System Requirements

## Minimum:
- Python 3.8+  
- 4GB RAM  
- Windows / Linux / macOS  
- 5GB free storage  

## Recommended:
- 8GB RAM  
- 4+ core CPU  
- 10GB storage  

## Tested Platforms:
- Kali Linux  
- Parrot OS  
- Ubuntu  
- Debian  
- Windows 10/11  
- macOS  

---

# Installation

## Quick Install

```bash
git clone https://github.com/indianhacker12/sudarshan.git
cd sudarshan
````

### Windows

```bash
install.bat
```

### Linux/macOS

```bash
chmod +x install.sh
./install.sh
```

Installer performs:

* Python dependency installation
* Ollama setup
* LLaMA 3.2 (3B) model install
* Environment check

---

# How to Run

## GUI Mode (Recommended)

```bash
python sudarshan_gui.py
```

or

```bash
python sudarshan.py
```

## CLI Mode

### Basic Scan

```bash
python sudarshan.py -u https://example.com --basic
```

### Medium Scan

```bash
python sudarshan.py -u https://example.com
```

### Aggressive Scan

```bash
python sudarshan.py -u https://example.com --aggressive
```

### Advanced

```bash
python main.py -u https://example.com --owasp-all --chain-attacks
```

---

# Usage Examples

### Quick assessment

```bash
python sudarshan.py -u http://testphp.vulnweb.com/ --basic
```

### Standard assessment

```bash
python sudarshan.py -u http://demo.testfire.net/
```

### Full audit with verbose output

```bash
python sudarshan.py -u https://example.com --aggressive --verbose
```

### Custom payloads

```bash
python main.py -u https://example.com --custom-payloads payloads.txt
```

---

# Scan Modes

## Basic Scan

* Fast
* Common vulnerabilities only
* No chain attacks

## Medium Scan (Default)

* OWASP Top 10 full
* AI analysis
* Optional chain attack detection

## Aggressive Scan

* Deep scanning
* Chain attacks enabled
* Best for pre-production audits

---

# Troubleshooting

### Python Not Found

Install Python 3.8+

### Ollama not running

```bash
ollama serve
curl http://localhost:11434/api/tags
```

### Model missing

```bash
ollama pull llama3.2:3b
```

### GUI not opening

```bash
sudo apt install python3-tk
```

### Dependencies issue

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

# Help & Support

### CLI Help:

```bash
python sudarshan.py --help
python verify_installation.py
```

---

# Legal Notice

SUDARSHAN is for:

* Authorized security testing
* Educational usage
* Systems where you have explicit written permission

Unauthorized scanning is illegal.

---

# Author

**Developer:** Yaswant Pandey
**Email:** [mrindianh27@gmail.com](mailto:mrindianh27@gmail.com)
**GitHub:** [https://github.com/indianhacker126](https://github.com/indianhacker126)

---

# License

MIT License

---

# Acknowledgments

* Ollama
* Meta AI
* OWASP
* Security Community

---

© 2025 Yaswant Pandey. All Rights Reserved.

```

```
