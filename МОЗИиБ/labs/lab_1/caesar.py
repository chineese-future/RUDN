# Шифр Цезаря с поддержкой русского и английского языка:
def caesar_cipher(text, shift, lang):
  result = ''
  if lang == 'ru':
    #  Для русского языка
    alphabet_size = 32
    for char in text:
      if char.isalpha(): # Проверка символа на буквенность
        if 'А' <= char <= 'Я' or 'a' <= char <= 'я':
          ascii_offset = 1040 if char.isupper() else 1072 # Смещение для букв русского алфавита
          result += chr((ord(char)-ascii_offset+shift)%alphabet_size + ascii_offset)
        else:
          # если символ - не буква - без изменений
          result += char
  elif lang == 'en':
    #Если язык - английский
    alphabet_size = 26
    for char in text:
      if char.isalpha(): # Проверка символа на буквенность
          ascii_offset = 65 if char.isupper() else 97 # Смещение для букв английского алфавита
          result += chr((ord(char)-ascii_offset+shift)%alphabet_size + ascii_offset)
      else:
          # если символ - не буква - без изменений
          result += char
  return result
def caesar_cipher_main():
  # Выбор языка
  lang = input("Выбор языка(en/ru): ").lower()

  if lang not in ['en', 'ru']:
    print("Неподдерживаемый язык")
    return

    #Получение данных для шифрования
  text = input("Введите сообщение для шифрования:")
  shift = int(input("Введите ключ (cдвиг) для шифрования:"))
  # шифрование:
  encrypted_text = caesar_cipher(text, shift, lang)
  print("Зашифрованный текст:", encrypted_text)

# Запуск:
if __name__ == "__main__":
  caesar_cipher_main()
