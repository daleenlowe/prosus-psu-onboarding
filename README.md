# Prosus PSU Board Onboarding — Streamlit App

A password-protected, interactive onboarding dashboard for board members on Prosus Performance Share Units (PSUs). Built with Streamlit and ready for deployment to Streamlit Community Cloud.

## Deploying to Streamlit Community Cloud

1. Push this folder to a GitHub repository (public or private — private is recommended for board materials)
2. Go to [https://share.streamlit.io](https://share.streamlit.io)
3. Click **"New app"** → select your repo → set main file to `app.py`
4. Click **Deploy** — takes approximately 2 minutes

No environment variables or secrets are required. The bcrypt hash is generated at runtime.

## Login credentials

- **Username:** `board_member`
- **Password:** `Prosus2026!`

To change the password, locate the line in `app.py`:

```python
_raw_password = "Prosus2026!"
```

Replace `"Prosus2026!"` with your new password. The bcrypt hash is generated automatically at startup.

## Sharing with external users

Share the Streamlit Cloud URL and the credentials above via a **secure channel** (e.g. encrypted email, Microsoft Teams DM, or a secure file-sharing service). The login page prevents unauthorised access.

For additional security, consider changing the password before sharing and using a unique password per user (requires adding more entries to the `credentials` dict in `app.py`).

## Local development

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

App will open at [http://localhost:8501](http://localhost:8501)

## File structure

```
app.py                  # Main Streamlit application
requirements.txt        # Python dependencies
.streamlit/
  config.toml           # Theme and server configuration
README.md               # This file
```

## Content sections

| Section | Description |
|---|---|
| What are PSUs? | Primer on PSU mechanics and purpose |
| Types of PSUs | Phase 1, 2, and 3 plan design details |
| How performance is measured | Grant → Measurement → Vesting steps |
| Eligibility & current awards | Current in-flight FY25 awards |
| Peer group | Governance rules and company lists |
| Malus & clawback | Recovery provisions |
| Value creation | Placeholder for live TSR data |

## Contact

shares@prosus.com
