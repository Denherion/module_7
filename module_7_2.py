# Задача "Записать и запомнить"

def custom_write(file_name: str, strings: list):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    string_number = 0
    for string in strings:
        start_of_line_byte = file.tell()
        string_number += 1
        file.write(string + "\n")
        strings_positions[(string_number, start_of_line_byte)] = string
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)




