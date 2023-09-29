import smtplib
import os

carriers = {
	'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
}

def send(message):
	number = os.environ.get('phone_number')
	to_number = number.format(carriers['verizon'])
	auth = (os.environ.get('email'), os.environ.get('emailapikey'))

	# Establish a secure session with gmail's outgoing SMTP server using your gmail account
	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	server.starttls()
	server.login(auth[0], auth[1])

	# Send text message through SMS gateway of destination number
	server.sendmail(auth[0], to_number, message)


