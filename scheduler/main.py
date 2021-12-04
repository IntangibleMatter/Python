import time
import csv

commands = {
    "help": """
    help: print list of commands.
    start: start a work timer
    stop: stop a work timer
    """,
    "start": ""
}

class WorkTime:
    
    startTime = 0
    workTime = 0
    endTime = 0
    tasks = "task"
    
    def start(self, timeofstart):
        self.startTime = timeofstart

class TimeRecord:
    pass

class cmd:
    
    
    def get_cmd(self):
        comd = input("$ ")
        
        if comd in commands:
            exec(commands[comd])
        else:
            print("Err. Command not found.")

def mainloop():
    cmdprompt = cmd
    
    while True:    
        cmdprompt.get_cmd()

mainloop()
