import time 
import requests 
import os
from twilio.rest import Client
from dotenv import load_dotenv
from ISS_tracker import save_iss_location
load_dotenv()
twilio_sid = "YOUR_TWILIO_SID"
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
from_no = "whatsapp:+14155238886"
to_no = f"whatsapp:{os.environ.get("NUMBER")}"

def send_whatsapp_alert(lat,lon):
    try:
        client = Client(account_sid, auth_token)
        message_body = f"🚀 LOOK UP! The ISS is passing directly over you right now!\n🛰️ Current Location: ({lat}, {lon})"
        message = client.messages.create(body = message_body, from_ = from_no, to = to_no)
        print(f"[{time.strftime('%H:%M:%S')}] WhatsApp alert sent successfully! SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send the message: {e}")

def not_overhead_alert(lat,lon):
    try:
        client = Client(account_sid, auth_token)
        message_body = f" Current Location location of ISS: ({lat}, {lon}, not close to you.)"
        message = client.messages.create(body = message_body, from_ = from_no, to = to_no)
        print(f"[{time.strftime('%H:%M:%S')}] WhatsApp alert sent successfully! SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send the message: {e}")


def is_iss_overhead(my_lat=28.627,my_lon = 79.8042 ):

    already_sent = False
    url = "http://api.open-notify.org/iss-now.json"
    while True:
        sleeptime = 10
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                iss_lat = float(resp.json()["iss_position"]["latitude"])
                iss_lon = float(resp.json()["iss_position"]["longitude"])

                is_iss_here = abs(iss_lat - my_lat)< 5 and abs(iss_lon - my_lon) < 5
                
                if is_iss_here:
                    if not already_sent:
                        send_whatsapp_alert(iss_lat,iss_lon)
                        already_sent = True
                        save_iss_location(iss_lat, iss_lon)
                    else:
                        print((f"[{time.strftime('%H:%M:%S')}] ISS is overhead, but alert was already sent for this pass."))
                    sleeptime = 5  # Wait for 5 seconds before checking again
                else:
                    if already_sent:
                        print("The ISS has left your airspace. Resetting alert trigger for next time.")
                        already_sent = False
                    not_overhead_alert(iss_lat,iss_lon)
                    sleeptime = 10  # Wait for 10 seconds before checking again

            else:
                print(f"API returned an error code: {resp.status_code}")
                sleeptime = 30
        except requests.exceptions.RequestException as e:
            print(f"Network glitch encountered: {e}. Retrying...")
            sleeptime = 15
        time.sleep(sleeptime)
        
        

if __name__ == "__main__":
    sure = input("Are you sure you want to run the ISS overhead alert script? (y/n): ").strip().lower()
    if sure == "y":
        is_iss_overhead(28.6279,79.8042)
    else:
        print("Exiting the script. No alerts will be sent.")
