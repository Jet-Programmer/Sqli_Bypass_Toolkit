🧠 SQLi Bypass Toolkit – Changelog

Track the evolution of this elite login-busting recon agent. Every release. Every upgrade. Every exploit.

---

[v1.0.0] – 2025-07-02
🔥 Initial Strike Deployment

✨ Added
- **Automated SQL Injection Login Bypass**  
  Rotates through curated payloads to exploit weak login forms.

- **Flag Sniper Mode**  
  After successful bypass, auto-targets `/admin.php` to extract `flag{}` tokens.

- **Dynamic Target Targeting**  
  `--target` flag lets users inject custom login URLs for testing live instances.

- **Session Cookie Interception**  
  Add `--cookie` to bypass login walls that rely on active sessions.

- **Payload Customization**  
  Support for user-supplied wordlists via `--wordlist` for advanced payload testing.

- **Colorized CLI Output**  
  Instantly spot success/fail payloads in red/green terminal glory 🌈

- **.deb Installer for Kali & Linux**  
  Packaged for plug-and-play on offensive boxes via `dpkg -i`

---🛠️ Tool Architecture
- CLI-based, portable, no dependencies outside Python 3 and standard libs
- Fully operational inside virtual labs, CTFs, and hardened target assessments
- Easy to clone, fork, and mod for variant recon missions

---🙌 Author
**Sanctification Yeboah a.k.a Jet-Programmer**  
Builder of ethical recon tools. Champion of precision payloads.

---

🧤 Stay tuned for:  
- `--export` JSON/CSV reporting  
- XSS payload support  
- Modular scanner architecture  
- GitHub badge & release badges incoming!
