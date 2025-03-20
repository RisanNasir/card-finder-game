import pytest
from project import *
import tkinter as tk
from PIL import Image, ImageTk

def test_populate_std_deck():
    assert len(populate_std_deck()) == 52
    assert type(populate_std_deck()) == type([Card])
    assert populate_std_deck()[0].get_card() == '2_of_spades'
    assert populate_std_deck()[51].get_card() == '14_of_diamonds'

def test_shuffle_deck():
    assert len(shuffle_deck(populate_std_deck())) == 52
    #assert shuffle_deck(populate_std_deck()).find() 
    assert type(shuffle_deck(populate_std_deck())[0]) == Card

def test_resize_image():
    root = tk.Tk()
    img = Image.open('cardimages/10_of_hearts.png')
    img = ImageTk.PhotoImage(img)
    assert type(resize_image('10_of_hearts')) == type(img)

def test_three_musketeers():
    deck = populate_std_deck()
    deck = shuffle_deck(deck)
    assert len(three_musketeers(deck)) == 3
    assert len(three_musketeers(deck)[0]) == 18
    assert len(three_musketeers(deck)[1]) == 17
    assert len(three_musketeers(deck)[2]) == 17

def test_rearrange_deck():
    deck = populate_std_deck()
    deck = shuffle_deck(deck)
    list = three_musketeers(deck)
    assert type(rearrange_deck(list[0],list[1],list[2])) == type(deck)
    assert len(rearrange_deck(list[0],list[1],list[2])) == 52