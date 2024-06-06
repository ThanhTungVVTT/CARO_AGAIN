from config import *
from button import Button
from board import Board
board=Board()
import pygame,sys
pygame.init()


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/images/font.ttf", size)


def draw_main_menu(screen,buttons,back_ground_image):
    screen.blit(back_ground_image,(0,0))
    MENU_TEXT=get_font(50).render("MAIN MENU",True,(255,255,255))
    MENU_RECT=MENU_TEXT.get_rect(center=(((WIDTH+board.ADD_WIDTH)//2),HEIGHT//2-200))
    screen.blit(MENU_TEXT,MENU_RECT)

    
    for button in buttons:
        button.changeColor(pygame.mouse.get_pos())
        button.update(screen)

def create_button():
    PLAY_BUTTON=Button(image=None,pos=((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2-50),text_input="PLAY",font=get_font(40),base_color="#d7fcd4",hovering_color=(0,0,200))
    OPTIONS_BUTTON=Button(image=None,pos=((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2+70),text_input="OPTIONS",font=get_font(40),base_color="#d7fcd4",hovering_color=(0,200,0))
    QUIT_BUTTON=Button(image=None,pos=((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2+190),text_input="QUIT",font=get_font(40),base_color="#d7fcd4",hovering_color=(200,0,0))
    return [PLAY_BUTTON,OPTIONS_BUTTON,QUIT_BUTTON]

def size_board():
    _3x3=Button(image=None,pos=((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2-50),text_input="3x3",font=get_font(40),base_color="#d7fcd4",hovering_color=(0,0,200))
    _7x7=Button(image=None,pos=((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2+70),text_input="7x7",font=get_font(40),base_color="#d7fcd4",hovering_color=(0,200,0))
    _15x15=Button(image=None,pos=((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2+190),text_input="15x15",font=get_font(40),base_color="#d7fcd4",hovering_color=(200,0,0))
    BACK_BUTTON=Button(image=None,pos=((WIDTH+board.ADD_WIDTH)//2,HEIGHT//2+310),text_input="BACK",font=get_font(40),base_color="#d7fcd4",hovering_color=(200,0,0))
    return [_3x3,_7x7,_15x15,BACK_BUTTON]

def draw_option_menu(screen,option_button,back_ground_image):
    screen.blit(back_ground_image,(0,0))
    OPTION_TEXT=get_font(50).render("OPTIONS",True,(255,255,255))
    OPTION_RECT=OPTION_TEXT.get_rect(center=(((WIDTH+board.ADD_WIDTH)//2),HEIGHT//2-200))
    screen.blit(OPTION_TEXT,OPTION_RECT)    
    for button in option_button:
        button.changeColor(pygame.mouse.get_pos())
        button.update(screen)

