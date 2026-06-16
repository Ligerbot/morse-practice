from playsound import playsound
import pymorsecode.pymorsecode

#feel free to change this
autoid = False

if autoid:
	callsign = input("Callsign: ")
	wpm = input("WPM (5-25): ")
	morse = pymorsecode.pymorsecode.MorseCode(callsign, wpm=20)
	morse.play_morse()
else:
	wpm = input("WPM (5-25): ")
morse = pymorsecode.pymorsecode.MorseCode(callsign, wpm=int(wpm))
while True:
	text = input("> ")
	morse.save_wav("tmp.wav", text)
	playsound("tmp.wav")
