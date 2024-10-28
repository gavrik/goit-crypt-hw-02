def create_permutation(secret_key):
    return sorted(range(len(secret_key)), key=lambda k: secret_key[k])

def permutation_encrypt(secret_key, text):
    permutation = create_permutation(secret_key)
    bsize = len(secret_key)
    cipher_text = ''
    for i in range(0, len(text), bsize):
        cblock = text[i:i + bsize]
        if len(cblock) < bsize:
            cblock += ' ' * (bsize - len(cblock))
        encrblock = ''.join(cblock[j] for j in permutation)
        cipher_text += encrblock
    return cipher_text

def permutation_decrypt(secret_key, cipher_text):
    permutation = create_permutation(secret_key)
    rev_permutation = sorted(range(len(permutation)), key=lambda k: permutation[k])
    bsize = len(secret_key)
    decipher_text = ''
    for i in range(0, len(cipher_text), bsize):
        cblock = cipher_text[i:i + bsize]
        decrblock = ''.join(cblock[j] for j in rev_permutation)
        decipher_text += decrblock
    return decipher_text


if __name__ == "__main__":
    secret_key = ('SECRET', 'CRYPTO')
    fp = open("original.txt", 'r')

    print('Кодування одним ключем')
    cipher_text = permutation_encrypt(secret_key[0], fp.read().replace("\n", ""))
    print(cipher_text)
    print('========')
    decipher_text = permutation_decrypt(secret_key[0], cipher_text)
    print(decipher_text)
    fp.close()

    fp = open("original.txt", 'r')
    print('\n\n\nПодвійне кодування')
    cipher_text = fp.read().replace("\n", "")
    for c in secret_key:
        cipher_text = permutation_encrypt(c, cipher_text)
    print(cipher_text)
    print('========')
    decipher_text = cipher_text
    for c in reversed(secret_key):
        decipher_text = permutation_decrypt(c, decipher_text)
    print(decipher_text)
