import itertools
import sys

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def words_set():
    words = set()
    with open('sowpods.txt', 'r') as words_file:
        for l in words_file:
            words.add(l.rstrip().lower())
    return list(words)

def get_letters():
    letters = sys.argv[1] if len(sys.argv) > 1 else input("Please enter letters: ")
    return list(letters)

def possible_words(letters):
    words = set()
    for i in range(1, len(letters)+1):
        for word in itertools.combinations(letters, i):
            words.add(''.join(word).lower())
    return list(words)

def are_words(possible_words, actual_words):
    words = set()
    for word in possible_words:
        if word in actual_words:
            words.add(word)
    return list(words)

def score_words(words):
    scored_words = {}
    for word in words:
        score = 0
        for letter in word:
            score += scores[letter]
        scored_words[word] = score
    return scored_words

def print_scores_words(scored_dict):
    sorted_keys = sorted(scored_dict, key=scored_dict.__getitem__, reverse=True)
    for k in sorted_keys:
        print(scored_dict[k], '\t', k)

if __name__ == '__main__':
    all_words = words_set()
    rack_letters = get_letters()
    maybe_words = possible_words(rack_letters)
    real_words = are_words(maybe_words, all_words)
    scores = score_words(real_words)
    print_scores_words(scores)
