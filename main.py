import webbrowser
import os
from ext import util, calc, twitter
from time import strftime

util.cls()
txt = raw_input("> ").lower()
opt = util.cmd(txt)

while "bye" not in opt: 
	if "hi" in opt:
		print "Hi there! The time is " + strftime("%H:%M:%S")
	elif "today" in opt:
		print "Now is", strftime("%A, %d %b %Y %X")
	elif "irc" in opt:
		os.system("irssi")
	elif "thanks" in opt:
		print "You're welcome"
	elif "wiki" in opt:
		keyword = util.content(opt,"wiki")
		util.wiki(keyword)
	elif "open" in opt:
		url = raw_input("Enter the URL: > ")
		util.web(url)
		util.cls()
	elif "print" in opt:
		print opt
	elif "calculate" in opt:
		print "Current available operation: +, -, *, /"
		op = raw_input("Select your operation: > ")
		num1 = input("Enter first number:")
		num2 = input("Enter second number:")
		print "Result: ", calc.simpcalc(num1,num2,op)
	elif "tweet" in opt:
		keyword = util.content(opt,"tweet")
		twitter.tweet(keyword)
		print "Your text has been tweeted!"
	elif "mention" in opt:
		twitter.mention()
	else:
		print "I'm still learning so I might not understand that. Please try again."
	
	del opt[:]
	txt = raw_input("> ").lower()
	opt = util.cmd(txt)
else:
	print "bye!"
