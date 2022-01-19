morse = {'A': '.-', 'B': '-...', 'C': '-.-.',
         'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---',
         'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-',
         'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..',
         }

reverse_morse = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
                 '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                 '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                 '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                 '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                 '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                 '-.--': 'Y', '--..': 'Z'}


def encode_to_morse(text):  # "sos sos" => "... --- ...  ... --- ..."
    return text


def decode_from_morse(code):  # "... --- ...  ... --- ..." => "sos sos" вроде работает
    code = code.split('  ')
    for i in range(len(code)):
        code[i] = code[i].split()
    for i in range(len(code)):
        for j in range(len(code[i])):
            code[i][j] = reverse_morse[code[i][j]].lower()
    for i in range(len(code)):
        code[i] = ''.join(code[i])
    return ' '.join(code)


def main():
    action = int(input('Если вы хотите закодировать сообщение - введите 0, раскодировать - 1 \n'))
    if action == 0:
        text = input('Введите сообщение \n')
