# euro_project_old

README / explanation ---------------------

Python 3.5

step 1 - create_training_data.py

step 2 - balance_data.py

step 3 - train_model.py

step 4 - test_model.py



---------------------------

create_training_data.py

>> takes in and stores training data for the neural network

>> takes an 800 * 600 screenshot in a region specified by co-ordinates

>> converts the screen to grayscale

	now grayscale has 256 possible values -- (256 shades of grey to be precise)

>> this grayscale image is then converted to an array which 
   contains the "numerical values of grey"

>> this huge 800*600 matrix is then resized to (320 * 240), because my laptop cannot
   handle such a large amount of data

>> while the screenshot is taken, the key pressed on the keyboard is also registered in another array simultaneously

	[0,1,0] for W (straight)
	
	[1,0,0] for A (left)

	[0,0,1] for D (right)

>> the large 320*240 array is then paired up with the [ , , ] array  (see attached image 1 )

>> the pairs are then appended to one final array (training_data.npy) and saved after every 1000 frames are taken. 



----------------------------

balance_data.py

>> makes sure the training data has an equal number of "lefts", "rights", an "straights"

>> this makes sure there are no biases in the final model due to the presence of too many 
   straights as compared to lefts or rights

>> it also shuffles the data


-----------------------------

train_model.py


>> I really dont know much about how it works from it's core, line by line

		but I know how to tweak a few of the parameters

>> it's based on "alexnet" made by a russian guy back in 2012

>> alexnet is a flexible CNN which I used for my "image sorting model"

>>  EPOCHS = the number of cycles/ number of times the neural network will go through the complete 
    training data to train itself. 

>> LR = learning rate

>> there is also a "validation set" of 200 frames on which the neural network tests itself after every epoch



--------------------------------

test_model.py


>> this program "drives" the truck 





>>>>      input as 800*600 frame and resize and convert  to 320*240 array

>>>>      array is then fed to the model (euro_self.model which was generated after training) 

>>>>      The model then returns an output like  [ 0.85,   0.11,   0.03]

>>>>      the largest value of the three is chosen as the input



>>>>      [ 0.8,   0.2,   0.1]  --- wants to go left
             ^
             |




>>>>      [ 0.01,   0.4,   0.9]  ---- wants to go right 

                            ^
                            |



>>>>      [ 0.2,   0.8,   0.3]    --- wants to go straight

                    ^
                    |


>>>> But to make the driving less erratic, there is a
     threshold value for turning and straight

>>>> if all the values are below threshold,  it will just press "W" 
      and keep moving forward 


>>>> the amount of time the keys for turning are pressed is a
     function of the value returned for (say) left


>>>>    [ 0.93,   0.2,   0.1]  will press "A" (left) for longer
           ^
           |
       


        than

        [ 0.75,   0.2,   0.1]  
           ^
           |


        because 0.93 > 0.75


------------------------------------------------------------------



Some of the errors/mistakes which I learned from

>> error 1 :  biased neural network because of too many "forward" 
   frames in training data

>>  fix = balance_training_data.py -- makes sure there is an equal number of all the three types of frames 





>> error 2 : the truck the straightens itself on the road and presses nothing after that

>> fix = added an else statement which makes python press W if all the values in the output matrix [ x , y , z] are below threshold





>> error 3 =  python was pressing the keys for a very short period of time for turns and straights

              and the time for which the key was pressed was the same for both sharp and smooth turns


>> fix = modified test-model.py so that the amount of time the turning keys (A or D) is pressed is a direct function of the value returned in the output array [  ,   ,  ]






-----------------------------------------------------------------------------------------------------------------------------


improvements I will work on 

-- RGB input

-- joystick input by python for smoother steering

-- vehicle detection and avoiding 

-- larger and a higher resolution training dataset (maybe use the original 800*600 matrix)

-- use a better neural network model, something better than alexnet maybe 
	 




*******************************************************************************************************************************







