# -*- coding: utf-8 -*-

vocals = [
          "a","e","i","o","u",
          "á","é","í","ó","ú",
          "ä","ë","ï","ö","ü",
          "â","ê","î","ô","û",
          "à","è","ì","ò","ù",
          ]

def vocal_count(text):
    global vocals
    count = 0
    try:
        if type(text) is str:
            text = text.lower()
            for letter in text:
                if letter in vocals:
                    count += 1
            return count
        else:
            raise Exception("type error")
    except:
        print("El parámetro de entrada no es de tipo string")

def vocal_replace(text):
    global vocals
    replace = ""
    try:
        if type(text) is str:
            for letter in text:
                newvocal = ''
                if letter.lower() in vocals:
                    index = vocals.index(letter.lower())
                    if index in [4,9,14,19,24]:
                        newvocal = vocals[index - 4]
                    else:
                        newvocal = vocals[index + 1]
                    if letter.isupper():
                        replace += newvocal.upper()
                    else:
                        replace += newvocal
                else:
                    replace += letter
            return replace
        else:
            raise Exception("type error")
    except:
        print("El parámetro de entrada no es de tipo string")

if __name__ == "__main__":
    import doctest
    doctest.testfile('testA1.txt')
