from twilio.rest import Client

def send_alert():
    client = Client("Account SID",
                    "Auth Token")
    client.messages.create(to="Number",
                           from_="Number",
                           body="SECURITY ALERT! Door was opened when system was active.")

def password_alert():
    client = Client("Account SID",
                    "Auth Token")
    client.messages.create(to="Number",
                           from_="Number",
                           body="SECURITY ALERT! 3 failed password attempts.")

