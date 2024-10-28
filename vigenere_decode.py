from codecs import encode
from math import factorial
from cryptonita.scoring import scoring
from cryptonita.scoring import key_length_by_ic
from cryptonita import B
from cryptonita.conv import transpose
from cryptonita.scoring.freq import etaoin_shrdlu
from cryptonita.attacks import freq_attack
from cryptonita.attacks import brute_force
from cryptonita.scoring import all_ascii_printable
from cryptonita.fuzzy_set import join_fuzzy_sets
from cryptonita.fuzzy_set import len_join_fuzzy_sets

def find_key_len(text):
    gklength = scoring(
        text,
        space=range(5, 25),
        score_func=key_length_by_ic,
        min_score=0.025,
    )
    print(gklength)
    return gklength.most_likely()

def vigenere_decode(text):
    most_common_pbytes = etaoin_shrdlu()
    ntop_most_common_cbytes = 1
    key_len = find_key_len(text)
    print("Possible key len: ", key_len)
    cblock = text.nblocks(key_len)
    cblock = transpose(cblock, allow_holes=True)
    #print("", cblock)
    guess_keys = []
    for c in cblock:
        guess_keys.append(freq_attack(c, most_common_pbytes, ntop_most_common_cbytes))
    print(len_join_fuzzy_sets(guess_keys))
    print("Possible keys: ", len(guess_keys))
    for i, c in enumerate(cblock):
        g_key = guess_keys[i]
        ref = brute_force(c,
            score_func = all_ascii_printable,
            key_space=g_key,
            min_score=0.01)
        guess_keys[i] = ref
    gkstream = join_fuzzy_sets(guess_keys, cut_off=1024, j=B(''))
    #print(gkstream)
    print("Possible combination:", len_join_fuzzy_sets(guess_keys))

if __name__ == "__main__":
    s = B(open('cipher_text.txt'))
    vigenere_decode(s)
