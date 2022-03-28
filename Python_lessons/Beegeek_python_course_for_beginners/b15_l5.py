def cesar(text):
    words = text.replace('!', '').replace('"', '').replace('.', '').replace(',', '').split()
    for word in words:
        rword = ''
        for symbol in word:
            rword += sdvig(symbol, len(word))
        text = text.replace(word, rword, 1)
    return text


def sdvig(symb, num):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    symb_index = abc.find(symb.lower())
    if symb in '1234567890 .,?"!\'-'' ':
        return symb
    elif symb_index + num > 25:
        if symb.lower() == symb:
            return abc[symb_index + num - 26]
        else:
            return abc[symb_index + num - 26].upper()
    else:
        if symb.lower() == symb:
            return abc[symb_index + num]
        else:
            return abc[symb_index + num].upper()


text = input()
print(cesar(text))
