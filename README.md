# ISS Alert System 🛰️

Python scripts to track the International Space Station (ISS) and send WhatsApp alerts when it passes near your location.

## What changed (recent updates)
- Added CSV logging: overhead sightings are now appended to `iss_entry.csv` for record-keeping.
- Security improvement: credentials are read from environment variables (uses python-dotenv). This fixes prior privacy leaks.
- README typos and file-name guidance corrected (now recommends `ISS_tracker.py` for production).

---

## Files
- ISS_tracker.py — Production-ready: sends a WhatsApp alert only when the ISS is overhead and logs sightings to `iss_entry.csv`.
- ISS_tracker_exp.py — Experimental: useful for testing and learning but sends many messages (not recommended for long runs).

---

## Quick start
1. Install dependencies:

```
pip install requests twilio python-dotenv
```

2. Create a `.env` file in the repo root with these variables:

```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
NUMBER=+91xxxxxxxxxx    # your WhatsApp number in E.164 format (used as TO)
```

3. Run the production script (recommended):

```
python ISS_tracker.py
```

The script appends each overhead sighting to `iss_entry.csv` with timestamp and coordinates.

---

## Configuration notes
- The Twilio "from" number remains the Twilio WhatsApp sandbox number by default (`whatsapp:+14155238886`).
- Do not commit `.env` or credentials to version control. Use environment variables for deployment.
- Adjust the default coordinates in `ISS_tracker.py` to your location if needed.

---

## Recommendation
Use `ISS_tracker.py` for real monitoring (efficient, logs sightings). Keep `ISS_tracker_exp.py` for experimentation only — it will consume Twilio messages quickly.

---

## License
Educational / learning purposes.

