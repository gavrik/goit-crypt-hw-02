def generate_long_key(key, len_text):
    key = list(key)
    if len_text == len(key):
        return key
    else:
        for i in range(len_text - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def veginere_encode(key, text):
    fp = open('cipher_text.txt', 'w')
    key_long = generate_long_key(key, len(text))
    for idx in range(len(text)):
        c = (ord(text[idx]) + ord(key_long[idx])) % 26
        c += ord('A')
        fp.write(chr(c))

def veginere_decode(key, cipher_text):
    fp = open('decipher_text.txt', 'w')
    key_long = generate_long_key(key, len(cipher_text))
    for idx in range(len(cipher_text)):
        c = (ord(cipher_text[idx]) - ord(key_long[idx]) + 26) % 26
        c += ord('A')
        fp.write(chr(c))

if __name__ == "__main__":
    key = 'CRYPTOGRAPHY'
    with open('original.txt', 'r') as fp:
        veginere_encode(key, fp.read().replace("\n",""))

    with open('cipher_text.txt', 'r') as fp:
        veginere_decode(key, fp.read())
