# Broken Authentication Lab

A terminal-themed educational lab to explore OWASP Broken Authentication scenarios:

## Modules
- Weak login auth
- Insecure password reset
- Brute-force rate limiting
- MFA bypass
- CAPTCHA flaws
- Timing attacks
- Replay attacks
- Attack timeline view
- Secure/secure mode toggle

## Run Locally
```bash
docker build -t broken-auth-lab .
docker run -p 5000:5000 broken-auth-lab
```

Or run using Python:
```bash
pip install flask flask-limiter
python app.py
```

## Credits
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
