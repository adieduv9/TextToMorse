MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
    '/': '-..-.',  '(': '-.--.',  ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-',  '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
    '@': '.--.-.', "'": '.----.',
}

def text_to_morse(text):
    """
    Convert plain text to Morse code.
    Words are separated by ' / ', letters by spaces.
    """
    if not text or not text.strip():
        return None, "Input cannot be empty."

    text = text.upper().strip()
    result_words = []

    for word in text.split():
        morse_letters = []
        for char in word:
            if char in MORSE_CODE:
                morse_letters.append(MORSE_CODE[char])
            else:
                return None, f"Character '{char}' is not supported in Morse code."
        result_words.append(' '.join(morse_letters))

    return ' / '.join(result_words), None
