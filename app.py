# from flask import Flask, render_template, request
# import json
# # from gpiozero import LED
# # from time import sleep


# app = Flask(__name__)
# led = LED(17)

class Room:
    def __init__ (self, name, tools, prompt)
    self.name = name 
    self.tools = tools
    self.prompt = prompt

ER = Room("Engine Room", "", "")
CF = Room("Cafeteria", "", "")
SP = Room("Spawn Point", "", "")
CC = Room("Control Center", "", "")
AR = Room("Airlock", "", "")
MB = Room("Medbay", "", "")
GA = Room("General Area", "", "")


room_dir =  {
    "top 1" : "Control Center",
    "top 2" :  "Cafeteria",
    "middle1" : "Airlock",
    "middle2" : "Medbay",
    "middle3" : "General Area",
    "bottom1" : "Spawn Point",
    "bottom2" : "Engine Room",
}

name = input("Please enter your name :")
print(name)

