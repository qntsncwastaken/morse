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
    action = input('Если вы хотите закодировать сообщение - введите 0, раскодировать - 1; '
            'завершить работу - 000\n').strip()
    if action == '0':        #здесь можно сделать if - elif - elif - else. Думаю, так лучше(и оптимизированней) почему не добавил того пацана?
        text = input('Введите сообщение\n')
        print(f'Закодированное сообщение > {encode_to_morse(text)}')
    if action == '1':
        code = input('Введите код\n')
        print(f'Раскодированное сообщение - {decode_from_morse(code)}.')
    if action == '000':
        print('Завершение работы...')
        return
    if action != '0' and action != '1' and action != '000':  # значение не является ни одним из допустимых
        print('Неверный формат ввода. Перезагрузка...')
    main()
