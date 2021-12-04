code =     ['g', 'å', '∫', 'ç', '∂', '´', 'ƒ', '©', '˙', 'ˆ', '∆', '˚', '¬' 'µ', '˜', 'ø', 'π', 'œ', '®', 'ß', '†', '¨', '√','∑', '≈', '¥', 'Ω']
alphabet = ['g', 'a', 'b', 'c' ,'d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def decrypt(encrypted):
    string = ""
    for i in encrypted:
        string += alphabet[code.index(i)]
        print(i)
        print(alphabet[code.index(i)])
    print(string)

decrypt(input("What do you want to decypher? "))
