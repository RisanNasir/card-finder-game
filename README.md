# Card Finder Game

#### Video Demo:  <https://youtu.be/pwWzn2WsXh8/>

## Overview and how to Play

Card Finder is an engaging card game that utilizes a graphical user interface, displaying the deck of cards in three columns. The interface includes three interactive buttons: New Deck, Shuffle, and Quit. Users have the option to reset and shuffle the deck as often as they desire. Once a player is satisfied and has selected a card to remember, they must click on the column where their chosen card appears, repeating this process three times, during which the card will change columns each time. After the third selection, the game will attempt to guess the chosen card, presenting it in the center of the screen with a random size and position.

### Necessary Imports and libraries

In this project, the primary library utilized for the graphical user interface is tkinter, which facilitates interaction with the game. Additionally, ttkbootstrap is employed to enhance the aesthetic appeal of the interface. The random module is also incorporated to randomly select a card, shuffle it, and determine the screen coordinates for displaying the card. Furthermore, the PILLOW library is utilized to manage the PNG images of the cards. Specifically, the Image and ImageTk methods from the PILLOW library are used to open the image files, resize them, and convert them into PhotoImage objects for display within label widgets. While considering various GUI libraries such as PyQt6, PyGUI, Kivy, wxPython, PySimpleGUI, and tkinter, I opted for tkinter due to its long-standing presence and preinstallation with Python, which contributes to its ease of use. Although tkinter may appear somewhat outdated, this concern is mitigated by the use of ttkbootstrap, which modernizes and stylizes the tkinter widgets. Additionally, tkinter demonstrates compatibility across Windows, Mac, and Linux platforms, although I did observe a slight delay at times when loading widgets.

### Challenges

The primary challenge I encountered in this project was the development of the graphical user interface (GUI), as I was entirely unfamiliar with any of the GUI libraries available in Python. This presented a significant initial challenge, particularly regarding the layout designs. I dedicated time to researching the subject, thoroughly reviewing the documentation, and watching several tutorials on Tkinter. Ultimately, I was able to comprehend its functionalities and effectively implement it in my project. In addition to the GUI, I invested a considerable amount of time understanding the sleep time considerations related to the Time, Async, or Tkinter after methods. Ultimately, I found Tkinter's after method to be particularly useful in the context of my GUI implementation.

### Tests

The project undergoes testing using pytest, for which a separate test file (test_project.py) has been created with a test prefix. This file encompasses tests for all functions within project.py. Additionally, all functions were evaluated during the development of the program.

### Project Structure

In the root directory of the project, there exist two folders designated for the PNG images of cards and the icon image intended for use within the game. Additionally, there are primarily three Python files: project.py, gui.py, and test_project.py. The project.py file contains the core logic of the game, while gui.py, as its name suggests, is responsible for the creation of graphical user interface components and their representation on the screen. The test_project.py file encompasses all the tests written to be executed with pytest.

### All the components and their brief description

#### project (root)

* cardimages
  * png images of cards

* icons
  * image to use as icon in title bar

* project.py
  * Class Card:
    This is a basic card class with its __init__ function to create a crd object and its setters and getters to set card rank and suit. 

  * populate_std_deck()
This function is dedicated to make a new deck of Cards and populate 

  * shuffle_deck(deck)
As its name sujjests it shuffled the given deck and retun a shuffled deck (list of Crds object)

  * three_musketeers(deck)
This method splits shuffled deck in to three lists (18,17,17 in total 52) of cards and return them.

  * rearrange_deck(left, center, right)
This method is to rearrange the three lists into a complete deck in specific order.

  * play_game(deck, choice)
This function arranged a deck in an order where picked line will be put in middle and if it was done 3 or maore time then return the chosen as guessed.

  * resize_image(name, x=0, y=0)
This function resizes the image and return the photoimage object

  * main()
This is the entry point method from where all starts.

* gui.py
  * card_game_gui(newdeck) 
    This is the main function in the gui.py which holds all other functins in it.

  * create_layout()
    This methods responsible to creating the game layout with buttons to interact.

  * wining_card(card_name)
    This is the function to announce the guessed card

  * moving_card(winlbl)
    once card is guessed this function is called to draw the card randomly in size and place on screen.

  * show_deck(deck)
    This method draw the deck in three columns on the screen.

  * line_clicked(event, choice)
    This function is called when user clicked the column in which his chosen card presents.

  * show_shuffled()
    This method is called when user pressed the shuffle button. this method calls the shuffle method from project.py and on recieving the shuffled deck call the show_deck method to draw cards.

  * new_game()
    This method setting the variables and populating the deck with populate_std_deck function and on recieving the deck call the show_deck method to draw the deck on screen.

* test_project.py
  tests to run in pytest
  * test_populate_std_deck()
  * test_shuffle_deck()
  * test_resize_image()
  * test_three_musketeers()
  * test_rearrange_deck()
  
