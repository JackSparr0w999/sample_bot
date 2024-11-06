#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:57:48 2024

@author: studente
"""
def choose_profile():
    
    print('Choose a profile 1/2/3/4 \n (1). John \n (2). Jack Sparrow \n (3). Stephen Hawking \n (4). Add a profile')

    profile = input("-> ")

    if profile == '1':
        
        print('Welcome John')
        print('What do you want to do today? \n (1). Operation with two numbers \n (2). Send a spaceship to a planet of your choice')
        to_do = input('-> ')
        
        if to_do == "1":
            
            print('Ok, give me two numbers. Write below the first')
            first_number = int(input('-> '))
            print('Now the second')
            second_number = int(input('-> '))
            print('Ok boss, but what do you want to do? \n (1). Sum \n (2). Subtraction')
            choose_op = input('-> ')
            
            if  choose_op == "1":
                return first_number + second_number
            elif choose_op == '2':
                return first_number - second_number
            
        elif to_do == "2":
            print('Great choice. Which planet do you want to send the mission to? \n Write a planet name: ')
            planet = input('-> ')
            
            if planet == "Mars" or "Jupiter" or "Saturn" or "Venus" or "":
                return f'Operation accomplished: our first available spaceship will be sent to {planet}'
            elif planet == "Earth":
                return "Why do you want to send a mission on your own planet? Are you an alien? "
            else: 
                return f'Operation aborted: I do not know the planet {planet}'
            
        
    
    elif profile == '2':
        return "Welcome Jack Sparrow \n I\'m sorry, nothing to do on this profile yet, come back tomorrow."
    
    elif profile == '3':
        return 'Welcome Stephen Hawking \n I\'m sorry, nothing to do on this profile yet, come back tomorrow.'
    
    elif profile == '4':
        print('Do you wanna add a profile? y/n')
        response = input("-> ")
    
        if response == 'y':
            name = input('Write the name to add -> ')
            return f'Perfect! "{name}" has been added to favorites'
            
        elif response == "n":
            print('Ok, press enter to come back to the main menu')
            enter = input("-> ")
            return choose_profile()
            
            
print(choose_profile())
        

        