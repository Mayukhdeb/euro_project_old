# create_training_data.py

## game on  center of screen 800 x 600 windowed

##works best with cockpit view





import numpy as np

from grabscreen import grab_screen

import cv2

import time

from getkeys import key_check   #extracts keypresses by user

import os





def keys_to_output(keys):

    '''

    Convert keys to a ...multi-hot... array



    [A,W,D] boolean values.

    '''

    output = [0,0,0]

    

    if 'A' in keys:           # left is taken as [1,0,0]


        output[0] = 1

    elif 'D' in keys:            # right is taken as [0,0,1]

        output[2] = 1

    else:

        output[1] = 1                  # forwards for [0,1,0]

    return output





file_name = 'training_data.npy'



if os.path.isfile(file_name):

    print('File exists, loading previous data!')

    training_data = list(np.load(file_name))

else:

    print('File does not exist, starting fresh!')

    training_data = []





def main():



    for i in list(range(10))[::-1]:                # timer for me to remove all other windows from the region from where python will capture the screenshots

        print(i+1)

        time.sleep(1)





    paused = False

    while(True):

        


        if not paused:

            # 800x600 windowed mode
            

            screen = grab_screen(region=(560,240,1360,840))                   #screenshot

            last_time = time.time()

            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)    #convert to grayscale

            screen = cv2.resize(screen, (320,240))

            # resize to something a bit more acceptable for a CNN

            keys = key_check()

            output = keys_to_output(keys)

            training_data.append([screen,output])   #pairs matrix form of grayscale screenshot with [0,1,0] or [1,0,0] od [0,0,1]

            

            if len(training_data) % 1000 == 0:

                print(len(training_data))
                

                np.save(file_name,training_data)
                print ("saved current chunk")



        keys = key_check()

        if 'T' in keys:         #press T to pause

            if paused:

                paused = False

                print('unpaused!')

                time.sleep(1)

            else:

                print('Paused, not recording')

                paused = True

                time.sleep(1)





main()
