# implementation of card game - Memory
# http://www.codeskulptor.org/#user40_Kurb83MIRHjDTqo.py

import simplegui, random

# helper function to initialize globals
def new_game():
    global cards, exposed, state, check_1, check_2, bool_1, bool_2, turns
    bool_1 = bool_2 = check_1 = check_2 = state = turns = 0
    label.set_text("Turns = " +str(turns))
    cards_a = cards_b = range(8)
    cards = cards_a + cards_b
    random.shuffle(cards)
    exposed = [False for i in range(len(cards))]

# define event handlers
def mouseclick(pos):
    global exposed, state, check_1, check_2, bool_1, bool_2, turns
    # add game state logic here
    card_index = pos[0] // 50
    if exposed[card_index] == False:
        if state == 0:
            exposed[card_index] = True
            check_1 = cards[card_index]
            bool_1 = card_index
            state = 1
        elif state == 1:
            exposed[card_index] = True
            check_2 = cards[card_index]
            bool_2 = card_index
            state = 2
            turns += 1
            label.set_text("Turns = " +str(turns))
        elif state ==2:
            if check_1 != check_2:
                exposed[bool_1] = False
                exposed[bool_2] = False
            exposed[card_index] = True
            check_1 = cards[card_index]
            bool_1 = card_index
            state = 1
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for card in range(len(cards)):
        card_pos = 50 * card
        if exposed[card] == True:
            canvas.draw_text(str(cards[card]), (card_pos + 15, 65), 40, "White") 
        elif exposed[card] == False:
            canvas.draw_polygon([[card_pos ,0], [card_pos + 50, 0], [card_pos + 50, 100], [card_pos, 100]], 5, "Black", "Green")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100, 160)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
