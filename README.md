# Auditory experiment
This code conforms a Python application to run a stimuli-response based experiment. It is intended to have a folder inside root with the stimuli samples. Beware not to change files structure as it may cause damage in the script.
## 1.- Adapt the experiment.py files
The experiment code has its features set as they were used. To change any feature, one just has to open the experiment.py in a text editor and change strings needed.
### Sociological inquiry
Find sociology() function and edit, add or delete any more data needed for the new run. Be careful to update the outputGen() inputs as it takes sociology variables to note the down in the experiment output files.
### Levels to evaluate
Tipically, you would want your own assesment levels to show in the run. One just has to find levelsGen() function and insert as many levels as needed. Note that each level should be one entry in the array "levels" to keep working - the display uses len function to calculate how many lines levels will take so a mistake in the structure of levels array may cause damages in the execution of the script.
### Stimuli folder
The application is intended to contain the samples inside a folder child to the root. Default folder is assumed to be named "samples". If your folder is named otherwise, you want to change "path" variable from ".\\samples" to ".\\<name>", being <name> whatever name your folder has been given.
## 2.- Output
This experiment is anonymous. It generates a random numeric id for every participant. As outputGen() functions shows, the application produces two files - one file with the judgements delivered by the participant and another one with the sociological data. This can be changed modifying outputGen() function. Again, be aware to study returns and inputs to other functions.