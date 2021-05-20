from bscscan import BscScan
bsc = BscScan("API_KEY")
import time
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sendgrid
import os
starting = bsc.get_bnb_balance(address = "address")


email = "email@email.com"
pas = "password"

sms_gateway = '4086640937@messaging.sprintpcs.com'


sg = sendgrid.SendGridAPIClient(api_key='API-KEY')
data = {
  "personalizations": [
    {
      "to": [
        {
          "email": "EMAIL"
        }
      ],
      "subject": "check"
    }
  ],
  "from": {
    "email": "EMAIL"
  },
  "content": [
    {
      "type": "text/plain",
      "value": "CHECK CHECK CHECK"
    }
  ]
}
response = sg.client.mail.send.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)


while True:
    print("hello")
    print(bsc.get_bnb_balance(address = "ADDRESS"))
    print(starting)
    if(bsc.get_bnb_balance(address = "ADDRESS") < starting):
        sg.client.mail.send.post(request_body=data)
        time.sleep(5)
    else:
        starting = bsc.get_bnb_balance(address = "ADDRESS")
    time.sleep(5)

