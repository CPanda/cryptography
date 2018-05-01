def atbash(text):
  text = text.lower()
  switcher = {
        'a': "z",
        'b': "y",
        'c': "x",
        'd': "w",
        'e': "v",
        'f': "u",
        'g': "t",
        'h': "s",
        'i': "r",
        'j': "q",
        'k': "p",
        'l': "o",
        'm': "n",
        'n': "m",
        'o': "l",
        'p': "k",
        'q': "j",
        'r': "i",
        's': "h",
        't': "g",
        'u': "f",
        'v': "e",
        'w': "d",
        'x': "c",
        'y': "b",
        'z': "a"
    }
  newText = ""
  for c in text:
    if c!=' ' and c!=',' and c!='.' and c!='!' and c!='?' and c!='/':
      newText += switcher.get(c, 'Invalid character')
    else:
      newText += c
  return newText
