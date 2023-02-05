# Download the helper library from https://www.twilio.com/docs/python/install
from datetime import datetime, timedelta
import os
from twilio.rest import Client

class scheduleTxt:
    # Set environment variables for your credentials
    # Read more at http://twil.io/secure

    def __init__(self,givenTime):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.client = Client(account_sid, auth_token)
        # send the SMS
        self.messaging_service_sid = os.environ.get('TWILIO_MESSAGING_SERVICE_SID')
        #messaging_service_sid = os.environ.get('TWILIO_MESSAGING_SERVICE_SID')

        self.givenTime = givenTime

    def theTimer(self):
        # schedule message to be sent 61 minutes after current time
        #send_when = datetime.utcnow() + timedelta(minutes=61)
        return(datetime.utcnow() + timedelta(minutes=self.givenTime))


    def timedMessage(self,theTime):
        message = self.client.messages.create(
            from_=self.messaging_service_sid,
            to='+1234567890,  # ← your phone number here
            body=input("Write your future message:\n"),
            schedule_type='fixed',
            send_at=theTime.isoformat() + 'Z',
            )


def main():
    myTxtSchedule =  scheduleTxt(61)
    futureTime = myTxtSchedule.theTimer()
    myTxtSchedule.timedMessage(futureTime)
if __name__ == "__main__":
    main()
#print(message.sid)
