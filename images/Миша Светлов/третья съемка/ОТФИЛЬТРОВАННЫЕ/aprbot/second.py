
import copy
from itertools import permutations
import sys

import time
t = time.time()

number = 7 # int(sys.argv[1]) if len(sys.argv) > 1 else 5



uniq_numbers = list(range(number + 1)) # все числа

perm = list(permutations(uniq_numbers[1:])) # перестановки только от неповторяющихся чисел, N!


# теперь для каждой перестановки из неповторяющихся чисел
# напр., 1 2 3 4 5
# в начале, в конце и между цифрами можно ставить любое количество нулей
# но всего нулей должно быть тоже 5
# так что для расстановки нулей нужно взять все комбинации 6-ти чисел от 0 до 5, у которых сумма равна 5 (числу нулей)
#
# уникальные наборы этих числе ищутся следующими функциями
#
#


def CombinationRepetitionUtil(chosen, arr, index,
                              r, start, end, here):
                                   
    # Current combination is ready,
    if index == r:
        here.append(copy.copy(chosen[:r]))
        return
         
    # When no more elements are
    # there to put in chosen[]
    if start > end:
        return
         
    # Current is included, put
    # next at next location
    chosen[index] = arr[start]
     
    # Current is excluded, replace it
    # with next (Note that i+1 is passed,
    # but index is not changed)
    CombinationRepetitionUtil(chosen, arr, index + 1,
                              r, start, end, here)
    CombinationRepetitionUtil(chosen, arr, index,
                              r, start + 1, end, here)
 
def CombinationRepetition(arr, r):
    
    here = []
    
    # A temporary array to store
    # all combination one by one
    chosen = [0] * r
 
    CombinationRepetitionUtil(chosen, arr, 0, r, 0, len(arr) - 1, here)
    
    return here
 


 
sums = [v for v in CombinationRepetition(uniq_numbers, len(uniq_numbers)) if sum(v) == number] # уникальные наборы чисел, дающих в сумме сколько надо

all_sets = sum([list(set(permutations(s))) for s in sums], []) # для каждого набора смотрю все комбинации, выбираю уникальные и все складываю вместе


def combine(zeros, another):
    """
    делает комбинацию от набора уникальных чисел
    и количеств нулей между ними и по бокам
    """

    answer = [0]*zeros[0]
    for i in range(len(another)):
        answer.append(another[i])
        answer.extend([0]*zeros[i+1])
    
    return ''.join(map(str, answer))


# все это перемножается друг с другом и выводится в файл

with open('Pasko_secondtask.txt', 'w') as f:

    for i, zeros in enumerate(all_sets):
        for j, uniq in enumerate(perm):

            print(combine(zeros, uniq), file=f)



print(time.time() - t)

    