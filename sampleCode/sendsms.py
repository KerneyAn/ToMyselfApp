import os
from twilio.rest import Client
#https://github.com/cduong21/Twilio_HowToSMS
account_sid =
auth_token =
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        body="What goes best with a cup of coffee? Another cup. \n \nThanks for being a loyal customer, we want to show you some love back \n \nShop our new buy 1 get 1 free promo online.",
        from_='+18332628799',
        # photo needs to be publically avaiable -- upload to flickr
        media_url=['https://live.staticflickr.com/65535/51898195883_13c197808a_b.jpg'],
        # replace with your own number
        to='+phonenumber'
    )

print(message.sid)
