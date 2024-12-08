# Проект "Игры разума"

[![Hexlet Ltd. logo](https://raw.githubusercontent.com/Hexlet/assets/master/images/hexlet_logo128.png)](https://ru.hexlet.io/?utm_source=github&utm_medium=link&utm_campaign=ru-test-assignments)
В этом репозитории собраны 5 простых консольных игр.<br> 
В начале каждой игры, после приветствия, вам будет предложено ввести свое имя.<br>
Введите имя и начинайте игру.<br>
В случае если вы трижды верно ответите на вопросы игры - вы победили.<br> 
Если вы дадите неверный ответ игра немедленно закончится и вам будет предложено сыграть еще раз.<br>
Правила каждой из игр описаны ниже.<br>

<details>
 <summary>"Калькулятор" (brain_calc)</summary>
 <br>Для запуска игры наберите brain-calc и нажмите клавишу "ENTER".
 <br>Так же игру можно запустить с помощью команды "make calc".
 <br>Программа предлагает вам решить простое выражение. Наберите ваш ответ на клавиатуре и нажмите клавишу "ENTER".
<p></p>
 <details>
    <summary>Пример успешной игры "Калькулятор: </summary>
    <p></p>
  
  [![brai-calc_victory](https://asciinema.org/a/KbrZvlJ0gAff8399X60H1NjuG.svg)](https://asciinema.org/a/KbrZvlJ0gAff8399X60H1NjuG)
 </details>
</details>
<hr></hr>

<details>
 <summary>"Чет-Нечет" (brain_even)</summary>
Для запуска игры наберите brain-even и нажмите клавишу "ENTER".
 <br>Так же игру можно запустить с помощью команды "make even".
 <br>Программа предлагает определить, является ли предлагаемое число четным, 
 <br>если вы считаете, что число четное наберите "yes", если нечетным, наберите "no".
 <br>После того как вы наберете на клавиатуре ваш ответ нажмите клавишу "ENTER".
<p></p>
 <details>
 <summary>Пример успешной игры: </summary>
  
  [![brai-calc_victory](https://asciinema.org/a/KbrZvlJ0gAff8399X60H1NjuG.svg)](https://asciinema.org/a/KbrZvlJ0gAff8399X60H1NjuG)
 </details>
</details>
<hr></hr>
 
 <details>
 <summary>"Наименьший общий делитель" (brain_gcd)</summary>
  <br>Для запуска игры наберите brain-gcd и нажмите клавишу "ENTER".
  <br>Так же игру можно запустить с помощью команды "make gcd".
  <br>Программа предлагает определить наименьший общий делитель двух чисел. 
  <br>Найденное решение наберите на клавиатуре и нажмите клавишу "ENTER".
<p></p>
 <details>
 <summary>Пример успешной игры: </summary>
  
 [![brain-gcd_victory](https://asciinema.org/a/2USkyJzQhILvKUodeYNLr2zZ8.svg)](https://asciinema.org/a/2USkyJzQhILvKUodeYNLr2zZ8)
 </details>
</details>
<hr></hr>

<details>
 <summary>"Простые числа" (brain_prime)</summary>
 <br>Для запуска игры наберите brain-prime и нажмите клавишу "ENTER".
 <br>Так же игру можно запустить с помощью команды "make prime".
 <br>Программа предлагает определить является ли предоставленное число простым, 
 <br>т.е делящимся без остатка только на себя или на 1, если вы считаете, что число простое,
 <br>то наберите "yes" если число не является простым, наберите "no".
 <p></p>
 <details>
 <summary>Пример успешной игры: </summary>
  
 [![brain-prime_victory](https://asciinema.org/a/JIZl2ajtPiOpZ0gU0UQIBntFn.svg)](https://asciinema.org/a/JIZl2ajtPiOpZ0gU0UQIBntFn)
 </details>
</details>
<hr></hr>

<details>
 <summary>"Прогрессия" (brain_progression)</summary>
 <br>Для запуска игры наберите brain-progression и нажмите клавишу "ENTER".
 <br>Так же игру можно запустить с помощью команды "make progression".
 <br>Программа выводит на экран последовательность чисел, являющихся 
 <br>арифметической прогрессией. В последовательности в произвольном месте,
 пропущено число, вам предстоит найти это число и набрать его на клавиатуре, затем нажмите клавишу "ENTER".
<p></p>
 <details>
 <summary>Пример успешной игры: </summary>
  
 [![brain-progression_victory](https://asciinema.org/a/ybRHleJe8rt0RJ5gjHUEdLVWd.svg)](https://asciinema.org/a/ybRHleJe8rt0RJ5gjHUEdLVWd)
 </details>
</details>
<hr></hr>
<p></p>
<p></p>

<details>
 <summary><h>Установка и запуск игр</h></summary>
  <br>После того как вы получили дистрибутив на свой компьютер выполните установку игр:
  <br>Войдите в директорию /python-project-49</br>
  <br>Наберите на клавиатуре make build и нажмите клавишу "ENTER".
  <br>Наберите на клавиатуре make package-install и нажмите клавишу "ENTER".
  <br>Наберите на клавиатуре make install и нажмите клавишу "ENTER".
  <br>Можете начинать игру!</br>
</details>

<p></p>
<p></p>

<details>
 <summary>Технологиии примененные при создании игры</summary>
  <br>Игра написана на языке программирования Python (version 3.10.12)
  <br>Проверка кода выполнена с помощью ruff (version 0.8.2) 
  <br>Сборка пакета выполнена с помощью Poetry (version 1.8.3)
</details>



  ### Статусы тестирования и проверки:
[![Actions Status](https://github.com/epolval/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/epolval/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/6d09c7fb21da73098770/maintainability)](https://codeclimate.com/github/epolval/python-project-49/maintainability)

