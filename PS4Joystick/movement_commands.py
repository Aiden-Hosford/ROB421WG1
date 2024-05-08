from UDPComms import Publisher
import time 

drive_pub = Publisher(8830)

def activate():
    drive_pub.send({"L1": 1, 
            "R1": 0, 
            "x": 0, 
            "circle": 0, 
            "triangle": 0, 
            "L2": 0, 
            "R2": 0, 
            "ly": 0, 
            "lx": 0, 
            "rx": 0, 
            "message_rate": 20, 
            "ry": 0, 
            "dpady": 0, 
            "dpadx": 0})

def move_forward(times):
    drive_pub.send({"L1": 1, "ly": 1, })
    time.sleep(time)
    activate()

def turn_left():
    drive_pub.send({"L1": 1, "lx": -1, })
    time.sleep(5)
    activate()

def turn_right():
    drive_pub.send({"L1": 1, "lx": 1, })
    time.sleep(5)
    activate()

if __name__ == "__main__":
    activate()
    move_forward(times=5)
    turn_left()
    move_forward(times=3)
    turn_right()
    move_forward(times=3)