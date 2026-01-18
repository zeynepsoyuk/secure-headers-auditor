# Secure Headers Auditor

**Secure Headers Auditor** is a Python-based cybersecurity tool designed to analyze, score, and report the presence of HTTP security headers on web applications.

This project was developed as a **Term Project** to demonstrate secure coding practices, asynchronous programming, and automated security auditing based on **OWASP** recommendations.

---

## Features

* **Asynchronous Scanning:** Uses `asyncio` and `aiohttp` to scan multiple targets concurrently for high performance.
* **Security Scoring Engine:** strict grading system (A+ to F) based on the presence of critical headers like `HSTS`, `CSP`, and `X-Frame-Options`.
* **Detailed Reporting:** Generates a comprehensive CSV report and a console summary.
* **Modular Architecture:** Clean separation of concerns (Scanner, Analyzer, Reporter) following PEP8 standards.
* **Robust Error Handling:** Handles timeouts, connection errors, and bot protection mechanisms (403/429).

---

## Technology Stack

* **Language:** Python 3.8+
* **Networking:** `aiohttp` (Asynchronous HTTP Client)
* **Data Processing:** `pandas` (DataFrames & CSV Export)
* **Testing:** `pytest` (Unit & Integration Tests)
* **Configuration:** `python-dotenv` (Environment Variable Management)

# Status Explanation
200- Successful
403- Forbidden 
404- Not Found
500- Server Error
---

## Project Structure

```text
secure-headers-auditor/
│
├── app/                  # Core application modules
│   ├── scanner.py        # Async HTTP scanning engine
│   ├── analyzer.py       # Scoring logic and grading algorithm
│   ├── reporter.py       # CSV and Console reporting
│   └── utils.py          # Logger and configuration helpers
│
├── tests/                # Test suite
│   └── test_auditor.py   # Unit tests for analyzer logic
│
├── logs/                 # Application logs
├── .env                  # Configuration (Timeout, User-Agent)
├── main.py               # Entry point of the application
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation

# INSTALLATION

-Clone the Repository

git clone [https://github.com/your-username/secure-headers-auditor.git](https://github.com/your-username/secure-headers-auditor.git)
cd secure-headers-auditorInstallation

-Create a Virtual Environment

# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

-Install Dependencies

pip install -r requirements.txt

-Configuration (.env) Ensure the .env file exists in the root directory

TIMEOUT=10
LOG_LEVEL=INFO
USER_AGENT="Mozilla/5.0 (Compatible; SecurityAuditor/1.0)"

# USAGE

python main.py (to start)