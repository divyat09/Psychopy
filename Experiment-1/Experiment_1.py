from psychopy import core, visual, event
import numpy as np
import random
from alphabet_stimuli_H_H import Draw_HH
from alphabet_stimuli_H_S import Draw_HS
from alphabet_stimuli_H_X import Draw_HX
from alphabet_stimuli_S_S import Draw_SS
from alphabet_stimuli_S_H import Draw_SH
from alphabet_stimuli_S_X import Draw_SX

result1 = []
result2 = []

mywin = visual.Window([800,600],monitor="testMonitor", units="deg")

clock = core.Clock()
off = 1
start_time = 0.5

# Draw a stimulus for 4s, drifting for middle 1.5s to 2.0s
# User has to press a key as soon as the phase shift appears

while clock.getTime() <= 20.0:  # clock times are in seconds

    # Measuring the reaction time of User to determine when the phase change starts to happen.
    # Calcualte the difference between current given time and 1.5( time when the Phase Shift started to happen )
    if len(event.getKeys())>0 and  clock.getTime() - start_time > 0 :
        result1.append( clock.getTime() - start_time )
        off = 0

    event.clearEvents()

    if clock.getTime() - start_time >= 0.5:
        start_time = clock.getTime() + 0.5
        off = 1

    if 0 <= clock.getTime() - start_time < 0.5 and off == 1:
        Draw_SS(mywin)
        continue

    Draw_HH(mywin)

####################################################
# Clocks are not completely accurate. Hence, better to work by specifying the number of frames
####################################################

print "Case 1 Results:\n"
for item in result1:
    print item

print "Total valid response cases: ",
print len(result1)
print "Average Response Time: ",
print np.mean(np.array(result1))

#cleanup
mywin.close()
core.wait(3)

clock_new = core.Clock()

mywin = visual.Window([800,600],monitor="testMonitor", units="deg")
fabor = visual.GratingStim(win= mywin, mask='circle', size=3, pos=[-4,0], sf=3)
tabor = visual.GratingStim(win= mywin, mask='circle', size=3, pos=[0,0], sf=3)

'''
fabor.setAutoDraw(True)  # automatically draw every frame
fabor.autoLog=False      # or we'll get many messages about phase change
'''

off = 1
sub_frameN = 0

# Stimulus drawn for 10000 frames. At the 500th frame, a new circle get added and stays there for next 500 frames
# and then goes off.
# New circle addition keeps repeating after every 1000 frames.
# Hence, in the later half part( i.e 500-1000 ) of every 1000 frames you get addition of a new stimulus
# User's task is to press a key as soon as the new stimulus gets added

for frameN in range(10000):#for exactly 200 frames

    # Measuring the reaction time of User to determine when the phase change starts to happen.
    # Calculate the difference between current given time and time_start( time when  set Phase started to happen )
    if len(event.getKeys())>0 and clock_new.getTime() > time_start :
        #print "Reaction Time for Case 2: "
        #print clock_new.getTime() - time_start
        result2.append( clock_new.getTime() - time_start )

        off = 0

    event.clearEvents()

    # Restarting the sub counter so that it keeps repeating values between 0 to 1000
    if sub_frameN ==1000 :
        sub_frameN = 0
        off = 1

    if 500 <= sub_frameN < 1000 and off == 1:  # present stim for a different subset
        if sub_frameN == 500:
            time_start = clock_new.getTime()

        Draw_SS(mywin)
        sub_frameN = sub_frameN + 1
        continue

    Draw_HH(mywin)
    sub_frameN = sub_frameN + 1

print "Case 2 Results:\n"
for item in result2:
    print item

print "Total valid response cases: ",
print len(result2)
print "Average Response Time: ",
print np.mean(np.array(result2))

core.quit()
