from psychopy import core, visual, event
import numpy, random

def Draw_HX(mywin):

    start_x = -2.0
    start_y = -6.0
    mid = 1.0           # Breadth of a single block of H
    end = 2.0           # Height of a single block of H
    gap_y = end + 0.5   # Gap in y-axis between two consecutive blocks of H
    gap_x = mid + 0.5   # Gap in x-axis between two consecutive blocks of H

    # Specifying the block number of S
    x = start_x
    y = start_y
    V1 = ( (x+mid, y + end), (x,y) )
    # Constructing X for that particular block
    H1 = visual.ShapeStim(win= mywin, vertices= V1 )

    x = start_x
    y = start_y + gap_y
    # Constructing S for that particular block
    V2 = ( (x+mid, y + end), (x,y) )
    H2 = visual.ShapeStim(win= mywin, vertices= V2 )

    x = start_x
    y = start_y + 2*gap_y
    # Constructing S for that particular block
    V3 = ( (x+mid, y + end), (x,y) )
    H3 = visual.ShapeStim(win= mywin, vertices= V3 )

    x = start_x
    y = start_y + 3*gap_y
    # Constructing S for that particular block
    V4 = ( (x+mid, y + end), (x,y) )
    H4 = visual.ShapeStim(win= mywin, vertices= V4 )

    x = start_x
    y = start_y + 4*gap_y
    # Constructing S for that particular block
    V5 = ( (x+mid, y + end), (x,y) )
    H5 = visual.ShapeStim(win= mywin, vertices= V5 )

    x = start_x + gap_x
    y = start_y + 2*gap_y
    # Constructing S for that particular block
    V6 = ( (x+mid, y + end), (x,y) )
    H6 = visual.ShapeStim(win= mywin, vertices= V6 )

    x = start_x + 2*gap_x
    y = start_y
    # Constructing S for that particular block
    V7 = ( (x+mid, y + end), (x,y) )
    H7 = visual.ShapeStim(win= mywin, vertices= V7 )

    x = start_x + 2*gap_x
    y = start_y + gap_y
    # Constructing S for that particular block
    V8 = ( (x+mid, y + end), (x,y) )
    H8 = visual.ShapeStim(win= mywin, vertices= V8 )

    x = start_x + 2*gap_x
    y = start_y + 2*gap_y
    # Constructing S for that particular block
    V9 = ( (x+mid, y + end), (x,y) )
    H9 = visual.ShapeStim(win= mywin, vertices= V9 )

    x = start_x + 2*gap_x
    y = start_y + 3*gap_y
    # Constructing S for that particular block
    V10 = ( (x+mid, y + end), (x,y) )
    H10 = visual.ShapeStim(win= mywin, vertices= V10 )

    x = start_x + 2*gap_x
    y = start_y + 4*gap_y
    # Constructing S for that particular block
    V11 = ( (x+mid, y + end), (x,y) )
    H11 = visual.ShapeStim(win= mywin, vertices= V11 )

    # Specifying the block number of S
    x = start_x
    y = start_y
    V12 = ( (x, y + end), (x+mid,y) )
    # Constructing X for that particular block
    H12 = visual.ShapeStim(win= mywin, vertices= V12 )

    x = start_x
    y = start_y + gap_y
    # Constructing S for that particular block
    V13 = ( (x, y + end), (x+mid,y) )
    H13 = visual.ShapeStim(win= mywin, vertices= V13 )

    x = start_x
    y = start_y + 2*gap_y
    # Constructing S for that particular block
    V14 = ( (x, y + end), (x+mid,y) )
    H14 = visual.ShapeStim(win= mywin, vertices= V14 )

    x = start_x
    y = start_y + 3*gap_y
    # Constructing S for that particular block
    V15 = ( (x, y + end), (x+mid,y) )
    H15 = visual.ShapeStim(win= mywin, vertices= V15 )

    x = start_x
    y = start_y + 4*gap_y
    # Constructing S for that particular block
    V16 = ( (x, y + end), (x+mid,y) )
    H16 = visual.ShapeStim(win= mywin, vertices= V16 )

    x = start_x + gap_x
    y = start_y + 2*gap_y
    # Constructing S for that particular block
    V17 = ( (x, y + end), (x+mid,y) )
    H17 = visual.ShapeStim(win= mywin, vertices= V17 )

    x = start_x + 2*gap_x
    y = start_y
    # Constructing S for that particular block
    V18 = ( (x, y + end), (x+mid,y) )
    H18 = visual.ShapeStim(win= mywin, vertices= V18 )

    x = start_x + 2*gap_x
    y = start_y + gap_y
    # Constructing S for that particular block
    V19 = ( (x, y + end), (x+mid,y) )
    H19 = visual.ShapeStim(win= mywin, vertices= V19 )

    x = start_x + 2*gap_x
    y = start_y + 2*gap_y
    # Constructing S for that particular block
    V20 = ( (x, y + end), (x+mid,y) )
    H20 = visual.ShapeStim(win= mywin, vertices= V20 )

    x = start_x + 2*gap_x
    y = start_y + 3*gap_y
    # Constructing S for that particular block
    V21 = ( (x, y + end), (x+mid,y) )
    H21 = visual.ShapeStim(win= mywin, vertices= V21 )

    x = start_x + 2*gap_x
    y = start_y + 4*gap_y
    # Constructing S for that particular block
    V22 = ( (x, y + end), (x+mid,y) )
    H22 = visual.ShapeStim(win= mywin, vertices= V22 )

    H1.draw()
    H2.draw()
    H3.draw()
    H4.draw()
    H5.draw()
    H6.draw()
    H7.draw()
    H8.draw()
    H9.draw()
    H10.draw()
    H11.draw()

    H12.draw()
    H13.draw()
    H14.draw()
    H15.draw()
    H16.draw()
    H17.draw()
    H18.draw()
    H19.draw()
    H20.draw()
    H21.draw()
    H22.draw()

    mywin.update()
