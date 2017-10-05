import ctypes
import time
# from gtts import gTTS
# import vlc

SendInput = ctypes.windll.user32.SendInput

P_1 = 0x02
P_2 = 0x03
P_3 = 0x04
P_4 = 0x05
F5 = 0x3F

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlag3s", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def SendKey(key, repeat=1):
    for x in range(repeat):
        PressKey(key)
        time.sleep(1)
        ReleaseKey(key)
        time.sleep(1)


def Pause():
    time.sleep(5)


def ResolveTicket(answers):
    for key in answers:
        SendKey(key, 2)


def Say(count):
    second_word = 'раз'
    if 1 < count < 5:
        second_word += 'а'

    phrase = 'Решено {0} {1}'.format(count, second_word)

    if not WITH_VOICE:
        print(phrase)
        return
    
    # tts = gTTS(text=phrase, lang='ru', slow=False)
    # tts.save('tmp.mp3')
    # p = vlc.MediaPlayer('tmp.mp3')
    # p.play()


def StartBot(ticket, repeats):
    for count in range(repeats):
        Pause()
        ResolveTicket(ticket)

        Say(count + 1)
        if count + 1 != repeats:
            SendKey(F5)


WITH_VOICE = False

answers18 = [P_1, P_3, P_1, P_2, P_2, P_2, P_3, P_2, P_2, P_3, P_3, P_2, P_3, P_3, P_2, P_3, P_2, P_2, P_3, P_3]
answers19 = [P_2, P_3, P_1, P_3, P_2, P_2, P_3, P_1, P_1, P_3, P_3, P_3, P_2, P_1, P_3, P_1, P_2, P_3, P_1, P_3]
answers20 = [P_4, P_1, P_3, P_2, P_2, P_3, P_1, P_3, P_2, P_2, P_3, P_1, P_3, P_2, P_3, P_1, P_2, P_1, P_2, P_2]
answers21 = [P_2, P_3, P_1, P_3, P_3, P_3, P_1, P_3, P_2, P_3, P_2, P_3, P_3, P_3, P_2, P_4, P_3, P_2, P_1, P_2]
answers22 = [P_1, P_2, P_2, P_3, P_1, P_3, P_1, P_2, P_3, P_4, P_2, P_1, P_1, P_3, P_2, P_3, P_2, P_2, P_3, P_1]
answers23 = [P_2, P_1, P_2, P_2, P_3, P_2, P_1, P_1, P_3, P_3, P_3, P_3, P_2, P_2, P_2, P_1, P_3, P_2, P_3, P_3]
answers24 = [P_3, P_2, P_1, P_2, P_2, P_2, P_2, P_3, P_2, P_3, P_3, P_2, P_1, P_3, P_3, P_2, P_1, P_2, P_2, P_3]
answers25 = [P_1, P_3, P_1, P_2, P_4, P_2, P_1, P_2, P_3, P_3, P_3, P_3, P_1, P_3, P_2, P_3, P_2, P_4, P_3, P_1]
answers26 = [P_3, P_2, P_2, P_1, P_2, P_2, P_1, P_2, P_3, P_2, P_3, P_2, P_2, P_3, P_2, P_2, P_1, P_3, P_2, P_2]
answers27 = [P_2, P_1, P_3, P_3, P_3, P_3, P_2, P_1, P_1, P_2, P_2, P_3, P_3, P_2, P_2, P_2, P_2, P_3, P_1, P_3]
answers28 = [P_1, P_1, P_3, P_3, P_1, P_3, P_3, P_2, P_1, P_2, P_1, P_3, P_3, P_1, P_1, P_1, P_2, P_2, P_4, P_4]
answers29 = [P_3, P_2, P_1, P_3, P_1, P_2, P_1, P_1, P_2, P_3, P_3, P_4, P_3, P_1, P_3, P_2, P_4, P_3, P_2, P_3]
answers30 = [P_1, P_2, P_2, P_2, P_3, P_2, P_3, P_1, P_3, P_2, P_3, P_3, P_3, P_2, P_4, P_3, P_1, P_3, P_1, P_2]
answers31 = [P_4, P_1, P_1, P_2, P_4, P_2, P_1, P_1, P_3, P_2, P_1, P_1, P_1, P_2, P_4, P_3, P_2, P_3, P_3, P_2]
answers32 = [P_2, P_2, P_1, P_4, P_3, P_3, P_1, P_3, P_4, P_4, P_3, P_1, P_3, P_2, P_3, P_3, P_2, P_3, P_1, P_1]
answers33 = [P_2, P_1, P_3, P_2, P_3, P_1, P_3, P_1, P_4, P_3, P_3, P_3, P_4, P_2, P_3, P_1, P_2, P_3, P_2, P_3]
answers34 = [P_3, P_2, P_2, P_2, P_1, P_3, P_1, P_2, P_3, P_2, P_3, P_3, P_1, P_2, P_1, P_2, P_3, P_3, P_2, P_3]
answers35 = [P_3, P_3, P_2, P_3, P_1, P_2, P_3, P_2, P_3, P_1, P_2, P_3, P_3, P_2, P_2, P_1, P_1, P_3, P_3, P_2]
answers36 = [P_1, P_2, P_1, P_3, P_3, P_2, P_1, P_3, P_1, P_3, P_2, P_2, P_3, P_3, P_2, P_3, P_3, P_2, P_3, P_1]
answers37 = [P_2, P_3, P_2, P_3, P_1, P_1, P_3, P_1, P_3, P_3, P_1, P_3, P_2, P_3, P_2, P_3, P_3, P_2, P_3, P_2]
answers38 = [P_2, P_2, P_2, P_3, P_1, P_3, P_2, P_4, P_2, P_1, P_2, P_2, P_3, P_3, P_2, P_1, P_2, P_3, P_2, P_2]


if __name__ == '__main__':
    print('Начнем...')
    StartBot(answers38, 10)
    Pause()
