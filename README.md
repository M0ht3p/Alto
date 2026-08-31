<img width="1600" height="736" alt="image" src="https://github.com/user-attachments/assets/dbd02536-6b4a-4748-9a60-8aebff1efb56" />

# Alto
![License](https://img.shields.io/badge/license-MIT-green)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)

**Discover the interactive WikINT Alto**

🔍 Alto — Interactive OSINT Tool Recommendation Engine

Alto is an interactive, decision-matrix recommendation engine built for Open Source Intelligence (OSINT) practitioners, threat intelligence analysts, and researchers.

Instead of searching through static link lists, Alto takes your current investigative starting points (e.g., username, email, IP address) and desired research goals to immediately recommend the exact OSINT tools, frameworks, and methodologies best suited for your objective.

✨ **Features :**

 Goal-Oriented Discovery: Filter tools based on what you are trying to achieve (e.g., Username Enumeration, Breach Analysis, Domain Infrastructure, Geolocation).

Context-Aware Recommendations: Factors in the starting data you currently hold to refine tool recommendations.

Direct Links & Categorization: Every recommendation provides clear tool descriptions, access types (Free, Open-Source, Freemium), and direct links to repository pages or web applications.

Lightweight & Fast: Built on top of Python and Streamlit for an intuitive interface.

**⚖️ Ethics & Responsible Use :**

Alto is designed strictly for educational, defensive, and lawful research purposes. All tools recommended within this platform rely exclusively on publicly available data (OSINT) and passive intelligence collection techniques. Users are expected to respect rate limits, adhere to target terms of service, and comply with local cybersecurity regulations.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## 🛠️ Local Installation & Usage

If you want to run **Alto** locally on your machine:

1. **Clone the repository**
   ```bash
   git clone [https://github.com/M0ht3p/Alto.git](https://github.com/M0ht3p/Alto.git)
   cd Alto
   ```

2. **Install dependencies**
```bash
   pip install -r requirements.txt
```

3. **Launch the application**
```bash
   streamlit run v2.2.py
```
