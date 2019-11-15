import sys 
    
def encode(string, rotation):
    encoded = ''
    for item in string:
        c = ord(item) + rotation
        if ord(item) >= 65 and ord(item) <= 90: #if item is uppercase
            c -= 65
            c %= 26
            c += 65
        elif ord(item) >= 97 and ord(item) <= 122:
            c -= 97
            c %= 26
            c += 97
        else: 
            c = ord(item)

        encoded += chr(c)
    return encoded

def main():
    if len(sys.argv) != 2:
        print("Error")
        sys.exit(1)

    k = int(sys.argv[1]) % 26

    m = input("plainttext: ")
    encoded_input = encode(m, k)
    decoded_input = encode(encoded_input, -k)


    print("ciphertext: ", end ='')
    print(encoded_input)

    print("decoded: ", end ='')
    print (decoded_input)

if __name__ == "__main__":
    main()


