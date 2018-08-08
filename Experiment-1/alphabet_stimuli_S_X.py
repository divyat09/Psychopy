from psychopy import core, visual, event
import numpy, random

def Draw_SX():

    start_x = -2.0
    start_y = -6.0
    mid = 1.0           # Breadth of a single block of H
    end = 2.0           # Height of a single block of H
    gap_y = end + 0.5   # Gap in y-axis between two consecutive blocks of H
    gap_x = mid + 0.5   # Gap in x-axis between two consecutive blocks of H

    # Specifying the block number of H
    x = start_x + 2*gap_x
    y = start_y + 4*gap_y
    V1 = ( (x+mid, y + end), (x,y) )
    # Constructing S for that particular block
    S1 = visual.ShapeStim(win= mywin, vertices= V1 )

    x = start_x + gap_x
    y = start_y + 4*gap_y
    # Constructing H for that particular block
    V2 = ( (x+mid, y + end), (x,y) )
    S2 = visual.ShapeStim(win= mywin, vertices= V2 )

    x = start_x
    y = start_y + 4*gap_y
    # Constructing H for that particular block
    V3 = ( (x+mid, y + end), (x,y) )
    S3 = visual.ShapeStim(win= mywin, vertices= V3 )

    x = start_x
    y = start_y + 3*gap_y
    # Constructing H for that particular block
    V4 = ( (x+mid, y + end), (x,y) )
    S4 = visual.ShapeStim(win= mywin, vertices= V4 )

    x = start_x
    y = start_y + 2*gap_y
    # Constructing H for that particular block
    V5 = ( (x+mid, y + end), (x,y) )
    S5 = visual.ShapeStim(win= mywin, vertices= V5 )

    x = start_x + gap_x
    y = start_y + 2*gap_y
    # Constructing H for that particular block
    V6 = ( (x+mid, y + end), (x,y) )
    S6 = visual.ShapeStim(win= mywin, vertices= V6 )

    x = start_x + 2*gap_x
    y = start_y + 2*gap_y
    # Constructing H for that particular block
    V7 = ( (x+mid, y + end), (x,y) )
    S7 = visual.ShapeStim(win= mywin, vertices= V7 )

    x = start_x + 2*gap_x
    y = start_y + gap_y
    # Constructing H for that particular block
    V8 = ( (x+mid, y + end), (x,y) )
    S8 = visual.ShapeStim(win= mywin, vertices= V8 )

    x = start_x + 2*gap_x
    y = start_y
    # Constructing H for that particular block
    V9 = ( (x+mid, y + end), (x,y) )
    S9 = visual.ShapeStim(win= mywin, vertices= V9 )

    x = start_x + gap_x
    y = start_y
    # Constructing H for that particular block
    V10 = ( (x+mid, y + end), (x,y) )
    S10 = visual.ShapeStim(win= mywin, vertices= V10 )

    x = start_x
    y = start_y
    # Constructing H for that particular block
    V11 = ( (x+mid, y + end), (x,y) )
    S11 = visual.ShapeStim(win= mywin, vertices= V11 )

    # Specifying the block number of H
    x = start_x + 2*gap_x
    y = start_y + 4*gap_y
    V12 = ( (x, y + end), (x+mid,y) )
    # Constructing S for that particular block
    S12 = visual.ShapeStim(win= mywin, vertices= V12 )

    x = start_x + gap_x
    y = start_y + 4*gap_y
    # Constructing H for that particular block
    V13 = ( (x, y + end), (x+mid,y) )
    S13 = visual.ShapeStim(win= mywin, vertices= V13 )

    x = start_x
    y = start_y + 4*gap_y
    # Constructing H for that particular block
    V14 = ( (x, y + end), (x+mid,y) )
    S14 = visual.ShapeStim(win= mywin, vertices= V14 )

    x = start_x
    y = start_y + 3*gap_y
    # Constructing H for that particular block
    V15 = ( (x, y + end), (x+mid,y) )
    S15 = visual.ShapeStim(win= mywin, vertices= V15 )

    x = start_x
    y = start_y + 2*gap_y
    # Constructing H for that particular block
    V16 = ( (x, y + end), (x+mid,y) )
    S16 = visual.ShapeStim(win= mywin, vertices= V16 )

    x = start_x + gap_x
    y = start_y + 2*gap_y
    # Constructing H for that particular block
    V17 = ( (x, y + end), (x+mid,y) )
    S17 = visual.ShapeStim(win= mywin, vertices= V17 )

    x = start_x + 2*gap_x
    y = start_y + 2*gap_y
    # Constructing H for that particular block
    V18 = ( (x, y + end), (x+mid,y) )
    S18 = visual.ShapeStim(win= mywin, vertices= V18 )

    x = start_x + 2*gap_x
    y = start_y + gap_y
    # Constructing H for that particular block
    V19 = ( (x, y + end), (x+mid,y) )
    S19 = visual.ShapeStim(win= mywin, vertices= V19 )

    x = start_x + 2*gap_x
    y = start_y
    # Constructing H for that particular block
    V20 = ( (x, y + end), (x+mid,y) )
    S20 = visual.ShapeStim(win= mywin, vertices= V20 )

    x = start_x + gap_x
    y = start_y
    # Constructing H for that particular block
    V21 = ( (x, y + end), (x+mid,y) )
    S21 = visual.ShapeStim(win= mywin, vertices= V21 )

    x = start_x
    y = start_y
    # Constructing H for that particular block
    V22 = ( (x, y + end), (x+mid,y) )
    S22 = visual.ShapeStim(win= mywin, vertices= V22 )

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

    S12.draw()
    S13.draw()
    S14.draw()
    S15.draw()
    S16.draw()
    S17.draw()
    S18.draw()
    S19.draw()
    S20.draw()
    S21.draw()
    S22.draw()

    mywin.flip()
