# the llm can barely decode morse even with a cheet sheet. a top priority for bug fixing it making it so that the morse code sent in by the user is decoded to text so the llm can understand it.

#chat with an LLM using morse code!
from playsound import playsound
import pymorsecode.pymorsecode
import ollama

playownmessage = True #if set to true it beeps your message first

print("Morse code chatbot for practicing morse code")
print("(Ignore any alsa related warnings below, they are unimportant as long as you have a working speaker")
conversation = []
conversation.append({"role": "system", "content": "You are a ham radio person who does morse code. Your callsign is abcd. All answers must be short answers in ENGLISH. The user will send you TEXT. Reply with a short text sentence. Only use common characters, no periods or commands, etc. Your replies must be short and concise, using only common words. You are encouraged to use common ham radio morse code terms like QSL, especialy if the user sends them to you. It CANNOT BE RANDOM CHARACTERS. REPLY WITH WORDS. NO ABBREVIATIONS. Do not ever use dashes or emojis. You don't need to echo what the user says. You are only allowed to answer in lowercase letters. No punctuation marks of any kind. No apostrophes either. No double quotes or single quotes are ever allowed. Avoid sending messages more than 3 words long if possible."})
#conversation.append({"role": "system", "content": "Here are the following Q codes for ham rado you can use: QRA = What is the name of your station: QRB = How far are you away from my station QRG = What is my exact frequency QRK = What is the intelligibility of my signals QRL = Are you busy QRM = Man Made Interference QRN = Natural interference e.g lightning QRO = Should I increase transmitting power? QRP = Should I decrease transmitting power? QRQ = Should I send faster? QRS = Should I send slower? QRT = Should I stop transmitting? QRV = Are you ready? QSL = I confirm that I recieved that"})
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

conversation.append({"role": "system", "content": "Morse code cheatsheet: " + str(cheatsheet)})

def llamaHandler(text):
#	print("Decoded: " + text)
	global conversation
	client = ollama.Client()
	conversation.append({"role": "user", "content": text})
	response = client.chat(
		model="llama3:latest",
		messages=conversation
	)
	output = response['message']['content'].replace(" ", "   ").replace("'", "")
	conversation.append({"role": "assistant", "content": output})
#	print("Output of llm: " + output)
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
			morse.save_wav("tmp.wav", text) #this line is meant to be outside of the if so that it validates that it is only dots and dashes
			if playownmessage:
				playsound("tmp.wav")
			print("Chatbot replying...")
			morse.sound_to_morse("tmp.wav")
			output = llamaHandler(morse.morse_text)
#			print(output)
			morse = pymorsecode.pymorsecode.MorseCode(output, wpm=int(wpm))
			morse.save_wav("tmp.wav")
			playsound("tmp.wav")
		except Exception as e:
			print("Did you make a typo?")
