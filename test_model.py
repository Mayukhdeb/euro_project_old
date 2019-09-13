# test_model.py



import numpy as np

from grabscreen import grab_screen

import cv2

import time

from directkeys import PressKey,ReleaseKey, W, A, S, D

from alexnet import alexnet

from getkeys import key_check



import random



WIDTH = 320

HEIGHT = 240

LR = 1e-3

EPOCHS = 40

MODEL_NAME = 'pygta5-car-fast-{}-{}-{}-epochs-300K-data.model'.format(LR, 'alexnetv2',EPOCHS)



t_time = 0.35



def straight():

##    if random.randrange(4) == 2:

##        ReleaseKey(W)

##    else:

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

    for i in list(range(20))[::-1]:

        print(i+1)

        time.sleep(1)



    paused = False

    while(True):

        

        if not paused:

            # 800x600 windowed mode

            #screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))

            screen = grab_screen(region=(560,240,1360,840))
      

            ##print('loop took {} seconds'.format(time.time()-last_time))

            last_time = time.time()

            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            
            screen = cv2.resize(screen, (320, 240))

          
            



            prediction = model.predict([screen.reshape(320,240,1)])[0]

           
            print ("")



            turn_thresh = .75

            fwd_thresh = 0.80



            if prediction[1] > fwd_thresh:

                straight()

            elif prediction[0] > turn_thresh:

                left(prediction[0])

            elif prediction[2] > turn_thresh:

                right(prediction[2])

            else:

                straight()



        keys = key_check()



        # p pauses game and can get annoying.

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



















