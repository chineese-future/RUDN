---
# Front matter
lang: ru-RU
title: "Лабораторная работа №2"
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

Познакомиться с реализацией шифров перестановки: маршрутный, решётка, Вижинера.

# Задание

1. Реализовать маршрутный шифр.
2. Реализовать шифрование решёткой.
3. Реализовать шифр Вижинера

# Выполнение лабораторной работы

1) Сначала я написал функцию выбора алфавита.

![Выбор алфавита](image1/image1.png){ width=70% }

2) Далее реализован шифр Вижинера.

![Генерация ключа и шифрование Вижинером](image1/image2.png){ width=70% }
![Расшифрование Вижинером](image1/image3.png){ width=70% }

3) Выполнение шифрования маршрутным шифром

![Шифрование маршрутным](image1/image4.png){ width=70% }

4) Выполнение дешифровки маршрутным шифром

![Дешифровка маршрутным](image1/image5.png){ width=70% }

5) Выполнение шифрования решёткой:

![Шифр решётки](image1/image6.png){ width=70% }

6) Выполнение основной части программы (взаимодействия с пользователем)

![Взаимодействие с пользователем](image1/image7.png){ width=70% }

7) Проверка работоспособности шифра Вижинера

![Проверка метода шифра Вижинера](image1/image8.png){ width=70% }

8) Проверка работоспособности маршрутного шифра

![Проверка маршрутного шифра]](image1/image9.png){ width=70% }

Полный код программы в https://colab.google: https://colab.research.google.com/drive/1mA9WtslytuM3D3ZfgU4SkrwKG8rGgdXR?usp=sharing

# Выводы

На практике изучил работу познакомиться с шифрами перестановки: маршрутный, решётка, Вижинера.