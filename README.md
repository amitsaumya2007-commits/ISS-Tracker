# ISS Alert System 🛰️

This repository contains two Python scripts for tracking the International Space Station (ISS) and sending WhatsApp notifications when it passes overhead your location.

## Project Overview

Both scripts use the **Open-Notify API** to fetch real-time ISS coordinates and the **Twilio API** to send WhatsApp alerts when the ISS is in proximity to a specified location.

---

## 📁 Files

### 1. **project_1.py** (Recommended for Production ⭐)

This is the **efficient and sustainable** version of the ISS alert system.

**Features:**
- Fetches ISS location every 10 seconds
- Sends a WhatsApp alert **ONLY when ISS is directly overhead** (within 5° latitude/longitude)
- Reduces token consumption by only sending messages when necessary
- Includes a confirmation prompt before running to prevent accidental execution
- Fixed sleep interval of 10 seconds between checks

**Why use this?**
✅ Minimal Twilio API calls = preserves free-tier tokens  
✅ Stays within Twilio's free trial limits  
✅ Production-ready with user confirmation  
✅ Most resource-efficient approach

**Default Location:** Mathura, India (28.6279°N, 79.8042°E)

---

### 2. **not_close_alert.py** (Learning & Experimental Only ⚠️)

This script is designed for **learning purposes** and **experimental exploration** of the Twilio API.

**Features:**
- Fetches ISS location every 10 seconds
- Sends alerts in **two scenarios**:
  - WhatsApp message when ISS is overhead
  - WhatsApp message when ISS is **NOT overhead** (every iteration!)
- Sends messages **continuously** throughout execution
- Adaptive sleep intervals based on ISS proximity:
  - 5 seconds when ISS is overhead (for real-time updates)
  - 10 seconds during normal tracking
  - 15 seconds if a network error occurs
  - 30 seconds if the API returns an error

**Why it consumes more tokens:**
❌ Sends alerts on EVERY loop iteration, even when ISS is far away  
❌ The `not_overhead_alert()` function sends a message every 10 seconds continuously  
❌ This rapidly depletes Twilio free-tier tokens (typically ~100 messages/month)  
❌ **Not sustainable** for actual production use  
❌ Even with adaptive sleep times, the constant message sending is inefficient

**Use Cases:**
- Testing and experimenting with the Twilio API
- Learning how WhatsApp integration works
- Debugging message sending functionality
- Understanding API behavior and response handling

⚠️ **Warning:** Do NOT run this script unattended, as it will exhaust your Twilio free credits quickly!

---

## 🚀 Quick Start

### Prerequisites
```bash
pip install requests twilio
```

### Running project_1.py (Recommended)
```bash
python project_1.py
```
The script will ask for confirmation before starting:
```
Are you sure you want to run the ISS overhead alert script? (y/n): y
```

### Running not_close_alert.py (For Learning Only)
```bash
python not_close_alert.py
```

---

## 🔑 Configuration

Both scripts use Twilio credentials to send WhatsApp messages. Update the following variables if needed:

```python
twilio_sid = "your_twilio_account_sid"
twilio_auth_token = "your_twilio_auth_token"
from_no = "whatsapp:+14155238886"  # Twilio sandbox number
to_no = "whatsapp:+91xxxxxxxxxx"    # Your WhatsApp number
```

Modify the default coordinates in the main function:
```python
is_iss_overhead(latitude, longitude)
```

---

## 📊 Comparison

| Feature | project_1.py | not_close_alert.py |
|---------|--------------|-------------------|
| **Purpose** | Production tracking | Learning & Testing |
| **Messages Sent** | Only when ISS overhead | Every 10 seconds (continuously) |
| **Token Usage** | Minimal (sustainable) | High (rapid depletion) |
| **Ideal For** | Real-world use | Experimentation & Learning |
| **User Confirmation** | Yes | No |
| **Adaptive Sleep** | No (fixed 10s) | Yes |
| **Long-term Viability** | ✅ Yes | ❌ No |

---

## 🎯 Recommendation

**Use `project_1.py`** for actual ISS tracking and alerts. It is optimized for long-term use while respecting Twilio's free-tier limitations. This version will sustain your Twilio free access account.

Reserve `not_close_alert.py` for:
- Testing Twilio API integration
- Learning WhatsApp message sending
- Experimenting with alert logic and adaptive sleep intervals
- Development and debugging purposes only

---

## 📍 ISS Coordinates

The default location is set to **Mathura, India** (28.6279°N, 79.8042°E). You can change this to your location by passing custom coordinates to the function:

```python
is_iss_overhead(my_lat, my_lon)
```

---

## 🌐 API Reference

- **Open-Notify API:** http://api.open-notify.org/iss-now.json
  - Returns current ISS latitude and longitude
  - Free to use, no authentication required
  - Response updates every second

- **Twilio API:** WhatsApp messaging service
  - Requires authentication (Account SID and Auth Token)
  - Free tier: Limited messages (~100/month depending on trial status)

---

## ⚠️ Important Notes

1. **Keep credentials private:** Never commit your Twilio SID and Auth Token to version control
2. **Twilio sandbox:** The default numbers are Twilio sandbox numbers. To use personal numbers, verify them first
3. **Free tier limits:** Monitor your Twilio usage to avoid unexpected charges. `not_close_alert.py` will consume tokens rapidly and is not recommended for long-term monitoring
4. **ISS proximity threshold:** Set to 5° in both latitude and longitude (roughly 500+ km), adjustable in the code

---

## 📝 License

This project is for educational and learning purposes.
