from winreg import *
import os
import pygame.midi
import subprocess

def start():
    if not process_exists('Soundpad.exe'):
      os.system("start \"\" steam://rungameid/629520")
      print('Soundoad not running!')
    pygame.midi.init()
    os.system('cls')
    print_devices()
    readInput(pygame.midi.Input(1))

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

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    output = subprocess.check_output(call).decode()
    last_line = output.strip().split('\r\n')[-1]
    return last_line.lower().startswith(process_name.lower())

def print_devices():
    for n in range(pygame.midi.get_count()):
        print (n,pygame.midi.get_device_info(n))

def readInput(input_device):
    SoundPad = FindSoundpad()
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
                
start()