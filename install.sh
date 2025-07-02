#!/bin/bash
echo "[*] Installing SQLi Bypass Module..."
mkdir -p /opt/sqli_bypass
cp sqli_bypass.py sqli_payloads.txt /opt/sqli_bypass
chmod +x /opt/sqli_bypass/sqli_bypass.py
ln -sf /opt/sqli_bypass/sqli_bypass.py /usr/local/bin/sqli_bypass
echo "[+] Installed. Run with: sqli_bypass"
