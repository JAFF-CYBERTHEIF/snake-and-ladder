# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 21:05:44 2021
snake and ladder
@author: jawahar
"""
#importing random for dice
import random

#setup counter for two players
p1=0
p2=0

dice=0
#elements of board represents the weight of blocks 
#the index of the element is indexes in the board
#first element is out of board where players starts to play 
board=[0,0,0,0,4,0,0,0,0,-3,0,0,5,0,0,0,-10,0,0,3,0,0,0,-8,0,0]

#looping untill the end of the game
for i in range(1,1000000000000000):
    
    #break if any one of the player reached 25
    if p1==25:
        print("player 1 is the winner")
        break
    if p2==25:
        print("player 2 is the winner")
        break
    #allowing user to interact with the game
    user=str(input("type 'roll' and enter to roll the dice :"))
    #if user said roll, rolling the dice 
    #if user said anything else, turn will be lost
    if user=='roll':
        dice=random.randint(1,6)
        
    #palyer 2 turn if i was even number    
    if (i%2)==0:
        print('player 2 turn')
        print('DICE: ', dice)
        p2+=dice
        #checking for possiblity of move 
        if p2>25:
            p2-=dice
            print('WAIT')
        else: 
            p2+=board[p2]
        print(p2,' is the player 2 position')
    #player 1 turn if i was odd number    
    else:
        print('player 1 turn')
        print('DICE: ', dice)
        p1+=dice
        #checking for possiblity of move 
        if p1>25:
            p1-=dice
            print('wait')
        else:    
            p1+=board[p1]
        print(p1,' is the psition of player1')
    #reseting the dice value to 0   
    dice=0    
  #aurthor jawahar 
#https://www.linkedin.com/in/jawahar-b/      
