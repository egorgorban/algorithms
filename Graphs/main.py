from graph import Graph
from johnson import Johnson
from time import sleep, time
from math import log2
import pandas as pd
from random import randint as rint
import numpy as np

# ------------------------------------------------------------------------------------------------
# первый график
# ------------------------------------------------------------------------------------------------

# Элементы словаря - {value: t}, где value - значение переменной, характеризующей объём входных данных (количество вершин), t - время работы алгоритма
time_johnson = {}

# Элементы словаря {value: t}, где value - значение переменной, характеризующей объём входных данных (количество вершин), t - время работы функции, определяющей класс временной сложности
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
        # СОЗДАНИЕ ГРАФА
        # False означает, что граф не пустой, далее передаются количество вершин и рёбер соответственно
        G = Graph(False, v, e_number)
        # начинаем замерять время работы алгоритма
        t1 = time()
        # ЗДЕСЬ ВЫЗЫВАЕТСЯ АЛГОРИТМ
        paths = Johnson(G)
        # заканчиваем замерять время работы алгоритма
        t2 = time() - t1
        t.append(t2)
    # среднее время работы (см. ранее)
    time_johnson[v] = sum(i for i in t)/k

    # Симулирование функции, определяющей класс временной сложности O(v*v*log(v)+v*e)
    time_average[v] = (v*v*log2(v)+v*e_number
    
# График, показывающий отношение измеренной сложности к сложности функции, определяющей класс временной сложности
t={}
# чтобы привести графики к одному масштабу
for i in time_average.keys():
    t[i] = time_average[i]/700000
d = {"измеренная": pd.Series(time_johnson), "теоретическая": pd.Series(t)}
df = pd.DataFrame(d)
df.plot(kind='line',figsize=(15,5))
plt.title("Отношение измеренной трудоёмкости к теоретической")
plt.xlabel("Количество вершин")
plt.ylabel("Время, с")
plt.show()
                       
# ------------------------------------------------------------------------------------------------
# второй график
# ------------------------------------------------------------------------------------------------

# элементы словаря [v, t, av_t], где v - значение переменной, характеризующей объём входных данных (количество вершин), 
# t - отношение времен работы алгоритма на текущем и удвоенном объёме данных, 
# av_t - отношение (v*log2(v)+e_number)/(v*log2(2*v)+e_number), для вычисления теоретического значения O(T(n)/T(2n))
meas = []

# пределы входных значений (количества вершин)
_from = 10
_to = 50

for v in range(_from, _to):
    # здесь хранятся времена работы на одинаковом объёме входных данных для последующего усреднения
    t = []
    # количество повторений
    k = 10
    # Генерируется количество рёбер
    e_number = rint(v*(v-1)//6, v*(v-1)*2//3)

    for _ in range(k):
        # СОЗДАНИЕ ГРАФА
        # False означает, что граф не пустой, далее передаются количество вершин и рёбер соответственно
        G = Graph(False, v, e_number)
        # начинаем замерять время работы алгоритма
        t1 = time()
        # ЗДЕСЬ ВЫЗЫВАЕТСЯ АЛГОРИТМ
        paths = Johnson(G)
        # заканчиваем замерять время работы алгоритма
        t2 = time() - t1
        t.append(t2)
    # среднее время работы (см. ранее)
    _t1 = sum(i for i in t)/k
   
    # Аналогично с удвоенным объёмом входных данных
    for _ in range(k):
        G = Graph(False, v*2, e_number*2)
        t1 = time()
        paths = Johnson(G)
        t2 = time() - t1
        t.append(t2)
    _t2 = sum(i for i in t)/k

    meas.append([v, _t1/_t2, (v*log2(v)+e_number)/(v*log2(2*v)+e_number)])               
                       
# График, показывающий изменение сложности при удвоении данных

a1 = meas[1]
a2 = np.array(meas)[:,2]/4

d1 = {"измеренных": pd.Series(a1, index=[i+10 for i in range(len(a1))]), "теоретических": pd.Series(a2, index=[i+10 for i in range(len(a2))])}
df1 = pd.DataFrame(d1)
df1.plot(kind='line',figsize=(15,5))
plt.title("Отношение трудоёмкостей при удвоении объёма входных данных")
plt.xlabel("Объём входных данных (кол-во вершин)")
plt.ylabel("Время, с")
plt.show()
