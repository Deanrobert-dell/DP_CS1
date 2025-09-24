def spin_the_fidget():
    global no_of_spins
    #clearing the objects on the turtle window
    clear()
    #setting the angle based on number of spins
    angle = no_of_spins / 10
    dot(120, 'black')
    #setting the angle
    right(angle)
    #Drawing the first lobe
    #Moving the mouse by 100 units in the 'angle' direction to draw the arm
    forward(150)
    dot(120, 'red') #Drawing the cap at the end of the arm of radius 120 units and red color
    back(150) #Moving the drawing pen back to the center
    #Drawing the second lobe
    right(120) #Changing the angle  to right by 120 degrees
    #Moving the mouse by 100 units in the 'angle' direction to draw the second arm
    forward(150)
    dot(120, 'green')#Drawing the cap at the end of the arm of radius 120 units and green color
    back(150)#Moving the drawing pen back to the center
    #Drawing the third lobe
    right(120)#Changing the angle  to right by 120 degrees
    #Moving the mouse by 100 units in the 'angle' direction to draw the third arm
    forward(150)
    dot(120, 'blue')#Drawing the cap at the end of the arm of radius 120 units and blue color
    back(150)#Moving the drawing pen back to the center
    right(120)#Changing the angle  to right by 120 degrees
    update() #Updating the turtle window