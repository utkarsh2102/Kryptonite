from RPIO import PWM
from time import sleep
roll = PWM.Servo(0,20000,5)
pitch = PWM.Servo(0,20000,5)
throttle = PWM.Servo(0,20000,5)
yaw = PWM.Servo(0,20000,5)
# start PWM on servo specific GPIO no, this is not the pin no but it is the GPIO no 
roll.set_servo(5,1500)# pin 29
pitch.set_servo(6,1500)# pin 31
throttle.set_servo(13,1150)# pin 33
yaw.set_servo(19,1505)# pin 35
min_throttle = 1150
max_yaw = 1900
min_yaw = 1100
def arm():
    throttle.set_servo(13,min_throttle)  #set to zero
    yaw.set_servo(19,max_yaw)  # set to max  (full right yaw)
    ## others to minimun
    print ("Display Armed!!!!")

def disarm():
    throttle.set_servo(13,min_throttle) # set to zero
    yaw.set_servo(19,min_yaw)  #set to min (full left yaw))
    print ("Display Disarmed!!!!")
try: 
    x = input("Are you ready: yes/no")
    disarm() 
    print ("Armed!!")
    print ("Waiting!!!")
    sleep(10)
    arm()
    print ("Disarmed!!")
except:
       yaw.stop_servo(19)
       roll.stop_servo(5)
       pitch.stop_servo(6)
       throttle.stop_servo(13)
PWM.cleanup()       

