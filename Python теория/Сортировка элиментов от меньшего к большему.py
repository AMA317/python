spisok = list(map(int, input().split())) #список

#идея такова, что мы рассматриваем весь списко кроме 1 элимента, если рассматриваемы элимент меньше перфого элимента (который мы не рассматриваем), то мы свапаем их местами

for i in range(len(spisok) - 1): #рассматриваем список без первогот элимента
    mini = i #переменная mini будет хранить минимальное значение


    for j in range(i + 1, len(spisok)): #перебираем от элимента с индексом 1 до всей дляины списка
        if spisok[j] < spisok[mini]: #если элимент из j < элимента mini то:

    spisok[i], spisok[mini] = spisok[mini], spisok[i] #свапаем их местами