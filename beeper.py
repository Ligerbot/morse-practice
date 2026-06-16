from playsound import playsound
import pymorsecode.pymorsecode

#feel free to change this
autoid = False #if using the ham radio bands then you can use this to automatically send your callsign before transmitting. a callsign is not required for this software though (morse code isn't restricted to ham radio)
extraspacing = True #this option is recommended if you are learning

#TODO: fix the following feature:
slashseperation = False #seperate letters with a space and words with a / and no space if this is on

if autoid:
	callsign = input("Callsign: ")
	wpm = input("WPM (5-25): ")
	morse = pymorsecode.pymorsecode.MorseCode(callsign + " is learning cw", wpm=20)
	morse.play_morse()
else:
	wpm = input("WPM (5-25): ")
	morse = pymorsecode.pymorsecode.MorseCode("a", wpm=int(wpm))
while True:
	text = input("> ")
	if slashseperation:
		text.replace("/", "  ")
	if extraspacing and not slashseperation:
		text.replace(" ", "  ")
	morse.save_wav("tmp.wav", text)
	playsound("tmp.wav")
