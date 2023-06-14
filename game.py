player = input("Please enter your name here ---> ").lower

class Room:
    def __init__ (self, name, tools, prompt, background):
        self.name = name 
        self.tools = tools
        self.prompt = prompt

        self.map = {}
        # self.items 
        self.background = background

    def add_map(self, top, right, down, left):
        self.map['top'] = top
        self.map['right'] = right
        self.map['down'] = down
        self.map['left'] = left
        



class Game:

    ER = Room("Engine Room", "", "Optional room to enter. Only there for immersiveness.", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4dd0906b-fdff-4f40-9658-ebf80b146d6c/da7jro9-2ff2e668-a063-43f9-b79e-2c9f4f53e611.jpg/v1/fill/w_1024,h_575,q_75,strp/engine_room_by_kypcaht_da7jro9-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTc1IiwicGF0aCI6IlwvZlwvNGRkMDkwNmItZmRmZi00ZjQwLTk2NTgtZWJmODBiMTQ2ZDZjXC9kYTdqcm85LTJmZjJlNjY4LWEwNjMtNDNmOS1iNzllLTJjOWY0ZjUzZTYxMS5qcGciLCJ3aWR0aCI6Ijw9MTAyNCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.TET31UwzEsRQBRP2fbohnAeGcdO7Ndznc_mcnb83p7s")
    CF = Room("Cafeteria", "", "First room player should be allowed to enter after spawn pt. Objective:Pass to airlock(cannot enter airlock w/o pass in inventory)", "https://i.pinimg.com/736x/88/fc/1f/88fc1f76dcd2e315f1a11515a0c815a9--scifi-interior-space-station.jpg")
    SP = Room("Spawn Point", "", "Player is prompted with a backstory as to why they have randomly woken up here (Could be bedroom instead of spawn pt.)", "https://i.ytimg.com/vi/qQvep-jJicg/maxresdefault.jpg")
    CC = Room("Control Center", "", "Last place player should enter, also cannot enter without pass for airlock", "https://media.istockphoto.com/id/1211233381/photo/spaceship-interior-with-view-on-space-and-distant-planets-system-3d-rendering.jpg?s=612x612&w=0&k=20&c=_Dbn5EufB3sUmmCseMGSY2wLX-oJzM6aauG4nfSVB0Y=")
    AR = Room("Airlock", "", "Player will find a key and be prompted to catch it in a short time framed sequence(Sequence starts once audio cue goes off) If the player fails they die", "https://i.pinimg.com/originals/69/80/94/698094b03928865aa984eb5602198d3d.jpg")
    MB = Room("Medbay", "", "Possible threat in this room...If player doesnt have a weapon when dealing w a threat, there is a suicide option", "https://gamestudio.champlain.edu/wp-content/uploads/2021/10/megan-tyler-Sci_Fi_Med_Bay.jpg")
    GA = Room("General Area", "", "Weapons in this room. Should be the first room players walks into when leaving cafeteria.", "https://imagedelivery.net/9sCnq8t6WEGNay0RAQNdvQ/UUID-cl9b8wql61990sfn6y8hzvkfe/public")
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
