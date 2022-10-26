import os
import pygame.midi
from winreg import *

def FindSoundpad():
    Registry = ConnectRegistry(None, HKEY_CLASSES_ROOT)
    RawKey = OpenKey(Registry, "Soundpad\shell\open\command")
    try: 
        name, value, type = EnumValue(RawKey, 0)
        path = '{}'.format(value).replace('" -c "%1"', '').replace('"', '')    
        print('Found Sountpad: {}'.format(path))
        return path
    except WindowsError: 
        print()

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
                os.system("{0} -rc DoPlaySound({1})".format(SoundPad,note_number))
                

pygame.midi.init()
os.system('cls')
SoundPad = FindSoundpad()
print_devices()
readInput(pygame.midi.Input(1))