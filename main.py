import sys
sys.path.append("ext")
import webbrowser
import os
import util, calc, twitter
from time import strftime

util.cls()
txt = raw_input("> ").lower()
opt = util.cmd(txt)

class Bot():
	while "bye" not in opt: 
		if "hi" in opt:
			print "Hi there! The time is " + strftime("%H:%M:%S")
		elif "today" in opt:
			print "Now is", strftime("%A, %d %b %Y %X")
		elif "irc" in opt:
			os.system("irssi")
		elif "thanks" in opt:
			print "You're welcome"
		elif "google" in opt:
			keyword = util.content(opt,"google")
			if len(keyword) >= 1:
				util.google(keyword)
			else:
				print "No input entered."
		elif "wiki" in opt:
			keyword = util.content(opt,"wiki")
			if len(keyword) >= 1:
				util.wiki(keyword)
			else:
				print "No input entered."
		elif "open" in opt:
			url = raw_input("Enter the URL: > ")
			if len(keyword) >= 1:
				util.web(url)
			else:
				print "No input entered."
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
