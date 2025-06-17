# Broken Authentication Lab

A terminal-style interactive web lab to teach key weaknesses in modern authentication systems.

## Stack
- Python + Flask
- SQLite (optional backend storage)
- HTML/CSS/JS (Terminal inspired UI)

## Educational Modules
Each module is designed to teach a security flaw:
- Module 1: Weak login (brute-force, no rate limit)
- Module 2: Password reset (predictable tokens)
- Module 3: Rate-limiting bypass
- Module 4: MFA bypass
- Module 5: CAPTCHA logic flaw

## Hosting
Deploy via [GitHub Pages](https://pages.github.com) using only the frontend if needed.

## Learn More
- OWASP: https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
- Flask: https://flask.palletsprojects.com/
- Rate-limiter: https://flask-limiter.readthedocs.io
