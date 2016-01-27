#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
The International Civil Aviation Organization (ICAO) alphabet assigns code
words to the letters of the English alphabet acrophonically (Alfa for A, Bravo
for B, etc.) so that critical combinations of letters (and numbers) can be
pronounced and understood by those who transmit and receive voice messages by
radio or telephone regardless of their native language, especially when the
safety of navigation or persons is essential. Here is a Python dictionary
covering one version of the ICAO alphabet:

    d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo',
        'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 
        'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 
        'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 
        'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 
        'z':'zulu'}
            
Your task in this exercise is to write a procedure speak_ICAO() able to 
translate any text (i.e. anystring) into spoken ICAO words. You need to 
import at least two libraries: os and time. On a mac, you have access to the 
system TTS (Text-To-Speech) as follows: os.system('say ' + msg), where msg is 
the string to be spoken. (Under UNIX/Linux and Windows, something similar 
might exist.) Apart from the text to be spoken, your procedure also needs 
to accept two additional parameters: a float indicating the length of the 
pause between each spoken ICAO word, and a float indicating the length 
of the pause between each word spoken.
"""
import os
import time

d = {
    'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo',
    'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo',
    'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 
    'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform', 
    'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 'z':'zulu'
}

def speak_ICAO(string):
    for char in string.lower():
        for k, v in d.items():
            if char == k:
                os.system('say ' + v)
                time.sleep(.5)

if __name__ == "__main__":
    speak_ICAO("TEST")




