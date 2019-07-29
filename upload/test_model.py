# test_model.py



import numpy as np

from grabscreen import grab_screen

import cv2

import time

from directkeys import PressKey,ReleaseKey, W, A, S, D      

from alexnet import alexnet

from getkeys import key_check







WIDTH = 320

HEIGHT = 240

LR = 1e-3

EPOCHS = 40

MODEL_NAME = ('euro_self.model')



t_time = 0.35



def straight():




    PressKey(W)

    ReleaseKey(A)

    ReleaseKey(D)

    print ("---------     111111111     ---------")



def left(foo):

    PressKey(W)

    PressKey(A)

    #ReleaseKey(W)

    ReleaseKey(D)

    #ReleaseKey(A)

    time.sleep(t_time*foo)   

    ReleaseKey(A)

    print ("111111111     ---------     ---------")



def right(foo):

    PressKey(W)

    PressKey(D)

    ReleaseKey(A)

    #ReleaseKey(W)

    #ReleaseKey(D)

    time.sleep(t_time*foo)

    ReleaseKey(D)

    print ("---------     ---------     111111111")

    

model = alexnet(WIDTH, HEIGHT, LR)

model.load(MODEL_NAME)



def main():

    last_time = time.time()

    for i in list(range(10))[::-1]:

        print(i+1)

        time.sleep(1)



    paused = False

    while(True):

        

        if not paused:

            # 800x600 windowed mode

            

            screen = grab_screen(region=(560,240,1360,840))
      

            

            last_time = time.time()

            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            
            screen = cv2.resize(screen, (320, 240))

          
            



            prediction = model.predict([screen.reshape(320,240,1)])[0]    #returns [ , , ,] array for output

           
            print ("")



            turn_thresh = .75      #minimum value over which the key will be pressed

            fwd_thresh = 0.80



            if prediction[1] > fwd_thresh:       #logic for output

                straight()

            elif prediction[0] > turn_thresh:

                left(prediction[0])

            elif prediction[2] > turn_thresh:

                right(prediction[2])

            else:

                straight()



        keys = key_check()   #detect what key is pressed



        # t pauses the game

        if 'T' in keys:

            if paused:

                paused = False

                time.sleep(1)
                

            else:

                paused = True
                print ("paused")

                ReleaseKey(A)

                ReleaseKey(W)

                ReleaseKey(D)

                time.sleep(1)



main()       



















