---
# Front matter
lang: ru-RU
title: "Лабораторная работа №1"
subtitle: "Дисциплина: Математические основы защиты информации и информационной безопасности"
author: "Лабузов Александр Сергеевич"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # Список рисунков
lot: true # Список таблиц
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Познакомиться с реализацией шифров простой замены: шифры Цезаря и Атбаш.

# Задание

1. Реализовать шифр Цезаря с произвольным ключом k.
2. Реализовать шифр Атбаш.

# Выполнение лабораторной работы

1) Сначала я написал функцию для шифра Цезаря на языке Python с возможностью консольного выбора языка (русский и английский)в среде google.colab. Я использовал вводимую переменную k в качестве сдвига, назвав её shift в коде. При проверке слова берётся каждый конкретный его символ (char). При этом ведётся учёт регистра символа. Если символ находится в алфавите, то берётся его код ASCII, из которого вычитается код ASCII первой буквы алфавита. Затем прибавляется сдвиг k (shift) и берётся остаток от количества символов в алфавите (русский - 32, английский 26). После чего мы определяем, какая по счёту буква в алфавите, и прибавляем код ASCII первой буквы алфавита. Затем вписываем каждый символ в result и возвращаем его.

![Шифр Цезаря на языке Python](image1/image1.png){ width=70% }

2) Далее реализована функция взаимодействия с пользователем и запуском алгоритма шифра Цезаря.

![Запрос текста и вывод результата шифра Цезаря](image1/image2.png){ width=70% }

3) Проверка работоспособности кода:

![Проверка метода шифра Цезаря](image1/image3.png){ width=70% }

4) Ниже отображена реализация функции шифра Атбаша. При проверке слова берётся конкретный символ (char).Ниже реализован консольный выбор языка проверки на наличие выбранного символа в русском или английском алфавите. При этом я учёл регистр символа. Если символ находится в алфавите, то берётся код ASCII последней буквы алфавита, из которого вычитается код ASCII выбранного символа. С помощью этого мы определяем, какое значение имеет симметричный центру символ алфавита. Затем мы прибавляем код ASCII первой буквы алфавита, чтобы определить нужный нам символ. Затем вписываем каждый символ в result и возвращаем его.

![Шифр Атбаш на языке Python](image1/image4.png){ width=70% }

5) Далее реализована функция запуска шифра Атбаша и запуска программы:

![Вывод результата шифра Атбаш](image1/image5.png){ width=70% }

6) Проверка работоспособности шифра Атбаша:

![Проверка метода шифра Атбаш](image1/image6.png){ width=70% }


# Выводы

На практике изучил работу шифров простой замены реализацией шифра Цезаря с произвольным ключом k и Атбаша.
