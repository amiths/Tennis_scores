#!/usr/bin/python
import sys
import re
import os
import shutil
import urllib2
import time
from bs4 import BeautifulSoup
import smtplib
from twilio.rest import TwilioRestClient



f = urllib2.urlopen("http://www.scorespro.com/rss2/live-soccer.xml")
#time.sleep(1)
text = f.info()
#print(text)
page = f.read()
#print (page)
soup = BeautifulSoup(page, "html.parser")
file = open('test.txt','w')
file.write(page)
#print(soup.prettify())
#print(soup.table)
#print soup
titles = re.findall(r'<description>(.*)</description>',page)

message = ""

for title in titles:	
	if '.com' in title:
		pass
	else:
		message += title + '\n'
print message

email_msg = """From: From Amio <stinson840@gmail.com>
To: To Pogo <amith171@gmail.com>
Subject: Live Scores

"""

email_msg += message


# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login("stinson840@gmail.com", "iamamith")
 

# server.sendmail("stinson840@gmail.com", "pragna255@gmail.com", email_msg)
# server.quit()


# To find these visit https://www.twilio.com/user/account




# ACCOUNT_SID = "ACd8192adb889cc018bdabf489f3a05099"
# AUTH_TOKEN = "0d6ccbe6f3af4b0a4d5ece0dba4d2ff6"

# client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

# message = client.messages.create(
#     body=email_msg,  # Message body, if any
#     to="+13527459695",
#     from_="+13524152798",
# )


# Notifier.notify("Live Score")
# Notify.Notification('Live Score', "Random", "dialog-information").show()



#def notify(title, text):
# os.system("""
#               osascript -e 'display notification "{}" with title "{}"'
#               """.format("email_msg",message))

#notify("Title", "Heres an alert")

