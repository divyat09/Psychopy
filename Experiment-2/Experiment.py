from psychopy import visual, core, event
import numpy as np
import json
import random
import time

# Funcion to simulate the experiment

def Experiment_Run( ExpType, TrialInput ):

    mywin= visual.Window([1000,800],monitor="testMonitor", units="deg", color = (1,1,1), fullscr = True)

    image_CO = visual.ImageStim(win=mywin, image="1.jpg")
    image_SO = visual.ImageStim(win=mywin, image="2.jpg")
    image_SX = visual.ImageStim(win=mywin, image="3.jpg")
    image_CX = visual.ImageStim(win=mywin, image="4.jpg")

    TotalIter = 1050

    if ExpType == 1:
        delay = np.random.normal( 1, 0, size = TotalIter + 1 )

    elif ExpType == 2:
        delay = np.random.normal( 1, 0.1, size = TotalIter + 1 )

    elif ExpType == 3:
        delay = np.random.normal( 1, 0.3, size = TotalIter + 1 )

    if TrialInput == 1:                        # Global Level Change
        Trial = "Global_Level"
        PrefferedStimuli  = image_CX
        NonPrefferedStimul = image_SX

    elif TrialInput == 2:                      # Local Level Change
        Trial = "Local_Level"
        PrefferedStimuli  = image_SO
        NonPrefferedStimul = image_SX

    # Keeping in Append Mode
    f = open("Info"+"_Id_" +str(Id) + ".txt","a")
    f.write(" Trial: %s,\n" % Trial  )
    f.close()

    core.wait(10)

    Iter = 0
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

            while( clock.getTime() - PrefStimuliStart <= delay[Iter] ):
                if len(event.getKeys()) > 0:
                    event.clearEvents()
                    CurrentTime = clock.getTime()

                    Result = {}
                    Result["ResultTime"] = CurrentTime
                    Result["ReactionTime"] = CurrentTime - StartTime
                    Result["Stimuli"] = valid

                    Final_Result.append( Result )
                    StartTime = clock.getTime()

            #print clock.getTime() - PrefStimuliStart
            Iter = Iter + 1
            #print Iter

    mywin.close()
    f = open("Results_"+Trial+".json","w")
    f.write( json.dumps(Final_Result, indent = 3 ))
    f.close()

#Storing the ID of the participant
Id = 1

# Experiment Case: 1 denotes the Constant Delay Case
#                  2 denotes the Delay N(1000,100) Case
#                  3 denotes the Delay N(1000,300) Case

ExpType = 1

# Trail Case:
Input = np.random.permutation([1,2])

# Run the First Trial
if raw_input("Start the Trial: "):
    Experiment_Run( ExpType ,Input[0] )
# Just make sure the experiment is Run, even when one by mistake presses Enter Key for raw input
else:
    Experiment_Run( ExpType ,Input[0] )

time.sleep(300)

# Run the Second Trial
if raw_input("Start the Next Trial: "):
    Experiment_Run( ExpType ,Input[1] )
# Just make sure the experiment is Run, even when one by mistake presses Enter Key for raw input
else:
    Experiment_Run( ExpType ,Input[1] )
