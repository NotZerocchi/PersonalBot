import os
import webbrowser

opt = []

def cls():
	return os.system('cls' if os.name=='nt' else 'clear')

def cmd(txt):
	spl = txt.split() #splitting the command into individual string
	for word in spl:
		opt.append(word) #append the strings into list
	return opt

def content(opt,key):
	keyword = opt[opt.index(key)+1:] #take the keyword after the word "wiki"
	keyword = " ".join(keyword) #join the given strings in list by delimiter
	return keyword

def web(url):
	webbrowser.open("http://" + url)

def wiki(word):
	webbrowser.open("http://en.wikipedia.org/wiki/" + word)

def google(word):
	webbrowser.open("https://www.google.com/search?q=" + word)


