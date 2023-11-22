# Author name: Jeremiah E. Ochepo
# Last Edited: 2/28/2020 (2 PM)
# Description: Archery Target GUI

from graphics import *

def main():
    # Create a graphics window
    win = GraphWin('Shapes', 500, 500, autoflush=False)

    # Program Status Message
    msg = Text(Point(250.0, 20.0), 'Archery Target')
    msg.setFace('helvetica')
    msg.setStyle('bold')
    msg.setSize(12)
    msg.draw(win)

    # List of colors for the target rings
    color_list = ['black', 'yellow', 'red', 'blue', 'white']
    radius = 20

    # Function to draw the white ring
    def white_shape_method():
        shape = Circle(Point(250, 250), radius * 4)
        shape.setFill(color_list[4])
        shape.setOutline(color_list[0])
        shape.draw(win)

    # Call the function to draw the white ring
    white_shape_method()

    # Function to draw the blue ring
    def blue_shape_method():
        shape = Circle(Point(250, 250), radius * 3)
        shape.setFill(color_list[3])
        shape.setOutline(color_list[0])
        shape.draw(win)

    # Call the function to draw the blue ring
    blue_shape_method()

    # Function to draw the red ring
    def red_shape_method():
        shape = Circle(Point(250, 250), radius * 2)
        shape.setFill(color_list[2])
        shape.setOutline(color_list[0])
        shape.draw(win)

    # Call the function to draw the red ring
    red_shape_method()

    # Function to draw the yellow ring
    def yellow_shape_method():
        shape = Circle(Point(250, 250), radius)
        shape.setFill(color_list[1])
        shape.setOutline(color_list[0])
        shape.draw(win)

    # Call the function to draw the yellow ring
    yellow_shape_method()

    # Update program status message
    msg.setText('Click Again to Quit')

    # Wait for a mouse click to close the window
    pt = win.getMouse()
    win.close()

try:
    main()
except:
    pass
