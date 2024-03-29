import pytest
from morse import decode


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


@pytest.mark.parametrize(
    'morse_text, result',
    [
        ('... --- ...', 'SOS'),
        ('... .- ...- . --- ..- .-. ... --- ..- .-.. ...', 'SAVEOURSOULS'),
        ('.---- ..--- ...--', '123'),
        (
                '... .- ...- . --..-- --- ..- .-. --..-- ... --- ..- .-.. ...',
                'SAVE, OUR, SOULS'
         )
    ],
)
def test_decode(morse_text, result):
    assert decode(morse_text) == result
