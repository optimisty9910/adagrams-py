from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

SCORE_CHART = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
}

def draw_letters():
    pool = []
    for letter, quantity in LETTER_POOL.items():
        pool.extend([letter] * quantity)

    letters = []

    while len(letters) < 10:
        current_index = randint(0, len(pool) - 1)
        letter = pool.pop(current_index)
        letters.append(letter)

    return letters    

def list_to_dict(letters):
    letter_dict = {}

    for letter in letters:
        upper_letter = letter.upper()
        if upper_letter not in letter_dict:
            letter_dict[upper_letter] = 1
        else:
            letter_dict[upper_letter] += 1

    return letter_dict



def uses_available_letters(word, letter_bank):
    if len(word) > len(letter_bank):
        return False
    
    letter_dict = list_to_dict(letter_bank)
    word_dict = list_to_dict(word)
    
    for letter, quantity in word_dict.items():
        if (letter not in letter_dict) or (quantity > letter_dict[letter]):
            return False

    return True


def score_word(word):
    score = 0

    if 7 <= len(word) <= 10:
        score += 8

    for letter in word:
        upper_letter = letter.upper()
        for point, letters in SCORE_CHART.items():
            if upper_letter in letters:
                score += point
    
    return score

def get_highest_word_score(word_list):
    current_word = ""
    current_score = 0

    for word in word_list:
        score = score_word(word)
        if score > current_score:
            current_word = word
            current_score = score
        elif (score == current_score) and (len(current_word) != 10):
            if len(word) < len(current_word) or len(word) == 10:
                current_word = word

    return (current_word, current_score)
