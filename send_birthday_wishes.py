import json
# Import smtplib for the actual sending function
import smtplib
import time
# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import os
from datetime import datetime

gmail_id = os.environ.get('GMAIL_ID')
gmail_pwd = os.environ.get('GMAIL_PWD')

def send_email(data):
    sending_ts = datetime.now()

    contacts = ['gideon.realmdigital@gmail.com', 'mamaboloben21@gmail.com']

    sub = "Birthday wishes %s" % sending_ts.strftime('%Y-%m-%d %H:%M:%S')
    msg = MIMEMultipart('alternative')
    msg['From'] = 'gideonbenjamin28@gmail.com'
    msg['To'] = ' , '.join(contacts)
    msg['Subject'] = sub

    body = ("""\
    <body>
    <div class="card">
     <div class="back"></div>
    <div class="front">
    <div class="imgset">
         <img width="100%" src="https://1.bp.blogspot.com/-Mgj9-rbs65E/XfMoPSD5gtI/AAAAAAAAURk/NBokE2gSS2cTSJ2em5lZ5hJDuTtRN7UVwCLcBGAsYHQ/s1600/2713997.png">
       </div>
    </div>
    <div class="text-container">
    <p id="head">Happy Birthday </p>
    <p>I hope your special day will bring you lots of happiness, love, and fun. You deserve them a lot. Enjoy!</p>
    <p>Hope your day goes great!</p>
    </div>
    </div>
  
    </body>
    """)

    msg.attach(MIMEText(body, _subtype='html'))

    attachment = MIMEText(json.dumps(data))
    attachment.add_header('Content-Disposition', 'attachment', 
                          filename="birthdays.json")
    msg.attach(attachment)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(gmail_id, gmail_pwd)
        smtp.send_message(msg)

        #schedule.every(2).seconds.do(send_email(data))
        #while True:
            #schedule.run_pending()
            #time.sleep(1)

    return 0

if __name__=="__main__":
    data = {"id": "101","name": "Anders2", "lastname": "Hejlsberg" , "dateOfBirth": "1960-12-02T00:00:00"
        , "employmentStartDate": "2001-03-01T00:00:00" , "employmentEndDate": "null" , "lastNotification": "2021-06-04" , "lastBirthdayNotified": "2022-05-04"}
    send_email(data)


