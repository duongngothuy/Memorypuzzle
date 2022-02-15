#GROUP: MEMORY MATCH
#Members: Aidan Koenigsberger, Duong Ngo, Ngwe Sin
#Assignment: Final Project



# Necessary for pygame zero
import pgzrun, random

# Used for Quitting the Program
import sys
import time as time_lib


# chooses a random element from the inputted list
def choose_image(image_list):
    new_list = image_list
    index = random.randint(0, len(new_list) - 1)
    image = (new_list[index])
    return image


# Window Properties

TITLE = 'Match the Puzzle'
WIDTH = 1200
HEIGHT = 600


#Game states
game = Actor('sun')
game.midtop = (400, 200)
game.state = ['title', 'game', 'gameover', 'win']
game.current_state = game.state[0]


# Get the images to match using this dictionary 
match_log = {}
# Sets up all tiles as actors with a certain image
tile_list = ['sun', 'sun', 'circle', 'circle', 'diamond', 'diamond', 'moon',
             'moon', 'smiley', 'smiley']
#Places and assigns match values to each tile
icon = choose_image(tile_list)
tile_list.remove(icon)
tile1 = Actor(icon, center=(100, 100))
if icon == 'sun':
    match_log[tile1] = 'SUN'
elif icon == 'circle':
    match_log[tile1] = 'CIRCLE'
elif icon == 'diamond':
    match_log[tile1] = 'DIAMOND'
elif icon == 'moon':
    match_log[tile1] = 'MOON'
elif icon == 'smiley':
    match_log[tile1] = 'SMILEY'

icon = choose_image(tile_list)
tile_list.remove(icon)
tile2 = Actor(icon, center=(300, 100))
if icon == 'sun':
    match_log[tile2] = 'SUN'
elif icon == 'circle':
    match_log[tile2] = 'CIRCLE'
elif icon == 'diamond':
    match_log[tile2] = 'DIAMOND'
elif icon == 'moon':
    match_log[tile2] = 'MOON'
elif icon == 'smiley':
    match_log[tile2] = 'SMILEY'

icon = choose_image(tile_list)
tile_list.remove(icon)
tile3 = Actor(icon, center=(500, 100))
if icon == 'sun':
    match_log[tile3] = 'SUN'
elif icon == 'circle':
    match_log[tile3] = 'CIRCLE'
elif icon == 'diamond':
    match_log[tile3] = 'DIAMOND'
elif icon == 'moon':
    match_log[tile3] = 'MOON'
elif icon == 'smiley':
    match_log[tile3] = 'SMILEY'

icon = choose_image(tile_list)
tile_list.remove(icon)
tile4 = Actor(icon, center=(700, 100))
if icon == 'sun':
    match_log[tile4] = 'SUN'
elif icon == 'circle':
    match_log[tile4] = 'CIRCLE'
elif icon == 'diamond':
    match_log[tile4] = 'DIAMOND'
elif icon == 'moon':
    match_log[tile4] = 'MOON'
elif icon == 'smiley':
    match_log[tile4] = 'SMILEY'

icon = choose_image(tile_list)
tile_list.remove(icon)
tile5 = Actor(icon, center=(900, 100))
if icon == 'sun':
    match_log[tile5] = 'SUN'
elif icon == 'circle':
    match_log[tile5] = 'CIRCLE'
elif icon == 'diamond':
    match_log[tile5] = 'DIAMOND'
elif icon == 'moon':
    match_log[tile5] = 'MOON'
elif icon == 'smiley':
    match_log[tile5] = 'SMILEY'

icon = choose_image(tile_list)
tile_list.remove(icon)
tile6 = Actor(icon, center=(100, 300))
if icon == 'sun':
    match_log[tile6] = 'SUN'
elif icon == 'circle':
    match_log[tile6] = 'CIRCLE'
elif icon == 'diamond':
    match_log[tile6] = 'DIAMOND'
elif icon == 'moon':
    match_log[tile6] = 'MOON'
elif icon == 'smiley':
    match_log[tile6] = 'SMILEY'

icon = choose_image(tile_list)
tile_list.remove(icon)
tile7 = Actor(icon, center=(300, 300))
if icon == 'sun':
    match_log[tile7] = 'SUN'
elif icon == 'circle':
    match_log[tile7] = 'CIRCLE'
elif icon == 'diamond':
    match_log[tile7] = 'DIAMOND'
elif icon == 'moon':
    match_log[tile7] = 'MOON'
elif icon == 'smiley':
    match_log[tile7] = 'SMILEY'

icon = choose_image(tile_list)
tile_list.remove(icon)
tile8 = Actor(icon, center=(500, 300))
if icon == 'sun':
    match_log[tile8] = 'SUN'
elif icon == 'circle':
    match_log[tile8] = 'CIRCLE'
elif icon == 'diamond':
    match_log[tile8] = 'DIAMOND'
elif icon == 'moon':
    match_log[tile8] = 'MOON'
elif icon == 'smiley':
    match_log[tile8] = 'SMILEY'

icon = choose_image(tile_list)
tile_list.remove(icon)
tile9 = Actor(icon, center=(700, 300))
if icon == 'sun':
    match_log[tile9] = 'SUN'
elif icon == 'circle':
    match_log[tile9] = 'CIRCLE'
elif icon == 'diamond':
    match_log[tile9] = 'DIAMOND'
elif icon == 'moon':
    match_log[tile9] = 'MOON'
elif icon == 'smiley':
    match_log[tile9] = 'SMILEY'

icon = choose_image(tile_list)
tile_list.remove(icon)
tile10 = Actor(icon, center=(900, 300))
if icon == 'sun':
    match_log[tile10] = 'SUN'
elif icon == 'circle':
    match_log[tile10] = 'CIRCLE'
elif icon == 'diamond':
    match_log[tile10] = 'DIAMOND'
elif icon == 'moon':
    match_log[tile10] = 'MOON'
elif icon == 'smiley':
    match_log[tile10] = 'SMILEY'

#assigning and using global variables
guess1 = ''
guess2 = ''
clicks = 0
match_count = 0
hold1 = ''
hold2 = ''

#Checks where the user clicks to try and determine if a match was made
def on_mouse_down(pos):
    global guess1, guess2, clicks, hold1, hold2

    if tile1.collidepoint(pos):
        clicks += 1
        if clicks % 2 != 0:
            guess1 = match_log[tile1]
            hold1 = tile1

        elif clicks % 2 == 0:
            guess2 = match_log[tile1]
            hold2 = tile1
            match(guess1, guess2, hold1, hold2)

    if tile2.collidepoint(pos):
        clicks += 1
        if clicks % 2 != 0:
            guess1 = match_log[tile2]
            hold1 = tile2

        elif clicks % 2 == 0:
            guess2 = match_log[tile2]
            hold2 = tile2
            match(guess1, guess2, hold1, hold2)

    if tile3.collidepoint(pos):
        clicks += 1
        if clicks % 2 != 0:
            guess1 = match_log[tile3]
            hold1 = tile3

        elif clicks % 2 == 0:
            guess2 = match_log[tile3]
            hold2 = tile3
            match(guess1, guess2, hold1, hold2)

    if tile4.collidepoint(pos):
        clicks += 1
        if clicks % 2 != 0:
            guess1 = match_log[tile4]
            hold1 = tile4

        elif clicks % 2 == 0:
            guess2 = match_log[tile4]
            hold2 = tile4
            match(guess1, guess2, hold1, hold2)

    if tile5.collidepoint(pos):
        clicks += 1
        if clicks % 2 != 0:
            guess1 = match_log[tile5]
            hold1 = tile5

        elif clicks % 2 == 0:
            guess2 = match_log[tile5]
            hold2 = tile5
            match(guess1, guess2, hold1, hold2)

    if tile6.collidepoint(pos):
        clicks += 1
        if clicks % 2 != 0:
            guess1 = match_log[tile6]
            hold1 = tile6

        elif clicks % 2 == 0:
            guess2 = match_log[tile6]
            hold2 = tile6
            match(guess1, guess2, hold1, hold2)
            
    if tile7.collidepoint(pos):
        clicks += 1
        if clicks % 2 != 0:
            guess1 = match_log[tile7]
            hold1 = tile7

        elif clicks % 2 == 0:
            guess2 = match_log[tile7]
            hold2 = tile7
            match(guess1, guess2, hold1, hold2)
    if tile8.collidepoint(pos):
        clicks += 1
        if clicks % 2 != 0:
            guess1 = match_log[tile8]
            hold1 = tile8

        elif clicks % 2 == 0:
            guess2 = match_log[tile8]
            hold2 = tile8
            match(guess1, guess2, hold1, hold2)
    if tile9.collidepoint(pos):
        clicks += 1
        if clicks % 2 != 0:
            guess1 = match_log[tile9]
            hold1 = tile9

        elif clicks % 2 == 0:
            guess2 = match_log[tile9]
            hold2 = tile9
            match(guess1, guess2, hold1, hold2)
    if tile10.collidepoint(pos):
        clicks += 1
        if clicks % 2 != 0:
            guess1 = match_log[tile10]
            hold1 = tile10

        elif clicks % 2 == 0:
            guess2 = match_log[tile10]
            hold2 = tile10
            match(guess1, guess2, hold1, hold2)

#When tiles match, tiles disappear out of screen, the victory sound plays and match counted as a score
def match(first, second, first1, second1):
    global match_count
    if first == second:
        # score += 1
        # Make a match
        print('match')
        sounds.victory.play()

        match_count += 1
        first1.pos = 2000, 2000  # move the tiles out of screen after matched
        second1.pos = 2000, 2000
        if match_count == 5:
            game.current_state = game.state[3]

    else:
        # flip back
        print('not a match')


# Draw function provided by pygame zero draws screens and tiles based on gamestate
def draw():
    global timer, match_count
    
    #title and about screen combined
    # Makes the screen a light blue
    screen.fill((100, 255, 255))
    if game.current_state == 'title':
        screen.fill((100, 255, 255))
        screen.draw.text("Match the pairs!",
                         (330, 200), color="red", fontsize=90)

        screen.draw.text("Can you find match it all in 10 seconds?",
                         (300, 350), color="red", fontsize=40)

        screen.draw.text("By Aidan Koenigsberger, Duong Ngo, Ngwe Sin",
                         (700, 5), color="red", fontsize=30)

        screen.draw.text("Press SPACE to find out!",
                         (400, 400), color="Blue",
                         fontsize=40)  # pressing on spacebar to bring to the game menu screen

        tile1.pos = 100, 100
        tile2.pos = 300, 100
        tile3.pos = 500, 100
        tile4.pos = 700, 100
        tile5.pos = 900, 100
        tile6.pos = 100, 300
        tile7.pos = 300, 300
        tile8.pos = 500, 300
        tile9.pos = 700, 300
        tile10.pos = 900, 300


    #main game board with timer and match counter
    elif game.current_state == 'game':
        screen.fill((100, 255, 255))
        screen.draw.text(f"Time passed: {round(timer, 2)}", (950, 0),
                         color="red", fontsize=30)
        screen.draw.text(f"Matches: {match_count}", (0, 0), color="red",
                         fontsize=30)

        tile1.draw()
        tile2.draw()
        tile3.draw()
        tile4.draw()
        tile5.draw()
        tile6.draw()
        tile7.draw()
        tile8.draw()
        tile9.draw()
        tile10.draw()

    #game over screen
    elif game.current_state == 'gameover':
        screen.blit('gameover', (380, 120))
        screen.draw.text("Press Enter to Return", (400, 300), color="Blue", 
                         fontsize=50)
        timer = 0
        match_count = 0 
     
    #winner screen
    elif game.current_state == 'win':
        # screen.fill(255, 100, 255)
        screen.draw.text("All matched!", (380, 200), color="Red", fontsize=80)
        screen.draw.text("You win! ", (440, 300), color="Red", fontsize=80)
        screen.draw.text("Press Enter to Return", (420, 420), color="Blue", 
                         fontsize=50)
        
        timer = 0
        match_count = 0
        
        pass



def timer(delta):
    pass



# This function runs ~60 times every second
#   dt is a parameter that holds the amount of
#   time since the last call to update (delta time)


timer = 0
#Used to switch screens and control timer
def update(dt):
    # Add game states to go back to the start of the game
    global timer

    # if playing:
    # timer += dt
    if keyboard.space and game.current_state == 'title':
        # hitting the keyboard space bar will take us to the board
        game.current_state = game.state[1]
        on_key_down(dt)

        #timer = 0  # counting down but need to find a way to say game over and reset the screen when the time's up

    if game.current_state == 'game':
        timer += dt

    if 10 > timer> 7:
        if int(timer) + 0.0175 > timer > int(timer) - 0.0175:
            sounds.clockbeep.play()

    elif timer > 10:
        game.current_state = game.state[2]
        music.stop()



# Function provided by pygame zero to check for keyboard presses and switch screens
def on_key_down(key):
    
    if game.current_state == 'title':
        if key == keys.SPACE:
            # Change the state to be "game" when you hit spacebar
            game.current_state = game.state[1]

            music.set_volume(0.3)
            music.play('bgrmusic.wav')
            
# return to title screen after game over or winning screen when you hit enter
    if game.current_state == 'gameover':
        if key == keys.RETURN:
            # Change the state to be "game"
            game.current_state = game.state[0]
            time = 0
            

    elif game.current_state == 'win':
        if key == keys.RETURN:
            # Change the state to be "game"
            game.current_state = game.state[0]
            time = 0
            



    # Check for escape key press
    if key == keys.ESCAPE:
        # Exit the program
        sys.exit()


# Start pygame zero
pgzrun.go()
