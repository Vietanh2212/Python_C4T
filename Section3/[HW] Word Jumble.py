import random
words = ["lmaoez", "metaphoric", "modulus", "import"]
for i in range(len(words)):
    word = random.choice(words)
    chars = list(word)
    random.shuffle(chars)
    print(*chars)
    if input("Your answer: ") == word:
        print("HURA")
    else:
        print("u sucks")
