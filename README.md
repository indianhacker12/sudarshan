# 🛡️ SUDARSHAN AI Security Scanner

<div align="center">

![Sudarshan Logo](logo.png)

**Professional AI-Powered Web Application Security Testing Platform**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![AI Powered](https://img.shields.io/badge/AI-LLaMA%203.2-orange.svg)](https://ollama.ai)
[![OWASP](https://img.shields.io/badge/OWASP-Top%2010%202021-red.svg)](https://owasp.org)
[![Security](https://img.shields.io/badge/Security-Scanner-brightgreen.svg)](https://github.com/indianhacker12/sudarshan)

[🚀 Quick Start](#installation) • [📖 Documentation](#usage) • [🎯 Features](#key-features) • [🤝 Contributing](#contributing) • [💬 Support](#support)

</div>

---

## 🎯 What is SUDARSHAN?

**SUDARSHAN** (Security Testing & Risk Assessment with Vulnerability Analysis) is a cutting-edge **AI-powered web application security scanner** that combines traditional penetration testing with advanced artificial intelligence to deliver comprehensive security assessments.

### 🌟 Why Choose SUDARSHAN?

- 🤖 **AI-Powered Intelligence**: LLaMA 3.2 integration for smart vulnerability detection
- 🎯 **OWASP Top 10 2021**: Complete coverage of latest security standards  
- 🔍 **Advanced Reconnaissance**: Deep target analysis and fingerprinting
- 📊 **Professional Reports**: Executive summaries and technical details
- 🌐 **Multiple Interfaces**: CLI, GUI, and Web-based scanning
- ⚡ **High Accuracy**: 85%+ detection rate with false positive reduction

---

## 🚀 Key Features

### 🛡️ Security Testing Coverage
- **SQL Injection**: Advanced SQLi detection and exploitation
- **Cross-Site Scripting (XSS)**: Reflected, Stored, and DOM-based
- **Command Injection**: OS command execution vulnerabilities
- **File Upload Vulnerabilities**: Malicious file upload detection
- **Authentication Bypass**: Login mechanism weaknesses
- **Authorization Flaws**: Access control vulnerabilities
- **Server-Side Request Forgery (SSRF)**: Internal network access
- **Path Traversal**: Directory traversal attacks
- **Information Disclosure**: Sensitive data exposure
- **Security Misconfigurations**: Server and application settings

### 📊 Professional Reporting
- **HTML Reports**: Detailed vulnerability documentation
- **JSON Export**: Machine-readable results
- **Executive Summaries**: Business impact analysis
- **Risk Scoring**: CVSS-based vulnerability rating
- **Remediation Guidance**: Step-by-step fix instructions

---

## 🔧 Installation

### Prerequisites
- Python 3.8 or higher
- 4GB RAM (8GB recommended)
- 5GB free disk space
- Internet connection for AI model downloads

### Quick Install

#### Windows
```bash
git clone https://github.com/indianhacker12/sudarshan.git
cd sudarshan
install.bat
```

#### Linux/macOS
```bash
git clone https://github.com/indianhacker12/sudarshan.git
cd sudarshan
chmod +x install.sh
./install.sh
```

### Manual Installation
```bash
git clone https://github.com/indianhacker12/sudarshan.git
cd sudarshan
pip install -r requirements.txt
```

---

## 🎮 Usage

### 🖥️ GUI Mode (Recommended)
```bash
python sudarshan.py --gui
```

### 🌐 Web Interface
```bash
python sudarshan.py --web
# Access: http://localhost:5000
```

### ⌨️ CLI Mode

#### Basic Scan
```bash
python sudarshan.py -u https://example.com --basic
```

#### Standard Scan (OWASP Top 10)
```bash
python sudarshan.py -u https://example.com
```

#### Aggressive Scan (Full AI Analysis)
```bash
python sudarshan.py -u https://example.com --aggressive
```

#### Advanced Options
```bash
python main.py -u https://example.com --owasp-all --chain-attacks --verbose
```

---

## 📋 Scan Modes

| Mode | Speed | Coverage | AI Analysis | Best For |
|------|-------|----------|-------------|----------|
| **Basic** | ⚡ Fast | Common vulns | ❌ | Quick assessment |
| **Medium** | 🔄 Standard | OWASP Top 10 | ✅ | Regular testing |
| **Aggressive** | 🐌 Thorough | Full coverage | ✅✅ | Comprehensive audit |

---

## 🎯 Supported Vulnerabilities

<details>
<summary><b>OWASP Top 10 2021 Coverage</b></summary>

| ID | Category | Tests Included |
|----|----------|----------------|
| **A01** | Broken Access Control | IDOR, Privilege Escalation, Path Traversal |
| **A02** | Cryptographic Failures | SSL/TLS Issues, Weak Encryption |
| **A03** | Injection | SQL, NoSQL, LDAP, Command, XXE |
| **A04** | Insecure Design | Logic Flaws, Business Logic |
| **A05** | Security Misconfiguration | Default Configs, Error Handling |
| **A06** | Vulnerable Components | Outdated Software Detection |
| **A07** | Authentication Failures | Weak Passwords, Session Issues |
| **A08** | Data Integrity Failures | Deserialization, Supply Chain |
| **A09** | Logging Failures | Security Event Logging |
| **A10** | Server-Side Request Forgery | SSRF, Internal Network Access |

</details>

---

## 🛠️ System Requirements

### Minimum Requirements
- **OS**: Windows 10/11, Linux (Ubuntu 18+), macOS 10.15+
- **Python**: 3.8+
- **RAM**: 4GB
- **Storage**: 5GB free space
- **Network**: Internet connection for AI models

### Recommended Specifications
- **RAM**: 8GB+
- **CPU**: 4+ cores
- **Storage**: 10GB+ SSD
- **Network**: Stable broadband connection

### Tested Platforms
- ✅ Kali Linux 2023+
- ✅ Parrot Security OS
- ✅ Ubuntu 20.04/22.04
- ✅ Windows 10/11
- ✅ macOS Big Sur+

---

## 📚 Documentation

- [📖 Installation Guide](docs/INSTALLATION.md)
- [🎯 Usage Examples](docs/USAGE.md)
- [🔧 Configuration](docs/CONFIGURATION.md)
- [🤖 AI Features](docs/AI_FEATURES.md)
- [📊 Reporting](docs/REPORTING.md)
- [🛠️ Troubleshooting](docs/TROUBLESHOOTING.md)

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md).

### Ways to Contribute
- 🐛 Report bugs and issues
- 💡 Suggest new features
- 🔧 Submit pull requests
- 📖 Improve documentation
- 🧪 Add test cases

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⚖️ Legal Notice

**⚠️ IMPORTANT: This tool is for AUTHORIZED SECURITY TESTING ONLY**

- ✅ Only scan systems you own or have explicit written permission to test
- ❌ Unauthorized scanning may violate computer crime laws
- 👤 Users are responsible for complying with all applicable laws
- 🛡️ The developers assume no liability for misuse

---

## 👨‍💻 Author

**Yaswant Pandey**
- 📧 Email: [mrindianh27@gmail.com](mailto:mrindianh27@gmail.com)
- 🐙 GitHub: [@indianhacker12](https://github.com/indianhacker12)
- 🌐 Website: [Coming Soon]

---

## 🙏 Acknowledgments

- 🤖 [Ollama](https://ollama.ai) - AI model infrastructure
- 🧠 [Meta AI](https://ai.meta.com) - LLaMA model development
- 🛡️ [OWASP](https://owasp.org) - Security standards and guidelines
- 🌍 Security research community

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/indianhacker12/sudarshan?style=social)
![GitHub forks](https://img.shields.io/github/forks/indianhacker12/sudarshan?style=social)
![GitHub issues](https://img.shields.io/github/issues/indianhacker12/sudarshan)
![GitHub license](https://img.shields.io/github/license/indianhacker12/sudarshan)

---

## 🔗 Related Projects

- [OWASP ZAP](https://github.com/zaproxy/zaproxy) - Web application security scanner
- [Burp Suite](https://portswigger.net/burp) - Professional security testing
- [Nuclei](https://github.com/projectdiscovery/nuclei) - Vulnerability scanner
- [SQLMap](https://github.com/sqlmapproject/sqlmap) - SQL injection tool

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

**Made with ❤️ by [Yaswant Pandey](https://github.com/indianhacker12)**

</div>