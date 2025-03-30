def is_in_L1(word):
    if '1' in word:
        i = word.index('1')
        j = len(word) - i 
        return i > j
    return False

def is_in_L2(word):
    i = word.count('a')
    j = word.count('b')
    return i <= j and 'c' not in word

def is_in_L3(word):
    n_a = word.count('a')
    n_b = word.count('b')
    n_c = word.count('c')
    return n_a == n_b == n_c > 0 

test_words = ["000111", "aaabb", "aaabbbccc", "011", "abb", "abc"]
for word in test_words:
    print(f"{word} in L1: {is_in_L1(word)}")
    print(f"{word} in L2: {is_in_L2(word)}")
    print(f"{word} in L3: {is_in_L3(word)}")
