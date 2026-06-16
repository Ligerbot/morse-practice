import pymorsecode.pymorsecode
callsign = input("Callsign: ")
wpm = input("WPM (5-25): ")
morse = pymorsecode.pymorsecode.MorseCode(callsign, wpm=20)
morse.play_morse()
morse = pymorsecode.pymorsecode.MorseCode(callsign, wpm=int(wpm))
while True:
	text = input("> ")
	morse.play_morse(text)
