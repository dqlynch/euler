import math

def load(filename):
    with open(filename) as f:
        file = f.read()
        words = [word.strip('" ') for word in file.split(',')]
    return words

def encode(word, first_letter='A'):
    # Bitwise encoding of letter count in each word
    # Assume max number of repeated letters in a word <= 16 --> use 4 bits/letter
    # => 13 bytes
    encoding = 0
    for letter in word:
        pos = ord(letter) - ord(first_letter)
        encoding += 0b0001 << pos * 4
    return encoding

def find_anagrams(words, first_letter='A'):
    anagrams = {}
    for word in words:
        encoding = encode(word, first_letter=first_letter)
        if anagrams.get(encoding):
            anagrams[encoding].append(word)
        else:
            anagrams[encoding] = [word]

    anagrams_groups = []
    for encoding, group in anagrams.items():
        if len(group) > 1:
            anagrams_groups.append(group)
    return anagrams_groups


def find_squares(n):
    return [str(i**2) for i in range(1, math.ceil(math.sqrt(n)))]

#def joint_encode(word):
#    letter_counts = {}
#    for letter in word:
#        if letter_counts.get(letter):
#            letter_counts[letter] += 1
#        else:
#            letter_counts[letter] = 1
#    counts = [count for _, count in letter_counts.items()]
#    counts.sort(reverse=True)
#
#    encoding = 0
#    for i, count in enumerate(counts):
#        encoding += 0b0001 * count << i * 4
#    return encoding


def common_form(word):
    increment = 'A'
    letter_map = {}
    common_word = ''
    for letter in word:
        if not letter_map.get(letter):
            letter_map[letter] = increment
            increment = chr(ord(increment) + 1)
        common_word += str(letter_map.get(letter))
    return common_word, letter_map


def convert(word, letter_map):
    converted = ''
    for letter in word:
        converted += letter_map[letter]
    return converted


if __name__=='__main__':
    words = load("words.txt")
    words.sort(reverse=True)
    # Max length of word is 14 letters
    anagrams = find_anagrams(words)

    # Longest anagram is INTRODUCE/REDUCTION = 9 letters, so only have to find
    # squares up to 10 digits => 1000000000
    squares = find_squares(1000000000)
    squares.reverse()

    # Find squares with anagrams
    square_anagrams = find_anagrams(squares, first_letter='0')


    # Jointly encode squares and anagrams
    common_word_anagrams = {}
    for group in anagrams:
        for word in group:
            common_word, letter_map = common_form(word)

            if common_word not in common_word_anagrams:
                common_word_anagrams[common_word] = []
            for anagram in group:
                # TODO need to preserve the letter mapping from first anagram
                if anagram != word:
                    common_anagram = convert(anagram, letter_map)
                    common_word_anagrams[common_word].append(common_anagram)
    print(common_word_anagrams)

    for group in square_anagrams:
        for square in group:
            common_square, letter_map = common_form(square)

            if common_square in common_word_anagrams:

                for square_anagram in group:
                    if square_anagram != square:
                        common_square_anagram = convert(square_anagram, letter_map)
                        if common_square_anagram in common_word_anagrams[common_square]:
                            print(square)
                            print(square_anagram)
                            print(common_square)
                            print(common_square_anagram)

                            #exit()
