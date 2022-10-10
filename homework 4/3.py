from random import random
from typing import Iterable


list_num_seq=[int(20*random()) for i in range(10)]
print(f"Заданая последовательность: {list_num_seq}")
new_list=[]
[new_list.append(i) for i in list_num_seq if i not in new_list]
print(f"Список из неповторяющихся элементов: {new_list}")
