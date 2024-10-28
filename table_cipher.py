def create_table(secret_key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    secret_key = "".join(sorted(set(secret_key), key = secret_key.index))
    mkey = secret_key + alphabet
    key_table = "".join(sorted(set(mkey), key = mkey.index))
    return [list(key_table[i:i+5]) for i in range(0,25,5)]

def find_char_position(key_table, char):
    for row in range(5):
        for col in range(5):
            if key_table[row][col] == char:
                return (row, col)
    return None

def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "").replace("\n","")
    if len(text) %2 != 0:
        text += 'X'
    return text

def encrypt_pair(table, char1, char2):
    pos1 = find_char_position(table, char1)
    pos2 = find_char_position(table, char2)
    if pos1 is None or pos2 is None:
        print("Not a char")
        print(char1, char2)
        return (char1, char2)
    if pos1[0] == pos2[0]:
        return (table[pos1[0]][(pos2[1]+1)%5], table[pos2[0]][(pos1[1]+1)%5])
    elif pos1[1] == pos2[1]:
        return (table[(pos1[0]+1)%5][pos2[1]], table[(pos2[0]+1)%5][pos1[1]])
    else:
        return (table[pos1[0]][pos2[1]], table[pos2[0]][pos1[1]])

def decrypt_pair(table, char1, char2):
    pos1 = find_char_position(table, char1)
    pos2 = find_char_position(table, char2)
    if pos1 is None or pos2 is None:
        print("Not a char")
        print(char1, char2)
        return (char1, char2)
    if pos1[0] == pos2[0]:
        return (table[pos1[0]][(pos2[1]-1)%5], table[pos2[0]][(pos1[1]-1)%5])
    elif pos1[1] == pos2[1]:
        return (table[(pos1[0]-1)%5][pos2[1]], table[(pos2[0]-1)%5][pos1[1]])
    else:
        return (table[pos1[0]][pos2[1]], table[pos2[0]][pos1[1]])

def encrypt(text, secret_key):
    key_table = create_table(secret_key)
    text = prepare_text(text)
    #print(key_table)
    #print(text)
    encrypted = ""
    for c in range(0, len(text), 2):
        chars = encrypt_pair(key_table, text[c], text[c+1])
        encrypted += chars[0] + chars[1]
    return encrypted

def decrypt(text, secret_key):
    key_table = create_table(secret_key)
    decrypt = ""
    for c in range(0, len(text), 2):
        chars = decrypt_pair(key_table, text[c], text[c+1])
        decrypt += chars[0] + chars[1]
    return decrypt

if __name__ == "__main__":
    secret_key = "MATRIX"
    #key_table = create_table(secret_key)
    #print(key_table[0])
    #print(key_table[1])
    #print(key_table[2])
    #print(key_table[3])
    #print(key_table[4])
    #print(find_char_position(key_table, 'H'))
    #print(find_char_position(key_table, 'D'))
    #enc = encrypt_pair(key_table, 'H', 'E')
    #print(enc)
    #enc = encrypt('hello world', secret_key)
    #print(enc)
    #denc = decrypt(enc, secret_key)
    #print(denc)
    with open('original.txt', 'r') as fp:
        enc = encrypt(fp.read(), secret_key)
        print(enc)
        print("\n=============\n")
        denc = decrypt(enc, secret_key)
        print(denc)
