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
   need a more efficient input method for that 

-- use a better neural network model, something better than alexnet maybe 
	 




*******************************************************************************************************************************

pip list  

Package                  Version
------------------------ --------
absl-py                  0.6.1
astor                    0.7.1
attrs                    19.1.0
backcall                 0.1.0
bleach                   3.1.0
cachetools               3.1.0
colorama                 0.4.1
cycler                   0.10.0
decorator                4.4.0
defusedxml               0.6.0
docutils                 0.14
entrypoints              0.3
gast                     0.2.0
google-api-python-client 1.7.8
google-auth              1.6.2
google-auth-httplib2     0.0.3
grpcio                   1.16.1
h5py                     2.8.0
httplib2                 0.12.0
inputs                   0.5
ipykernel                5.1.1
ipython                  7.6.1
ipython-genutils         0.2.0
jedi                     0.14.1
Jinja2                   2.10.1
jsonschema               3.0.1
jupyter-client           5.3.1
jupyter-core             4.5.0
jupyterthemes            0.20.0
Keras                    2.2.4
Keras-Applications       1.0.6
Keras-Preprocessing      1.0.5
kiwisolver               1.0.1
lesscpy                  0.13.0
Markdown                 3.0.1
MarkupSafe               1.1.1
matplotlib               3.0.2
mistune                  0.8.4
nbconvert                5.5.0
nbformat                 4.4.0
notebook                 6.0.0
numpy                    1.15.4
oauth2client             4.1.3
opencv-python            3.4.4.19
pandas                   0.23.4
pandocfilters            1.4.2
parso                    0.5.1
pickleshare              0.7.5
Pillow                   5.3.0
pip                      18.1
ply                      3.11
prometheus-client        0.7.1
prompt-toolkit           2.0.9
protobuf                 3.6.1
pyasn1                   0.4.5
pyasn1-modules           0.2.4
PyAutoGUI                0.9.38
PyDrive                  1.3.1
Pygments                 2.4.2
PyMsgBox                 1.0.6
pyparsing                2.3.0
pyrsistent               0.15.3
PyScreeze                0.1.18
python-dateutil          2.7.5
PyTweening               1.0.3
pytz                     2018.7
pywin32                  224
pywinpty                 0.5.5
PyYAML                   3.13
pyzmq                    18.0.2
rsa                      4.0
scikit-learn             0.20.1
scipy                    1.1.0
Send2Trash               1.5.0
setuptools               41.0.1
six                      1.11.0
sklearn                  0.0
statistics               1.0.3.5
tensorboard              1.12.0
tensorflow               1.12.0
termcolor                1.1.0
terminado                0.8.2
testpath                 0.4.2
tflearn                  0.3.2
tornado                  6.0.3
traitlets                4.3.2
uritemplate              3.0.0
wcwidth                  0.1.7
webencodings             0.5.1
Werkzeug                 0.14.1
wheel                    0.32.3
win-unicode-console      0.5
windows-curses           1.0
		





