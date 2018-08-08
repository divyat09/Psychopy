from psychopy import core, visual, event
from psychopy.tools.filetools import fromFile, toFile
import numpy, random

#create a window
mywin = visual.Window([800,600],monitor="testMonitor", units="deg")

#create some stimuli
grating = visual.GratingStim(win=mywin, mask='circle', size=3, pos=[-4,0], sf=3)
fixation = visual.GratingStim(win=mywin, size=0.2, pos=[0,0], sf=0, rgb=-1)

#draw the stimuli and update the window
while True: #this creates a never-ending loop
    grating.setPhase(0.05, '+')#advance phase by 0.05 of a cycle
    grating.draw()
    fixation.draw()
    mywin.flip()

    # Break the experiment on the pressing of any key
    if len(event.getKeys())>0:
        break
    event.clearEvents()

#cleanup
mywin.close()

#create a new window
mywin = visual.Window([800,600],monitor="testMonitor", units="deg")

# Radius for the circle
count = 0

while True: #this creates a never-ending loop

    if count >15:
        break

    # Increase the size of the circle on the pressing of any key
    if len(event.getKeys())>0:
        count = count + 0.5

    event.clearEvents()

    # Create a circle with Radius as count
    grating = visual.GratingStim(win=mywin, mask='circle', size=count, pos=[0,0], sf=3)
    grating.draw()
    mywin.update()

core.quit()
