from random import randint
import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
import project as pj

# Main function to create the graphical user interface
def card_game_gui(newdeck):
    # all the global variables used for GUI and images and cards deck
    global image, images, deck, count, window, line0, line1, line2, line3, frame, btn_container
    deck = newdeck
    img_lbl = []
    count = 0

    # creating the gui layout
    def create_layout():
        global image, images, deck, count, window, line0, line1, line2, line3, frame, btn_container
        # creating main frame and lines to deploy cards on the page.
        frame = ttk.Frame(window)
        line0 = ttk.Label(frame)
        line1 = ttk.Label(frame)
        line2 = ttk.Label(frame)
        line3 = ttk.Label(frame)
        line0.pack(side='left',fill='both', expand=True)
        line1.pack(side='left',fill='both', expand=True)
        line2.pack(side='left',fill='both', expand=True)
        line3.pack(side='left',fill='both', expand=True)
        frame.pack(side='left',fill='both', expand=True)

        btn_container = ttk.Frame(window)
        txt = 'Hi there, Its a fun card game for you. Please choose a card in the deck and click on the line in which chosen card appears. Please repeat this for few times and witness the Magic!!!. \nThanks. \nNasir Amin.'
        lbl_message = ttk.Label(
            btn_container,bootstyle='inverse-primary', relief="flat",
            wraplength=270 ,justify='center', padding=20,
            text=txt, foreground='white', font='calbri 16 italic'
            )
        lbl_message.pack(side='top',pady=180)

        # creating buttons on the page
        s = ttk.Style()
        s.configure('my.TButton', font=('Helvetica', 14))
        btn_new = ttk.Button(   # New button to create a fresh deck
            btn_container,width=18,style='my.TButton',
            text='New Deck', command=new_game
            )
        btn_shuffle = ttk.Button(   # Button to shuffle the deck
            btn_container,width=18,style='my.TButton', 
            text='Shuffle Deck', command=show_shuffled
            )
        btn_quit = ttk.Button( # quit button 
            btn_container,style='my.TButton',width=18, 
            text='Quit', command=window.destroy
            )
        btn_quit.pack(side='bottom',ipadx=8, ipady=8, padx=18, pady=8)
        btn_shuffle.pack(side='bottom',ipadx=8, ipady=8, padx=15, pady=8)
        btn_new.pack(side='bottom',ipadx=8, ipady=8, padx=15, pady=8)
        btn_container.pack(expand=True)

    def wining_card(card_name): # showig the chosen card randomly and make it shorter and shorte
        global image, images, deck, count, xx, yy, line0, line1, line2, line3, frame, btn_container
        img_lbl.clear()
        line1.unbind_all('<Button-1>')
        line2.unbind_all('<Button-1>')
        line3.unbind_all('<Button-1>')
        #frame.destroy()
        image = pj.resize_image(card_name, 200, 340)
        global c, win_lbl, xx, yy
        xx,yy = window.winfo_screenwidth()/2-200,(window.winfo_screenheight()-(window.winfo_screenheight()*10/100))/2-220
        c,win_lbl = 400,None
        img_lbl.clear()
        images.clear()
        def moving_card(winlbl): # function to show chosen card randomly on screen
            global xx, yy, c, wincard
            c -= 25
            if c < 0:
                return
            winlbl.destroy()
            image = pj.resize_image(card_name, 120+c,150+c+c-int(c/2))
            winlbl=ttk.Label(window,image=image)
            winlbl.place(x=xx, y=yy)
            xx = randint(0,1000)
            yy = randint(0,500)
            window.after(500,lambda: moving_card(winlbl)) # recalling function recursivly after dealy
        winlbl = ttk.Label(window,image=image)
        winlbl.place(x=xx,y=yy)
        moving_card(winlbl)
        winlbl.destroy()
        image = pj.resize_image(card_name, 380,540)
        xx,yy = window.winfo_screenwidth()/2-200,(window.winfo_screenheight()-(window.winfo_screenheight()*10/100))/2-220
        winlbl = ttk.Label(window,image=image)
        winlbl.place(x=xx,y=yy)

    def show_deck(deck): # showing the arranged deck in 3 line format and bind them to mouse click
        img_lbl.clear()
        global image, images, line0, line1, line2, line3, frame, btn_container
        card_width, card_height = 160, 230
        images = []
        #images.clear()
        for i in range(0,52):
            image = pj.resize_image(deck[i].get_card(), card_width, card_height )
            images.append(image)
            yaxis = 0
        for i in range(0,49, 3):
            img_lbl.append(tk.Label(line1, image=images[i], width=card_width, height=card_height))
            img_lbl[i].place(x=0,y=yaxis)
            img_lbl[i].bind('<Button-1>', lambda e, c = 1: line_clicked(e, c))
            img_lbl.append(tk.Label(line2, image=images[i+1], width=card_width, height=card_height))
            img_lbl[i+1].place(x=0,y=yaxis)
            img_lbl[i+1].bind('<Button-1>', lambda e, c = 2: line_clicked(e, c))
            img_lbl.append(tk.Label(line3, image=images[i+2], width=card_width, height=card_height))
            img_lbl[i+2].place(x=0,y=yaxis)
            img_lbl[i+2].bind('<Button-1>', lambda e, c = 3: line_clicked(e, c))
            yaxis += 58
        img_lbl.append(tk.Label(line1, image=images[51], width=card_width, height=card_height))
        img_lbl[51].place(x=0,y=yaxis)
        img_lbl[51].bind('<Button-1>', lambda e, c = 1: line_clicked(e, c))  
        
    def line_clicked(event, choice): # function to arrange the deck based on choice of line clicked and on finding chosen card call winning card function
        global count, deck, image, images
        if count < 3:
            deck, chosen = pj.play_game(deck, choice)
            show_deck(deck)
        elif count >= 3 and choice == 1: # arranged 3 times but card in line 1 of 18 cards
            deck, chosen = pj.play_game(deck, choice)
            show_deck(deck)
        else: #on finding of chosen card
            deck, chosen = pj.play_game(deck, choice)
            wining_card(chosen.get_card())
            
        count += 1
    
    def show_shuffled(): # shuffle the deck and arranging it one the page.
        global deck, count
        count = 0
        deck = pj.shuffle_deck(deck)
        show_deck(deck)
    
    def new_game(): # setting the variables and populating the deck.
        global image, images, deck, count, line0, line1, line2, line3, frame, btn_container
        image = ''
        images = []
        images.clear()
        deck.clear()
        count = 0
        deck = pj.populate_std_deck()
        show_deck(deck)

    # Initialise the GUI. Creating a main window and maxmise it and then calling other gui widgets through create_layout function.
    #window = tk.Tk()
    #window.iconbitmap('icons/ace-of-spades.ico')
    #window.wm_iconphoto(True, pj.resize_image('ace-of-spades'))

    window = ttk.Window(themename='journal') # ttk bootstrap window themed
    window.title("A Card Game by Nasir Amin!")
    window.iconphoto(False, tk.PhotoImage(file='icons/ace-of-spades.png'))
    window.eval('tk::PlaceWindow . center')
    #window.state('zoomed') # Maximising the window
    window.minsize(1000, 800)
    create_layout() # creating label and buttons widgets
    new_game() # Initialising the deck and other global variables to set the game.
    
    window.mainloop()
