letters = list(map(chr, range(ord("a"), ord("z"))))
vowels = "eyuioau"
consonants = list(filter(lambda l : l not in vowels, letters))