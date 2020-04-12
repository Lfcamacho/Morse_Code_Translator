def alphabet(letter):

    morse = {
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....": "H",
        "..": "I",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "--": "M",
        "-.": "N",
        "---": "O",
        ".--.": "P",
        "--.-": "Q",
        ".-.": "R",
        "...": "S",
        "-": "T",
        "..-": "U",
        "...-": "V",
        ".--": "W",
        "-..-": "X",
        "-.--": "Y",
        "--..": "Z"
    }

    if letter in morse:
        return morse[letter]
    else:
        return "no"

def decoder(counter,phrase,code,words):

    global number
    
    a = ""
    j = 1
    b = ""

    for j in range(1,6):

        if counter+j < len(code):
            b = b + (code[counter+j])
            a = alphabet(b)

            if a != "no":
                phrase2 = phrase
                phrase = phrase + a

                if (counter+j) == (len(code)-1):
                    words.append(phrase)
                    number = number + 1

                decoder(counter+j,phrase,code,words)
            
            phrase = phrase2

    return words

def morsedecoder(code):

    global number

    counter=-1
    number = 0
    phrase = ""
    words = []

    return decoder(counter,phrase,code,words)    
    


#code = input("Insert morse code: ")
#a = morsedecoder(".-.-.-.-.---.-.--.--.-.")

#for x in a:
 #   print (x)

#print("\nNumber of options: ",number)