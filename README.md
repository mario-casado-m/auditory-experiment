# Auditory experiment
This code conforms a Python application to run a stimuli-response based experiment. It is intended to have a folder inside root with the stimuli samples. Beware not to change files structure as it may cause damage in the script.
## 0.- Structure
It has two phases - firstly, it asks some sociological data to the participants. Secondly, there is the very experiment. In the experiment, each participant will hear successive sample audios. Only after the sound is fully played, a new screen will appear with the transcription of the sentence and the scale from 0 to 5, where zero intends to play the audio once again. Input function will listen keyboard numbers. Audio repeat is limited to two times. After the second play, 0 option will disappear and only input from 1 to 5 will be allowed. Each audio sample in the stimuli folder will be used twice to check answers consistency. Once all the audios have been played, end screen will remind participants that they are suppose to zip the output folder and send it to some email address.  
## 1.- Adapt the experiment.py files
The experiment code has its features set as they were used. To change any feature, one just has to open the experiment.py in a text editor and change strings needed.
### Sociological inquiry
Find sociology() function and edit, add or delete any more data needed for the new run. Be careful to update the outputGen() inputs as it takes sociology variables to note the down in the experiment output files.
### Levels to evaluate
Tipically, you would want your own assesment levels to show in the run. One just has to find levelsGen() function and insert as many levels as needed. Note that each level should be one entry in the array "levels" to keep working - the display uses len function to calculate how many lines levels will take so a mistake in the structure of levels array may cause damages in the execution of the script.
### Stimuli folder
The application is intended to contain the samples inside a folder child to the root. Default folder is assumed to be named "samples". If your folder is named otherwise, you want to change "path" variable from ".\\samples" to ".\\<name>", being <name> whatever name your folder has been given.
### Repetion
One can customize how many times each sample is used in the audio_csv_read() function. Check how each sound is appended twice at the end of the function. If you want to use the audios only once, just delete the second append. If you want to use them more times, just add more lines with append.
  Repeat constraint can also be customize so participants can hear each sample more than twice. Check the inquiry() function. Lines "if listenTime < 2" and "elif == 2" set the limit. One can alter these to lines at will.
## 2.- Output
This experiment is anonymous. It generates a random numeric id for every participant. As outputGen() functions shows, the application produces two files - one file with the judgements delivered by the participant and another one with the sociological data. This can be changed modifying outputGen() function. Again, be aware to study returns and inputs to other functions.
## 3.- Modifications & Feedback
Anyone who wants to use this script as the base to customize other experiment and make changes over it is encouraged to do so. Also, feedback is welcome as issues, pull requests, etc.
