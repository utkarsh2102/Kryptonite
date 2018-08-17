from RPIO import PWM


roll = PWM.Servo(0,20000,10)
pitch = PWM.Servo(0,20000,10)
throttle = PWM.Servo(0,20000,10)
yaw = PWM.Servo(0,20000,10)
#aux = PWM.Servo()
# start PWM on servo specific GPIO no, this is not the pin no but it is the GPIO no 
roll.set_servo(5,1520)# pin 29
pitch.set_servo(6,1520)# pin 31
throttle.set_servo(13,1100)# pin 33
yaw.set_servo(19,1520)# pin 35
print("Sleeping 15")
#sleep(20)
def disarm_with_self_level_on():
    roll.set_servo(5,1900)  ## hold  aileron to right when arming or disarm$
    throttle.set_servo(13,1150) # set to zero
    yaw.set_servo(19,1100)
    roll.set_servo(5,1520)  

x = input ("Are you ready: ")
#try: 
while True:
       disarm_with_self_level_on()
       x = int(input("CHECK THROTTLE: "))
       throttle.set_servo(13,x)
#except:
    throttle.stop_servo(13)
    yaw.stop_servo(19)
    pitch.stop_servo(6)
    roll.stop_servo(5)
PWM.cleanup()       

