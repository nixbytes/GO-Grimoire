# Caesar.py Cipher
# from Cracking the code book
# import paperclip
# The string to be encrypted/decrypted

message = '"Egw3EkivE1pw5EjtiksEq1E5pq2mEj7Eizo3umv2,"E1iqlENqtj7,E"j32E7w3E5qttEvm4mzEkwv4qvkmEumH"'

key = 8

# The encryption/decryption key

# whether the programing encrypts of decrypts:

mode = 'decrypt'

# Every possible symbol that can be encrypted:

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Store the  encrypted/decrypted form of the message:

translated = ''

for symbol in message:

    # Note: Only symbols in the SYMBOLS string can be encrypted/decrypted.

    if symbol in SYMBOLS:

        symbolIndex = SYMBOLS.find(symbol)

        # Perform encryption/decryption:
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key
        # Handle wraparound, if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
    # Append the symbol without encrypting/decrypting
        translated = translated + symbol

# Output the translated string

print(translated)
#pyperclip.copy(translated)



