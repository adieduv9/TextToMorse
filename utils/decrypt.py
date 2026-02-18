MORSE_TO_TEXT = {
    '.-': 'A',    '-...': 'B',  '-.-.': 'C',  '-..': 'D',
    '.': 'E',     '..-.': 'F',  '--.': 'G',   '....': 'H',
    '..': 'I',    '.---': 'J',  '-.-': 'K',   '.-..': 'L',
    '--': 'M',    '-.': 'N',    '---': 'O',   '.--.': 'P',
    '--.-': 'Q',  '.-.': 'R',   '...': 'S',   '-': 'T',
    '..-': 'U',   '...-': 'V',  '.--': 'W',   '-..-': 'X',
    '-.--': 'Y',  '--..': 'Z',

    '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9',

    '.-.-.-': '.', '--..--': ',', '..--..': '?', '-.-.--': '!',
    '-..-.': '/', '-.--.': '(',  '-.--.-': ')', '.-...': '&',
    '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+',
    '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$',
    '.--.-.': '@', '.----.': "'",
}

def morse_to_text(morse):
    """
    Convert Morse code to plain text.
    Words separated by ' / ', letters by spaces.
    """
    if not morse or not morse.strip():
        return None, "Input cannot be empty."

    morse = morse.strip()
    result_words = []

    # Split on word separator ' / '
    words = morse.split(' / ')

    for word in words:
        letters = word.strip().split()
        decoded_letters = []
        for code in letters:
            if code in MORSE_TO_TEXT:
                decoded_letters.append(MORSE_TO_TEXT[code])
            else:
                return None, f"Unknown Morse code sequence: '{code}'"
        result_words.append(''.join(decoded_letters))

    return ' '.join(result_words), None
