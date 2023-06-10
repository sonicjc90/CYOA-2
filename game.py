player = input("Please enter your name here ---> ").lower

class Room:
    def __init__ (self, name, tools, prompt):
        self.name = name 
        self.tools = tools
        self.prompt = prompt

        self.map = {}
        # self.items 
        # self.background 

    def add_map(self, top, right, down, left):
        self.map['top'] = top
        self.map['right'] = right
        self.map['down'] = down
        self.map['left'] = left
        # add other directions



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
        self.set_maps()

    def go_right(self):
        #use current location to set the right location
        self.location = self.location.map['right']

    def go_left(self):
        #use current location to set the right location
        self.location = self.location.map['left']

    def go_top(self):
        #use current location to set the right location
        self.location = self.location.map['top']

    def go_down(self):
        #use current location to set the right location
        self.location = self.location.map['down']

    def set_maps(self):
        self.ER.add_map(None, None, self.CC, None)
        self.CF.add_map(None, None, None, self.GA)
        self.SP.add_map(None, self.GA, None, None)
        self.CC.add_map(self.ER, self.AR, self.GA, self.MB)
        self.AR.add_map(None, None, None, self.CC)
        self.MB.add_map(None, self.CC, None, None)
        self.GA.add_map(self.CC, self.CF, None, self.SP)









room_dir =  {
    "top 1" : "Control Center",
    "top 2" :  "Cafeteria",
    "middle1" : "Airlock",
    "middle2" : "Medbay",
    "middle3" : "General Area",
    "bottom1" : "Spawn Point",
    "bottom2" : "Engine Room",
}
