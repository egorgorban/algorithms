from graph import Graph
from johnson import Johnson
from time import sleep, time
from math import log2
import pandas as pd
from random import randint as rint


# Элементы словаря - {value: t}, где value - значение переменной, характеризующей объём входных данных, t - время работы алгоритма
time_johnson = {}

# Элементы словаря {value: t}, где value - значение переменной, характеризующей объём входных данных, t - время работы функции, определяющей класс временной сложности
time_average = {}

# пределы входных значений (количества вершин)
_from = 10
_to = 100


for v in range(_from, _to):

    # здесь хранятся времена работы на одинаковом объёме входных данных для последующего усреднения
    t = []

    # количество повторений
    k = 10

    # Генерируется количество рёбер
    e_number = rint(v*(v-1)//6, v*(v-1)*2//3)

    for _ in range(k):
        # False означает, чтограф не пустой, далее передаются количество вершин и рёбер соответственно
        G = Graph(False, v, e_number)
        t1 = time()
        paths = Johnson(G)
        t2 = time() - t1
        t.append(t2)
    # среднее время работы (см. ранее)
    time_johnson[v] = sum(i for i in t)/k

    # Симулирование функции, определяющей класс временной сложности O(v*v*log(v)+v*e)

    # столько раз нужно повторять какие-то действия, занимающие константное время,
    # чтобы можно было говорить о симуляции функции, определяющей класс временной сложности
    stop = int(v*v*log2(v)+v*e_number)

    t1 = time()
    for _ in range(stop):
        # рандомные действия, не зависящие от шага (занимающие константное время)
        for i in range(3):
            s = i*(i)+1
            s = log2(s)
    t2 = time() - t1

    time_average[v] = t2
    
# График, показывающий отношение измеренной сложности к сложности функции, определяющей класс временной сложности

d = {"johnson": pd.Series(time_johnson), "g(n)": pd.Series(time_average)}
df = pd.DataFrame(d)
df.plot(kind='line',figsize=(15,5))
plt.show()

# График, показывающий изменение сложности при удвоении данных

a1 = [time_johnson[i] for i in range(_from, _to//2 + 1)]
a1x2 = [time_johnson[2*i] for i in range(_from, _to//2)]
d1 = {"data": pd.Series(a1, index=[i+10 for i in range(len(a1))]),
      "data x2": pd.Series(a1x2, index=[i+10 for i in range(len(a1x2))])}
df1 = pd.DataFrame(d1)
df1.plot(kind='line',figsize=(15,5))
plt.show()

