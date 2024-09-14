# Шифр Атбаш с поддержкой русского и английского языка:
def atbash_cipher(text, lang):
  result = ''
  if lang == 'ru':
    #  Для русского языка
    for char in text:
      if char.isalpha(): # Проверка символа на буквенность
        if 'А' <= char <= 'Я':
          result += chr(1040 +(31 - (ord(char)-1040))) #  для заглавных букв русского алфавита
        elif 'a' <= char <= 'я':
          result += chr(1072 +(31 - (ord(char)-1072))) #  для строчных букв русского алфавита
        else:
          # если символ - не буква - без изменений
          result += char
  elif lang == 'en':
    #Если язык - английский
    alphabet_size = 26
    for char in text:
      if 'A' <= char <= 'Z':
          result += chr(65 +(25 - (ord(char)-65))) #  для заглавных букв английского алфавита
      elif 'a' <= char <= 'z':
          result += chr(97 +(25 - (ord(char)-97))) #  для строчных букв английского алфавита
      else:
        # если символ - не буква - без изменений
        result += char
  return result
def atbash_cipher_main():
  # Выбор языка
  lang = input("Выбор языка(en/ru): ").lower()

  if lang not in ['en', 'ru']:
    print("Неподдерживаемый язык")
    return

    #Получение данных для шифрования
  text = input("Введите сообщение для шифрования:")
  # шифрование:
  encrypted_text = atbash_cipher(text, lang)
  print("Зашифрованный текст:", encrypted_text)

# Запуск:
if __name__ == "__main__":
  atbash_cipher_main()
