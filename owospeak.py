import os
import random
from win32api import GetKeyState
from win32con import VK_CAPITAL
import keyboard

random.seed()

to_record = [
    'enter',
    ' ',
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]

enter_press = [
    'UwU', 'OwO', '>w<', '-w-', ';w;',
    '^w^', 'òwó', 'ôwô', 'ÒwÓ', 'ÔwÔ',
    'úwù', '>3<', '₍₍ (ง Ŏ౪Ŏ)ว ⁾⁾', '(⁄ ⁄•⁄ω⁄•⁄ ⁄)',
    '(*^ω^)', '(◕‿◕✿)', '(｡♥‿♥｡)', '(*≧ω≦*)', 
    '(つ✧ω✧)つ', '(/^-^(^ ^*)/', '٩(｡•́‿•̀｡)۶', '(´｡• ᵕ •｡`)',
    '(づ｡◕‿‿◕｡)づ', '(^._.^)ﾉ', '(￣ω￣;)', '(/^▽^)/',
    '((╬ᴗ╬*)', '(>_<)>', '^･ｪ･^'
]

dupe_set = False

def on_press(key):
    global dupe_set
    keyname = key.name.lower()

    if keyname == 'enter':
        if random.randint(1, 2) == 1:
            keyboard.write(' ' + random.choice(enter_press))
            dupe_set = False
        return

    if keyname in ('r', 'l'):
        keyname = 'w'

    if keyname == 'x' and not keyboard.is_pressed('ctrl'):
        keyname = 'ks'

    if keyname == 'c' and not keyboard.is_pressed('ctrl'):
        keyname = 'ch'

    if keyname == 'space':
        dupe_set = True
    elif dupe_set:
        if random.randint(1, 3) == 1:
            keyboard.write(keyname[0] + '-')
        dupe_set = False

    pressed_key = keyname.lower()
    if keyname != pressed_key or keyboard.is_pressed('shift') or GetKeyState(VK_CAPITAL):
        if GetKeyState(VK_CAPITAL):
            keyboard.press_and_release(pressed_key)
        else:
            keyboard.press_and_release(f'shift+{pressed_key}')
    else:
        keyboard.press_and_release(keyname)


for keys in to_record:
    keyboard.on_press_key(keys, on_press, suppress=True)

print('owospeak active!')
print('Press any key to exit\n')

os.system('pause')
