from psychopy import visual, core, event
import numpy as np
import json
import random

mywin = visual.Window([1000,800],monitor="testMonitor", units="deg", color = (1,1,1), fullscr = True)
image_CO = visual.ImageStim(win=mywin, image="1.jpg")
image_SO = visual.ImageStim(win=mywin, image="2.jpg")
image_SX = visual.ImageStim(win=mywin, image="3.jpg")
image_CX = visual.ImageStim(win=mywin, image="4.jpg")

# Experiment Case:
Input = np.random.permutation([1,2])[0]

#Storing the ID
Id = 1

if Input == 1:                        # Global Level Change
    Case = "Global_Level"
    PrefferedStimuli  = image_CX
    NonPrefferedStimul = image_SX

elif Input == 2:                      # Local Level Change
    Case = "Local_Level"
    PrefferedStimuli  = image_SO
    NonPrefferedStimul = image_SX

# Keeping in Append Mode
f = open("Info"+"_Id_" +str(Id) + ".txt","a")
f.write("Case: %s,\n" % Case  )
f.close()

# Draw a stimulus for 4s, drifting for middle 1.5s to 2.0s
# User has to press a key as soon as the phase shift appears
core.wait(10)

TotalIter = 1050
Iter = 0
delay = 1.0
Final_Result = []
valid = 0
clock = core.Clock()

while( Iter <= TotalIter ):

    if valid == 0:
        StartTime = clock.getTime()

    NonPrefferedStimul.draw()
    mywin.update()
    valid  = 1

    if len(event.getKeys())>0:

        event.clearEvents()
        CurrentTime = clock.getTime()

        Result = {}
        Result["ResultTime"] = CurrentTime
        Result["ReactionTime"] = CurrentTime - StartTime
        Result["Stimuli"] = valid

        Final_Result.append( Result )
        StartTime = clock.getTime()

        PrefferedStimuli.draw()
        mywin.update()
        valid = 0

        PrefStimuliStart = clock.getTime()

        while( clock.getTime() - PrefStimuliStart <= delay ):
            if len(event.getKeys()) > 0:
                event.clearEvents()
                CurrentTime = clock.getTime()

                Result = {}
                Result["ResultTime"] = CurrentTime
                Result["ReactionTime"] = CurrentTime - StartTime
                Result["Stimuli"] = valid

                Final_Result.append( Result )
                StartTime = clock.getTime()

        print clock.getTime() - PrefStimuliStart
        Iter = Iter + 1
        print Iter

f = open("Results_"+Case+".json","w")
f.write( json.dumps(Final_Result, indent = 3 ))
f.close()

core.quit()


