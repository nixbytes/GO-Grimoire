# Caesar Cipher Hacker

# https:// www.nostarch.com/ crackingcodes/ (BSD Licensed)

message = "guv6Jv6Jz!J6rp5r7Jzr66ntrM"

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

# Loop for every possible outcome

for key in range(len(SYMBOLS)):

    # It is important to set translated to the blank string so that the

    translated = ""

    # most of the code is the same as Caesar

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Handle wraparound, if needed:
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]

        else:
            # Append the symbols
            translated = translated + symbol

    print("Key #%s: %s" % (key, translated))
