import time 
import requests 
from twilio.rest import Client
twilio_sid = "YOUR TWILIO_SID"
twilio_auth_token = "YOUR TWILIO_AUTH_TOKEN"
from_no = "whatsapp:+14155238886"
to_no = "whatsapp:+917818870589"

def send_whatsapp_alert(lat,lon):
    try:
        client = Client(twilio_sid,twilio_auth_token)
        message_body = f"🚀 LOOK UP! The ISS is passing directly over you right now!\n🛰️ Current Location: ({lat}, {lon})"
        message = client.messages.create(body = message_body, from_ = from_no, to = to_no)
        print(f"[{time.strftime('%H:%M:%S')}] WhatsApp alert sent successfully! SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send the message: {e}")


def is_iss_overhead(my_lat=28.627,my_lon = 79.8042 ):

    already_sent = False
    url = "http://api.open-notify.org/iss-now.json"
    while True:
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
                    else:
                        print((f"[{time.strftime('%H:%M:%S')}] ISS is overhead, but alert was already sent for this pass."))
                else:
                    if already_sent:
                        print("The ISS has left your airspace. Resetting alert trigger for next time.")
                        already_sent = False
                    print(f"[{time.strftime('%H:%M:%S')}] ISS is at Lat: {iss_lat}, Lon: {iss_lon}. Not overhead yet.")
            else:
                print(f"API returned an error code: {resp.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Network glitch encountered: {e}. Retrying...")
        
        time.sleep(10)

if __name__ == "__main__":
    is_iss_overhead(28.6279,79.8042)

