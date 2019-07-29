word = str(raw_input("Word: "))

if word[-3:] == "ife":
        print(word[:-3] + "ives")
else:
        print(word + "s")

if word[-3:] == "ush":
        print(word[:-3] + "ushes")
else:
        print(word + "s")

if word[-2:] == "us":
    print(word[:-2] + "i")
else:
    print(word + "i")
