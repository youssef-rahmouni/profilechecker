![](https://github.com/youssef-rahmouni/profilechecker/other/11.jpg)

# 🔎 ProfileChecker

**ProfileChecker** is a simple Python tool that checks if a username exists on many websites at once. You just run the script, enter the username, and it quickly shows which profiles are found or missing. It uses multiple requests at the same time to be fast and gives clear, easy-to-understand results.

---

## ⚙️ Requirements

- Python 3.7+

---

## 🛠 Installation
```bash
git clone https://github.com/youssef-rahmouni/profilechecker.git
```
 

---

## ▶️ Usage

Run the script:

```bash
cd profilechecker
profilechecker.py
```

Enter the username you want to check when prompted.

The script will:

🔄 Load URL templates from data.json.

🔍 Replace {account} placeholders with the username.

⚡ Check all URLs concurrently.

📊 Display progress and results.

📋 Summarize total profiles found/not found and elapsed time.

---

## ⚙️ Configuration

data.json
A JSON file containing URL templates with {account} placeholders is from Sherlock.
Example entry:

```bash
{
  "site1": {"url": "https://www.example.com/user/{account}"},
  "site2": {"url": "https://profiles.example2.org/{account}"}
}
```

---

## 📝 Example
```bash
[*] Enter username: johndoe
[*] Starting profile checks for user 'johndoe' on 300 sites...

[+] Profile exists: https://www.example.com/user/johndoe
[+] Profile exists: https://profiles.example2.org/johndoe
[ERROR] Profile error for https://unknownsite.com/user/johndoe

...

[*] Total Profiles exists: 15/300
[*] Total Profiles not exists: 285/300
[*] Time taken: 45.67s

✔ Script finished successfully!
```

---

## 👤 Created by

Youssef Rahmouni
