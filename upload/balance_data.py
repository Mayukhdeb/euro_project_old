# balance_data.py


# makes sure that there are an equal number of forwards, lefts and rights to train with




import numpy as np

import pandas as pd

from collections import Counter

from random import shuffle



train_data = np.load('training_data.npy')



df = pd.DataFrame(train_data)


print(Counter(df[1].apply(str)))



lefts = []

rights = []

forwards = []



shuffle(train_data)       



for data in train_data:

    img = data[0]

    choice = data[1]

   

    if choice == [1,0,0]:

        lefts.append([img,choice])

    elif choice == [0,1,0]:

        forwards.append([img,choice])

    elif choice == [0,0,1]:

        rights.append([img,choice])

    else:

        print('no matches')





forwards = forwards[:len(lefts)][:len(rights)]

lefts = lefts[:len(forwards)]

rights = rights[:len(forwards)]



final_data = forwards + lefts + rights    #this time it has an equal number of forwards, lefts and rights 


print ("shuffling")
shuffle(final_data)



np.save('training_data.npy', final_data)



print ("saved!!!")







