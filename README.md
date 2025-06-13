# 🔐 Password Breach Checker (SHA-1 / k-Anonymity)

![Screenshot 2025-06-13 163144](https://github.com/user-attachments/assets/1abc632b-ae5e-45c8-a940-fb754390aed0)


A simple Python script that checks if a password has been compromised in known data breaches using the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange). Built with `requests`, `colorama`, and `hashlib`, it demonstrates:

- SHA-1 hashing
- API consumption with `requests`
- Secure password checks using k-Anonymity

---

## ⚙️ Features

- Local password hashing (SHA-1)
- k-Anonymity method (privacy-safe API querying)
- Checks breach count from HIBP database
- Styled CLI interface with `colorama`

---

## 🧪 Example Output

```

Enter a password (: hunter2
This password has been breached 73253 times. It is not secure.

````

---

## 📦 Requirements

- Python 3.6+
- `requests`
- `colorama`

Install dependencies:

```bash
pip install -r requirements.txt
````

---

## 🚀 Usage

Run the script with:

```bash
python main.py
```

Follow the prompt to input a password. It will not be stored or sent in full to the server.

---

## 📚 Learning Goals

* Understand how to interact with APIs securely
* Practice using hash functions and string handling in Python
* Explore ethical cybersecurity techniques

---

## 🔒 Privacy Note

This tool uses a **privacy-conscious** method (k-Anonymity), meaning **your full password is never sent over the internet**. Only the first 5 characters of the SHA-1 hash are sent.

---

## 👤 Author

Made with ♥ by [17xet](https://github.com/17xet)

Discord: @17xet
YouTube: @17xet
Community: [Join the server](https://discord.gg/hKNW6wvyg3)
