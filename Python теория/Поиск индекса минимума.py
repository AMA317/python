a = list(map(int, input().split())) #список
min_index = 0 #будем считать min_index как нулевой индекс

for i in range(len(a)): #создаем цикл, который будет работать столько раз, сколько равна длина списка
    if a[i] <= a[min_index]: #если у нас элимент в списке  <= элименты с индексом min_index (в нашем случае 0)
        min_index = i #то тогда min_index = лименту i

print('Индекс минимального элемента равен', min_index)