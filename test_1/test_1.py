"""Morse Code Translator"""

LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}

MORSE_TO_LETTER = {
    morse: letter
    for letter, morse in LETTER_TO_MORSE.items()
}


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе

    >>> encode('SOS') # doctest: -NORMALIZE_WHITESPACE, -REPORT_NDIFF
    '... --- ...'

    >>> encode('SAVE, OUR, SOULS')
    '... .- ...- . --..-- --- ..- .-. --..-- ... --- ..- .-.. ...'

    >>> encode('SAVE/OUR/SOULS') # doctest: -NORMALIZE_WHITESPACE
    '... .- ...- . -..-. --- ..- .-. -..-. ... --- ..- .-.. ...'

    >>> encode('SAVE OUR SOULS') # doctest: -REPORT_NDIFF
    '... .- ...- . --- ..- .-. ... --- ..- .-.. ...'

    >>> encode('SAVE OUR SOULS') # doctest: -NORMALIZE_WHITESPACE
    '... .- ...- . --- ..- .-. ... --- ..- .-.. ...'


    >>> encode('123') # doctest: -NORMALIZE_WHITESPACE, -REPORT_NDIFF
    '.---- ..--- ...--'

    >>> encode('') # doctest: -NORMALIZE_WHITESPACE, -REPORT_NDIFF
    ''

    >>> encode('#%') # doctest: -NORMALIZE_WHITESPACE, -REPORT_NDIFF
    Traceback (most recent call last):
        ...
    KeyError: '#'

    >>> encode('$!@') # doctest: -NORMALIZE_WHITESPACE, -REPORT_NDIFF
    Traceback (most recent call last):
        ...
    KeyError: '$'

    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)
