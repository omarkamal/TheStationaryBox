import tweepy
from datetime import datetime
import serial
import time
from random import randint

localtime = time.asctime( time.localtime(time.time()) )


# Consumer keys and access tokens, used for OAuth
consumer_key = 'FADWhr61GVD5WB9tFCbzEqvHv'
consumer_secret = 'CGwgkZNTRmKHL4SBoxeO9PqVELjkbauytSwfULZWkBxcJqu2Da'
access_token = '3103176043-rYcrr6qlLDwKfyJHEeGXJeOlfDR7Hj0mHQQKZjU'
access_token_secret = 'H8nUgGH1zz1aJScCz60qfG5EXVWwjHpJxucEVvHLM84PG'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def checkSerial():
	if (serVal):
    		api.update_status(status= "Detected someone close by at " + 
	    	time.strftime("%H:%M:%S"))
	    	time.sleep(5)
	

while True:
	ser = serial.Serial('/dev/tty.usbmodem1411')
	serVal = ser.read()
	val = randint(0,9999)
	checkSerial()
