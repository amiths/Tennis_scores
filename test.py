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


def send_mail(email_msg):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("stinson840@gmail.com", "iamamith")
	server.sendmail("stinson840@gmail.com", "amith171@gmail.com", email_msg)
	server.quit()

def send_sms(message):
	ACCOUNT_SID = "ACd8192adb889cc018bdabf489f3a05099"
	AUTH_TOKEN = "0d6ccbe6f3af4b0a4d5ece0dba4d2ff6"
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

	message = client.messages.create(
  		body=message,  # Message body, if any
		to="+13527459695",
     	from_="+13524152798",
 	)
 	print "sms sent"


def main():



	f = urllib2.urlopen("http://www.scorespro.com/rss2/live-soccer.xml")
	text = f.info()
	page = f.read()
	soup = BeautifulSoup(page, "html.parser")
	titles = re.findall(r'<description>(.*)</description>',page)

	message = ""

	for title in titles:	
		if '.com' in title:
			pass
		else:
			message += title + '\n'
	#print message

	print "Choose notification type:\n1) Email\n2) SMS\n3) Exit"
	choice = int(raw_input())

	if (choice == 1):
		email_msg = """\
		From: From Amio <stinson840@gmail.com>
		To: To Pogo <amith171@gmail.com>
		Subject: Live Scores

		"""

		email_msg += message
		send_mail(email_msg)

	if (choice == 2):
		send_sms(message)

	else:
		return

if __name__ == '__main__':
	main()



# Notifier.notify("Live Score")
# Notify.Notification('Live Score', "Random", "dialog-information").show()



#def notify(title, text):
# os.system("""
#               osascript -e 'display notification "{}" with title "{}"'
#               """.format("email_msg",message))

#notify("Title", "Heres an alert")

