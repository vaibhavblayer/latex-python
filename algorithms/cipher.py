m = input('message to be ciphered : ')

ciphered = ''

i = len(m) - 1


while i>=0:
	ciphered = ciphered + m[i]
	i = i -1


print(ciphered)


import pyperclip

key = 13

mode = input('encrypt or decrypt : ')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

translated = ''

for symbol in m:
	if symbol in SYMBOLS:
		symbolIndex = SYMBOLS.find(symbol)

		if mode == 'encrypt':
			translatedIndex = symbolIndex + key
		elif mode == 'decrypt':
			translatedIndex = symbolIndex - key

		if translatedIndex >= len(SYMBOLS):
			translatedIndex = translatedIndex - len(SYMBOLS)
		elif translatedIndex < 0:
			translatedIndex = translatedIndex + len(SYMBOLS)

		translated = translated + SYMBOLS[translatedIndex]
	else:
		translated = translated + symbol


print(translated)
pyperclip.copy(translated)




