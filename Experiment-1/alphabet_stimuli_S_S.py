from psychopy import core, visual, event
import numpy, random

def Draw_SS(mywin):

    start_x = -2.0
    start_y = -6.0
    mid = 1.0           # Breadth of a single block of H
    end = 2.0           # Height of a single block of H
    gap_y = end + 0.5   # Gap in y-axis between two consecutive blocks of H
    gap_x = mid + 0.5   # Gap in x-axis between two consecutive blocks of H

    # Specifying the block number of S
    x = start_x + 2*gap_x
    y = start_y + 4*gap_y
    V1 = ( (x+mid, y + end), (x, y + end), ( x, y + mid ), (x +mid, y + mid), (x + mid, y), (x, y ), (x + mid, y), (x +mid, y + mid), (x, y + mid), (x, y + end)  )
    # Constructing S for that particular block
    S1 = visual.ShapeStim(win= mywin, vertices= V1 )

    x = start_x + gap_x
    y = start_y + 4*gap_y
    # Constructing S for that particular block
    V2 = ( (x+mid, y + end), (x, y + end), ( x, y + mid ), (x +mid, y + mid), (x + mid, y), (x, y ), (x + mid, y), (x +mid, y + mid), (x, y + mid), (x, y + end)  )
    S2 = visual.ShapeStim(win= mywin, vertices= V2 )

    x = start_x
    y = start_y + 4*gap_y
    # Constructing S for that particular block
    V3 = ( (x+mid, y + end), (x, y + end), ( x, y + mid ), (x +mid, y + mid), (x + mid, y), (x, y ), (x + mid, y), (x +mid, y + mid), (x, y + mid), (x, y + end)  )
    S3 = visual.ShapeStim(win= mywin, vertices= V3 )

    x = start_x
    y = start_y + 3*gap_y
    # Constructing S for that particular block
    V4 = ( (x+mid, y + end), (x, y + end), ( x, y + mid ), (x +mid, y + mid), (x + mid, y), (x, y ), (x + mid, y), (x +mid, y + mid), (x, y + mid), (x, y + end)  )
    S4 = visual.ShapeStim(win= mywin, vertices= V4 )

    x = start_x
    y = start_y + 2*gap_y
    # Constructing S for that particular block
    V5 = ( (x+mid, y + end), (x, y + end), ( x, y + mid ), (x +mid, y + mid), (x + mid, y), (x, y ), (x + mid, y), (x +mid, y + mid), (x, y + mid), (x, y + end)  )
    S5 = visual.ShapeStim(win= mywin, vertices= V5 )

    x = start_x + gap_x
    y = start_y + 2*gap_y
    # Constructing S for that particular block
    V6 = ( (x+mid, y + end), (x, y + end), ( x, y + mid ), (x +mid, y + mid), (x + mid, y), (x, y ), (x + mid, y), (x +mid, y + mid), (x, y + mid), (x, y + end)  )
    S6 = visual.ShapeStim(win= mywin, vertices= V6 )

    x = start_x + 2*gap_x
    y = start_y + 2*gap_y
    # Constructing S for that particular block
    V7 = ( (x+mid, y + end), (x, y + end), ( x, y + mid ), (x +mid, y + mid), (x + mid, y), (x, y ), (x + mid, y), (x +mid, y + mid), (x, y + mid), (x, y + end)  )
    S7 = visual.ShapeStim(win= mywin, vertices= V7 )

    x = start_x + 2*gap_x
    y = start_y + gap_y
    # Constructing S for that particular block
    V8 = ( (x+mid, y + end), (x, y + end), ( x, y + mid ), (x +mid, y + mid), (x + mid, y), (x, y ), (x + mid, y), (x +mid, y + mid), (x, y + mid), (x, y + end)  )
    S8 = visual.ShapeStim(win= mywin, vertices= V8 )

    x = start_x + 2*gap_x
    y = start_y
    # Constructing S for that particular block
    V9 = ( (x+mid, y + end), (x, y + end), ( x, y + mid ), (x +mid, y + mid), (x + mid, y), (x, y ), (x + mid, y), (x +mid, y + mid), (x, y + mid), (x, y + end)  )
    S9 = visual.ShapeStim(win= mywin, vertices= V9 )

    x = start_x + gap_x
    y = start_y
    # Constructing S for that particular block
    V10 = ( (x+mid, y + end), (x, y + end), ( x, y + mid ), (x +mid, y + mid), (x + mid, y), (x, y ), (x + mid, y), (x +mid, y + mid), (x, y + mid), (x, y + end)  )
    S10 = visual.ShapeStim(win= mywin, vertices= V10 )

    x = start_x
    y = start_y
    # Constructing S for that particular block
    V11 = ( (x+mid, y + end), (x, y + end), ( x, y + mid ), (x +mid, y + mid), (x + mid, y), (x, y ), (x + mid, y), (x +mid, y + mid), (x, y + mid), (x, y + end)  )
    S11 = visual.ShapeStim(win= mywin, vertices= V11 )


    S1.draw()
    S2.draw()
    S3.draw()
    S4.draw()
    S5.draw()
    S6.draw()
    S7.draw()
    S8.draw()
    S9.draw()
    S10.draw()
    S11.draw()

    mywin.flip()
