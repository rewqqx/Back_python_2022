# Back_python_2022
## Спринт 1
<details>
<summary>
<b>Ближайший ноль (<a href="sprint1/task1.py">nearest_zero.py</a>)</b>
</summary>

#### Алгоритм решения

На вход функции <b>nearest_zero(array: list)</b> подается список домов. Дальше я пробегаю список одновременно два раза: слева направо и справа налево. Записываю искомые расстояния в два массива <b>dist_fin_1</b> и <b>dist_fin_2</b>. Ответом задачи будет являться строка минимальных значений из соответствующих элементов двух массивов.
</details>


<details>
<summary>
<b>Ловкость рук (<a href="sprint1/task2.py">sleight_of_hand.py</a>)</b>
</summary>
 
 #### Алгоритм решения
На вход функции <b>sleight_of_hand(k: int)</b> подается число - количество клавиш, на которые может нажать каждый из двоих участников. Далее итеративно вводим раскладку клавиатуры и заодно пробегаем по значениям. В заранее созданном массиве, содержащим 9 нулей, увеличиваем счетчик числа <b>i</b> на позиции <b>i-1</b> за каждую встречу числа <b>i</b> на клавиатуре. Как только какое-то число встретилось первый раз увеличиваем их финальный результат на 1, как только это число встретилось <b>2*k + 1</b> раз, то уменьшаем финальный результат на единицу. Пробежав по всей клавиатуре, получааем ответ
 </details>

## Спринт 2
<details>
<summary>
<b>Генерация скобочных последовательностей (<a href="sprint2/psp.py">psp.py</a>)</b>
</summary>

#### Алгоритм решения
  
Сначала генерируем первую строку, для всех входных чисел она одинакова (сначала n - "(", затем n - ")"). Затем получаем следующую скобочную последовательность. Принцип генерация следующей скобочной последовательности: в предыдущей последовательности ищем последнюю открывающуюся скобку, которую можно заменить (внутри цикла идет проверка на правильную последовательность, т.е. количество закрывающихся должно быть меньше или равно закрывающихся). Заменяем последнюю возможную открывающуюся на закрывающуюся, и в оставшееся место в строке заменяем на лексикографически минимальную возможную последовательность скобок.
</details>


<details>
<summary>
<b>Самое большое число (<a href="sprint2/largest_number.py">largest_number.py</a>)</b>
</summary>
 
 #### Алгоритм решения
С помощью "пузырька" сортируем входной набор чисел по лексикографическому убыванию цифр
 </details>

## Спринт 3
<details>
<summary>
<b> Двоичная система счисления (<a href="sprint3/binary.py">binary.py</a>)</b>
</summary>

#### Алгоритм решения

С помощью операции взятия остатка от деления формируем двоичную запись. С помощью целочисленного деления уменьшаем исходное число. Также добавляем условие для "входного" нуля.  
</details>


<details>
<summary>
<b>Палиндром (<a href="sprint3/palindrome.py">palindrome.py</a>)</b>
</summary>
 
 #### Алгоритм решения
С помощью регулярных выражений убираем все символы, кроме букв и цифр. Переводим получившуюся строку в нижний регистр. Сравниваем измененную строку и её перевернутый образ. Если равны true, иначе false.
 </details>
