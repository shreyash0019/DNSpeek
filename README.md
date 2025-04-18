# DNSpeek

A lightweight Python script to quickly retrieve the IP address of any website based on its hostname using the built-in `socket` library.

---

## 🌐 What It Does
- Takes a website URL as input
- Resolves and prints its hostname
- Fetches and displays the corresponding IP address

---

## 🚀 Usage

### 1. Clone the Repository
```bash
git clone https://github.com/shreyash0019/DNSpeek.git
cd DNSpeek
```

### 2. Run the Script
```bash
python dnspeek.py
```

### 3. Sample Interaction
```
Please enter website address (URL): google.com
Hostname: google.com
IP Address: 142.250.183.206
```

---

## ⚙️ How It Works
The script uses Python's built-in `socket` module to perform DNS resolution:
```python
socket.gethostbyname(hostname)
```

---

## 📦 Requirements
No external libraries required. Runs with any standard Python installation (3.x).

---

## 📌 Example Use Cases
- Quick DNS lookup without a browser
- Debugging hostname resolution
- Educational tool to understand basic networking in Python

---

## 🤝 Contributing
Found a bug or want to add enhancements? Pull requests are welcome!

---
