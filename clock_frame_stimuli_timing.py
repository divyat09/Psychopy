from psychopy import core, visual
import numpy, random

mywin = visual.Window([800,600],monitor="testMonitor", units="deg")

# Cannot use TextStim .... unable to i
#message1 = visual.TextStim(mywin, pos=[0,+3],text='Hit a key when ready.')
#message1.draw()

gabor = visual.GratingStim(win= mywin, mask='circle', size=3, pos=[-4,0], sf=3)
gabor.setAutoDraw(True)  # automatically draw every frame
gabor.autoLog=False      # or we'll get many messages about phase change

clock = core.Clock()

#let's draw a stimulus for 4s, drifting for middle 1.5s to 2.0s
while clock.getTime() < 4.0:  # clock times are in seconds
    if 1.5 <= clock.getTime() < 2.0:
        gabor.setPhase(0.1, '+')  # increment by 10th of cycle
    #gabor.draw()   # Dont need to draw it yourself everytime again
    mywin.flip()

####################################################
# Clocks are not completely accurate. Hence, better to work by specifying the number of frames
####################################################

#cleanup
mywin.close()

mywin = visual.Window([800,600],monitor="testMonitor", units="deg")
fabor = visual.GratingStim(win= mywin, mask='circle', size=3, pos=[-4,0], sf=3)
fabor.setAutoDraw(True)  # automatically draw every frame
fabor.autoLog=False      # or we'll get many messages about phase change

#draw a stimulus for 400 frames, drifting for frames 150:100
for frameN in range(1000):#for exactly 200 frames

    if 300 <= frameN < 600:  # present stim for a different subset
        fabor.setPhase(0.1, '+')  # increment by 10th of cycle
    mywin.flip()

core.quit()
