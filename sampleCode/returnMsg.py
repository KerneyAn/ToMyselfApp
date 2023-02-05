import mimetypes
from flask import Flask, Response, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
#from https://github.com/cduong21/Twilio_HowToSMS

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid =
auth_token = 
client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body = request.values.get('Body').lower()
    resp = MessagingResponse()

    if body == 'yes':
        resp.message("We are glad you enjoyed Drip2Duong Coffee!")
    elif body == 'no':
        resp.message("We are sorry to here that.")
    else:
        resp.message("Please respond to Drip2Duong with yes or no. If you wish to unsubscribe text stop")

    return Response(str(resp), mimetype="application/xml")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
