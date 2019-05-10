def left(string, number):
    string = str(string)
    string = string[:number]
    return string


def right(string, number):
    string = str(string)
    string = string[len(string) - number:]
    return string


def left_right(string, lnum, rnum):
    string = str(string)
    string = left(string, lnum)
    string = right(string, rnum)
    return string


def l_trim(string, number):
    string = str(string)
    string = string[number:]
    return string


def r_trim(string, number):
    string = str(string)
    string = string[:len(string) - number]
    return string


def l_rtrim(string, l, r):
    string = str(string)
    string = string[l:]
    string = string[:len(string) - r]
    return string
