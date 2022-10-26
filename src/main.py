import os
from os import system, name
import pygame.midi


def print_devices():
    for n in range(pygame.midi.get_count()):
        print (n,pygame.midi.get_device_info(n))

def readInput(input_device):
    while True:
        if input_device.poll():
            event = input_device.read(1)[0]
            data = event[0]
            id = data[0]
            note_number = data[1]
            velocity = data[2]
            if velocity != 0:
                os.system('cls')
                print ("Key:{0} \n\rNote:{1}".format(id,note_number))
                os.system("E:\SteamLibrary\steamapps\common\Soundpad\Soundpad.exe -rc DoPlaySound({})".format(note_number))
                

pygame.midi.init()
os.system('cls')
#print_devices()
readInput(pygame.midi.Input(1))