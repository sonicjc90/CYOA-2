player = input("Please enter your name here ---> ").lower

class Room:
    def __init__ (self, name, tools, prompt):
        self.name = name 
        self.tools = tools
        self.prompt = prompt

        self.map = {
            'right':
            'up':
            'down':
            'left':
        }
        self.items 
        self.background 


class Game:

    ER = Room("Engine Room", "", "")
    CF = Room("Cafeteria", "", "")
    SP = Room("Spawn Point", "", "")
    CC = Room("Control Center", "", "")
    AR = Room("Airlock", "", "")
    MB = Room("Medbay", "", "")
    GA = Room("General Area", "", "")
    LOCATIONS = [SP, ER, CF, CC, AR, MB, GA]
    

    def __init__(self, name, gender):
        self.player_name = name
        self.player_gender = gender
        self.location = self.SP
        self.inventory = []

    def go_right(self):
        #use current location to set the right location
        self.location = self.location.map.right









room_dir =  {
    "top 1" : "Control Center",
    "top 2" :  "Cafeteria",
    "middle1" : "Airlock",
    "middle2" : "Medbay",
    "middle3" : "General Area",
    "bottom1" : "Spawn Point",
    "bottom2" : "Engine Room",
}
