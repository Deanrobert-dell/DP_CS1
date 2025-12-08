if drawer.xcor() < SCREEN_WIDTH / 2:
        screen.ontimer(animate_line, int(DELAY * 1000)) # Delay in milliseconds
    else:
        # Stop animation
        print("Animation finished!")
