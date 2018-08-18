from RPIO import PWM

roll = PWM.Servo(0,20000,5)
pitch = PWM.Servo(0,20000,5)
throttle = PWM.Servo(0,20000,5)
yaw = PWM.Servo(0,20000,5)
# start PWM on servo specific GPIO no, this is not the pin no but it is the GPIO no 
roll.set_servo(5,1500)# pin 29
pitch.set_servo(6,1500)# pin 31
throttle.set_servo(13,1150)# pin 33
yaw.set_servo(19,1505)# pin 35

try: 
   while True:
       x = int(input("CHECK Roll: "))
       roll.set_servo(5,x)
except:
       yaw.stop_servo(19)
       roll.stop_servo(5)
       pitch.stop_servo(6)
       throttle.stop_servo(13)
PWM.cleanup()       



