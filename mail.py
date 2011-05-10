import smtplib
import serial
import time
import datetime
from ctypes import *

log = 'C:\mailbox.log'
ser = serial.Serial(4,9600,timeout=1)
smtpserver = 'smtp.example.com'
sender = 'sender@example.com'
receivers = 'receiver@example.com'
message = """From: Mailbox <sender@example.com>
To: Receiver Name <receiver@example.com>
Subject: Post

Mail's here!
At: {when}
"""

while True:
  time.sleep(4)
  output = ser.readline()
  if output == '1':
    timestamp = mail.strftime("%Y-%m-%d %H:%M:%S") + '\n'
    f = open(log, 'a')
    f.write(timestamp)
    f.close()
    print "Mail's here! " + timestamp
    try:
      smtpObj = smtplib.SMTP(smtpserver)
      timestamped_message = message.format(when=timestamp)
      smtpObj.sendmail(sender, receivers, timestamped_message)
    except Exception, e:
      print 'Unable to send mail :-( ' + str(e)
    
  
