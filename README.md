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
На вход функции <b>sleight_of_hand(k: int)</b> подается число - количество клавиш, на которые может нажать каждый из двоих участников. Далее итеративно вводим раскладку клавиатуры и заодно пробегаем по значениям. В заранее созданном массиве, содержащим 9 нулей, увеличиваем счетчик числа <b>i</b> на позиции <b>i-1</b> за каждую встречу числа <i> на клавиатуре. Как только какое-то число встретилось первый раз увеличиваем их финальный результат на 1, как только это число встретилось <b>2*k + 1</b> раз, то уменьшаем финальный результат на единицу. Пробежав по всей клавиатуре, получааем ответ
 </details>
