from psychopy import core, visual, event
import numpy, random

def Draw_HH(mywin):

    start_x = -2.0
    start_y = -6.0
    mid = 1.0           # Breadth of a single block of H
    end = 2.0           # Height of a single block of H
    gap_y = end + 0.5   # Gap in y-axis between two consecutive blocks of H
    gap_x = mid + 0.5   # Gap in x-axis between two consecutive blocks of H

    # Specifying the block number of H
    x = start_x
    y = start_y
    V1 = ((x, y + mid), (x, y), ( x, y + end ), (x, y + mid), (x + mid, y + mid), (x + mid, y ), (x + mid, y + end ), (x + mid, y + mid) )
    # Constructing H for that particular block
    H1 = visual.ShapeStim(win= mywin, vertices= V1 )

    x = start_x
    y = start_y + gap_y
    # Constructing H for that particular block
    V2 = ((x, y + mid), (x, y), ( x, y + end ), (x, y + mid), (x + mid, y + mid), (x + mid, y ), (x + mid, y + end ), (x + mid, y + mid) )
    H2 = visual.ShapeStim(win= mywin, vertices= V2 )

    x = start_x
    y = start_y + 2*gap_y
    # Constructing H for that particular block
    V3 = ((x, y + mid), (x, y), ( x, y + end ), (x, y + mid), (x + mid, y + mid), (x + mid, y ), (x + mid, y + end ), (x + mid, y + mid) )
    H3 = visual.ShapeStim(win= mywin, vertices= V3 )

    x = start_x
    y = start_y + 3*gap_y
    # Constructing H for that particular block
    V4 = ((x, y + mid), (x, y), ( x, y + end ), (x, y + mid), (x + mid, y + mid), (x + mid, y ), (x + mid, y + end ), (x + mid, y + mid) )
    H4 = visual.ShapeStim(win= mywin, vertices= V4 )

    x = start_x
    y = start_y + 4*gap_y
    # Constructing H for that particular block
    V5 = ((x, y + mid), (x, y), ( x, y + end ), (x, y + mid), (x + mid, y + mid), (x + mid, y ), (x + mid, y + end ), (x + mid, y + mid) )
    H5 = visual.ShapeStim(win= mywin, vertices= V5 )

    x = start_x + gap_x
    y = start_y + 2*gap_y
    # Constructing H for that particular block
    V6 = ((x, y + mid), (x, y), ( x, y + end ), (x, y + mid), (x + mid, y + mid), (x + mid, y ), (x + mid, y + end ), (x + mid, y + mid) )
    H6 = visual.ShapeStim(win= mywin, vertices= V6 )

    x = start_x + 2*gap_x
    y = start_y
    # Constructing H for that particular block
    V7 = ((x, y + mid), (x, y), ( x, y + end ), (x, y + mid), (x + mid, y + mid), (x + mid, y ), (x + mid, y + end ), (x + mid, y + mid) )
    H7 = visual.ShapeStim(win= mywin, vertices= V7 )

    x = start_x + 2*gap_x
    y = start_y + gap_y
    # Constructing H for that particular block
    V8 = ((x, y + mid), (x, y), ( x, y + end ), (x, y + mid), (x + mid, y + mid), (x + mid, y ), (x + mid, y + end ), (x + mid, y + mid) )
    H8 = visual.ShapeStim(win= mywin, vertices= V8 )

    x = start_x + 2*gap_x
    y = start_y + 2*gap_y
    # Constructing H for that particular block
    V9 = ((x, y + mid), (x, y), ( x, y + end ), (x, y + mid), (x + mid, y + mid), (x + mid, y ), (x + mid, y + end ), (x + mid, y + mid) )
    H9 = visual.ShapeStim(win= mywin, vertices= V9 )

    x = start_x + 2*gap_x
    y = start_y + 3*gap_y
    # Constructing H for that particular block
    V10 = ((x, y + mid), (x, y), ( x, y + end ), (x, y + mid), (x + mid, y + mid), (x + mid, y ), (x + mid, y + end ), (x + mid, y + mid) )
    H10 = visual.ShapeStim(win= mywin, vertices= V10 )

    x = start_x + 2*gap_x
    y = start_y + 4*gap_y
    # Constructing H for that particular block
    V11 = ((x, y + mid), (x, y), ( x, y + end ), (x, y + mid), (x + mid, y + mid), (x + mid, y ), (x + mid, y + end ), (x + mid, y + mid) )
    H11 = visual.ShapeStim(win= mywin, vertices= V11 )


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

    mywin.flip()
