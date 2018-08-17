from RPIO import PWM
from time import sleep

roll = PWM.Servo(0,20000,5)
pitch = PWM.Servo(0,20000,5)
throttle = PWM.Servo(0,20000,5)
yaw = PWM.Servo(0,20000,5)

roll.set_servo(5,1500)# pin 29
pitch.set_servo(6,1500)# pin 31
throttle.set_servo(13,1150)# pin 33
yaw.set_servo(19,1505)# pin 35

min_throttle = 1150
middle_throttle = 1500  
max_throttle = 1850
min_yaw = 1100  #max right
middle_yaw = 1505
max_yaw =1900 #max left
min_pitch = 1110    #forward
middle_pitch = 1500
max_pitch = 1880    #backward
min_roll = 1100 #left
middle_roll = 1500 
max_roll = 1900 #right

th = 1700
ya = middle_yaw
pi = middle_pitch
ro = middle_roll
def trim():
    roll.set_servo(5,middle_roll)
    pitch.set_servo(6,middle_pitch)
    throttle.set_servo(13,min_throttle)
    yaw.set_servo(19,middle_yaw)
    print("Trim!!!!!")



def arm_with_self_level_on():
    roll.set_servo(5,max_roll)  ## hold  aileron to right when arming or disarming.
    sleep(1)
    throttle.set_servo(13,min_throttle)  #set to zero
    yaw.set_servo(19,min_yaw)  # set to max  (full right yaw)
    ## others to minimum
    print ("SElf level on!!!")
    print ("Display Armed!!!!")



while True:
        x = input("Please check for error in KK2.1.5 if any!! Remove them: press arm:  ")
        if x=="arm":
           print("Arming")
           arm_with_self_level_on()
        else:
           print("Fool you have to print con!!!.")
           break
        print("\nReady for flying!!!")
        y = input("Are you ready: yes/no:")
        if(y=="yes"):
           sleep(1)
           print("Control")
        else:
           break

        while True: 
                 z = input("Enter value: ")
                 # Throttle up
                 if z == 'w':
                     th = th + 10
                     if (th < min_throttle):
                        throttle.set_servo(13,min_throttle)
                        th = min_throttle
                     elif (th > max_throttle):
                        throttle.set_servo(13,max_throttle)
                        th = max_throttle
                     elif (th > min_throttle & th < max_throttle):
                        throttle.set_servo(13,th)
                     print ("TH: ") + str(th)
                     continue
                 # Throttle down
                 if z == 's':
                    th = th - 10
                    if (th < min_throttle):
                        throttle.set_servo(13,min_throttle)
                        th = min_throttle
                    elif (th > max_throttle):
                        throttle.set_servo(13,max_throttle)
                        th = max_throttle
                    elif (th > min_throttle & th < max_throttle):
                        throttle.set_servo(13,th)
                    print ("TH: ") + str(th)
                    continue
                 
                 # yaw left (positive values)
                 if z == 'a':
                    ya = ya + 10
                    if (ya < min_yaw):
                        yaw.set_servo(19,min_yaw)
                        ya = min_yaw
                    elif (ya > max_yaw):
                        yaw.set_servo(19,max_yaw)
                        ya = max_yaw
                    elif (ya > min_yaw & ya < max_yaw):
                           yaw.set_servo(19,ya)
                    print ("YA: ") + str(ya)
                    continue
		# yaw right (negative values)
                 if z == 'd':
                    ya = ya - 10
                    if (ya < min_yaw):
                        yaw.set_servo(19,min_yaw)
                        ya = min_yaw
                    elif (ya > max_yaw):
                        yaw.set_servo(19,max_yaw)
                        ya = max_yaw
                    elif (ya > min_yaw & ya < max_yaw):
                           yaw.set_servo(19,ya)
                    print ("YA: ") + str(ya)
                    continue

	         # mapping PI = UP
                 if z == '8':
                    pi = pi + 10
                    if (pi < min_pitch):
                         pitch.set_servo(6,min_pitch)
                         pi = min_pitch
                    elif (pi > max_pitch):
                         pitch.set_servo(6,max_pitch)
                         pi = max_pitch
                    elif (pi > min_pitch & pi < max_pitch):
                         pitch.set_servo(6,pi)
                    print ("PI: ") + str(pi)
                    continue
            
                 # mapping PI = DOWN
                 if z == '2':
                    pi = pi - 10
                    if (pi < min_pitch):
                       pitch.set_servo(6,min_pitch)
                       pi = min_pitch
                    elif (pi > max_pitch):
                       pitch.set_servo(6,max_pitch)
                       pi = max_pitch
                    elif (pi > min_pitch & pi < max_pitch):
                       pitch.set_servo(6,pi)
                    print ("PI: ") + str(pi)
                    continue
                   
                    # mapping RO = LEFT
                 if z == '4':
                       ro = ro - 10
                       if (ro < min_roll):
                          roll.set_servo(5,min_roll)
                          ro = min_roll
                       elif (ro > max_roll):
                          roll.set_servo(5,max_roll)
                          ro = 1900
                       elif (ro > min_roll & ro < max_roll):
                          roll.set_servo(5,ro)
                       print ("RO: ") + str(ro)
                       continue
                   
                    # mapping RO = RIGHT
                 if z == '6':
                       ro = ro + 10
                       if (ro < min_roll):
                          roll.set_servo(5,min_roll)
                          ro = min_roll
                       elif (ro > max_roll):
                          roll.set_servo(5,max_roll)
                          ro = max_roll
                       elif (ro > min_roll & ro < max_roll):
                          roll.set_servo(5,ro)
                       print ("RO: ") + str(ro)
                       continue
                     
                    # break
                 if z == -1: 
                       break

   #     except: 
   #        pass
                 
#except:        
#   pass



yaw.stop_servo(19)
roll.stop_servo(5)
pitch.stop_servo(6)
throttle.stop_servo(13)
PWM.cleanup()       

