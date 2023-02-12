from src.ecer.dll.DLL import KIPR

from enum import Enum


class KeyCode(Enum):
    KeyEnter = '\n',
    KeyBackSpace = '\b',
    KeyTab = '\t',
    KeyCancel = 0x03,
    KeyClear = 0x0C,
    KeyShift = 0x10,
    KeyControl = 0x11,
    KeyAlt = 0x12,
    KeyPause = 0x13,
    KeyCapsLock = 0x14,
    KeyEscape = 0x1B,
    KeySpace = 0x20,
    KeyPageUp = 0x21,
    KeyPageDown = 0x22,
    KeyEnd = 0x23,
    KeyHome = 0x24,
    KeyLeft = 0x25,
    KeyUp = 0x26,
    KeyRight = 0x27,
    KeyDown = 0x28,
    KeyComma = 0x2C,
    KeyPeriod = 0x2E,
    KeySlash = 0x2F,
    KeyZero = 0x30,
    KeyOne = 0x31,
    KeyTwo = 0x32,
    KeyThree = 0x33,
    KeyFour = 0x34,
    KeyFive = 0x35,
    KeySix = 0x36,
    KeySeven = 0x37,
    KeyEight = 0x38,
    KeyNine = 0x39,
    KeySemiColon = 0x3B,
    KeyEquals = 0x3D,
    KeyA = 0x41,
    KeyB = 0x42,
    KeyC = 0x43,
    KeyD = 0x44,
    KeyE = 0x45,
    KeyF = 0x46,
    KeyG = 0x47,
    KeyH = 0x48,
    KeyI = 0x49,
    KeyJ = 0x4A,
    KeyK = 0x4B,
    KeyL = 0x4C,
    KeyM = 0x4D,
    KeyN = 0x4E,
    KeyO = 0x4F,
    KeyP = 0x50,
    KeyQ = 0x51,
    KeyR = 0x52,
    KeyS = 0x53,
    KeyT = 0x54,
    KeyU = 0x55,
    KeyV = 0x56,
    KeyW = 0x57,
    KeyX = 0x58,
    KeyY = 0x59,
    KeyZ = 0x5A,
    KeyOpenBracket = 0x5B,
    KeyBackSlash = 0x5C,
    KeyCloseBracket = 0x5D,
    KeyNumPad0 = 0x60,
    KeyNumPad1 = 0x61,
    KeyNumPad2 = 0x62,
    KeyNumPad3 = 0x63,
    KeyNumPad4 = 0x64,
    KeyNumPad5 = 0x65,
    KeyNumPad6 = 0x66,
    KeyNumPad7 = 0x67,
    KeyNumPad8 = 0x68,
    KeyNumPad9 = 0x69,
    KeyMultiply = 0x6A,
    KeyAdd = 0x6B,
    KeySeparator = 0x6C,
    KeySubtract = 0x6D,
    KeyDecimal = 0x6E,
    KeyDivide = 0x6F,
    KeyF1 = 0x70,
    KeyF2 = 0x71,
    KeyF3 = 0x72,
    KeyF4 = 0x73,
    KeyF5 = 0x74,
    KeyF6 = 0x75,
    KeyF7 = 0x76,
    KeyF8 = 0x77,
    KeyF9 = 0x78,
    KeyF10 = 0x79,
    KeyF11 = 0x7A,
    KeyF12 = 0x7B,
    KeyDelete = 0x7F,
    KeyNumLock = 0x90,
    KeyScrollLock = 0x91,
    KeyPrintScreen = 0x9A,
    KeyInsert = 0x9B,
    KeyHelp = 0x9C,
    KeyMeta = 0x9D,
    KeyBackQuote = 0xC0,
    KeyQuote = 0xDE,
    KeyFinal = 0x18,
    KeyConvert = 0x1C,
    KeyNonConvert = 0x1D,
    KeyAccept = 0x1E,
    KeyModeChange = 0x1F,
    KeyKana = 0x15,
    KeyKanji = 0x19,
    KeyUndefined = 0x0,





def get_key_state(key: KeyCode) -> bool:
    """
    #todo docs
    :param key:
    :return:
    """
    return KIPR.get_key_state(key) == 1


def get_left_button() -> bool:
    """
    #todo docs
    :return:
    """
    return KIPR.get_mouse_left_button() == 1


def get_mouse_middle_button() -> bool:
    """
    #todo docs
    :return:
    """
    return KIPR.get_mouse_middle_button() == 1


def get_right_button() -> bool:
    """
    #todo docs
    :return:
    """
    return KIPR.get_mouse_right_button() == 1
