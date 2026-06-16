#chat with an LLM using morse code!
from playsound import playsound
import pymorsecode.pymorsecode
import ollama
print("Morse code chatbot for practicing morse code")
print("(Ignore any alsa related warnings below, they are unimportant as long as you have a working speaker")
conversation = []
conversation.append({"role": "system", "content": "You are a morse code practice bot. Your callsign is KO6BOT. All answers must be short answers in ENGLISH. The user will send you dots and dashes. Decode those yourself and then reply with a short text sentence NOT IN MORSE CODE. Only use common characters, no periods or commands, etc. Your replies must be short and concise, using only common words. Do not use common ham radio morse code terms like QSL unless the user sends them to you. It CANNOT BE RANDOM CHARACTERS. REPLY WITH WORDS. NO ABBREVIATIONS. Do not ever use dashes or emojis. You don't need to echo what the user says. Instead, try to have a conversation with the user. You are only allowed to answer in lowercase letters. No punctuation marks of any kind. No apostrophes either"})
cheatsheet = [
"a = .-",
"b = -...",
"c = -.-.",
"d = -..",
"e = .",
"f = ..-.",
"g = --.",
"h = ....",
"i = ..",
"j = .---",
"k = -.-",
"l = .-..",
"m = --",
"n = -.",
"o = ---",
"p = .--.",
"q = --.-",
"r = .-.",
"s = ...",
"t = -",
"u = ..-",
"v = ...-",
"w = .--",
"x = -..-",
"y = -.--",
"z = --..",
"1 = .----",
"2 = ..---",
"3 = ...--",
"4 = ....-",
"5 = .....",
"6 = -....",
"7 = --...",
"8 = ---..",
"9 = ----.",
"0 = -----",
". = .-.-.-",
", = --..--",
"? = ..--.."
]
def llamaHandler(text):
	global conversation
	client = ollama.Client()
	conversation.append({"role": "user", "content": text})
	response = client.chat(
		model="llama3:latest",
		messages=conversation
	)
	output = response['message']['content']
	conversation.append({"role": "assistant", "content": output})
	return output

wpm = input("WPM (5-25): ")
morse = pymorsecode.pymorsecode.MorseCode("a", wpm=int(wpm))
output = "No output yet"
while True:
	text = input("> ")
	if text == "/show":
		print(output)
	elif text == "/help":
		print("Morse code chatbot practice")
		print("An LLM will reply to any morse code message entered with morse code so you can practice decoding morse.")
		print("Available commands: /show (shows previous message from bot), /exit (exits the program gracefully (ctrl+c works too!)), /cheat (prints a cheat sheet for morse code), /context (prints out the whole entire conversation so far)")
	elif text == "/cheat":
		print("Morse code cheat sheet")
		for character in cheatsheet:
			print(character)
	elif text == "/context":
		print("Conversation so far:")
		for a in conversation:
			print(str(a))
#		print(str(conversation))
	elif text == "/exit":
		print("Thanks for using my morse code trainer program")
		exit(0)
	else:
		try:
			morse.save_wav("tmp.wav", text)
			playsound("tmp.wav")
			output = llamaHandler(text)
		#	print(output)
			morse = pymorsecode.pymorsecode.MorseCode(output, wpm=int(wpm))
			morse.save_wav("tmp.wav")
			playsound("tmp.wav")
		except Exception as e:
			print("Did you make a typo?")
