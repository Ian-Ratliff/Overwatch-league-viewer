#Random Import stuff
from selenium import webdriver
from selenium.common.keys import keys
#Creates a prompt for starting the program

userInfo = []
print("Welcome to the Overwatch League Viewer, this is a auto watcher. ")
print("Please provide your twitch username")
username = input()
userInfo.append(username)
print("Please provide twitch password")
password = input()
userInfo.append(password)

open("browser launch.py")

