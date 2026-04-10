def stats(lst):
    min = None
    max = None
    freq = {}
    for i in lst:
        if min is None or i < min:
            min = i
        if max is None or i > max:
            max = i
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    lst_sorted = sorted(lst)
    if len(lst_sorted) % 2 == 0:
        middle = len(lst_sorted) // 2
        median = (lst_sorted[middle] + lst_sorted[middle - 1]) / 2
    else:
        median = lst_sorted[len(lst_sorted) // 2]
    mode_times = None
    for i in freq.values():
        if mode_times is None or i > mode_times:
            mode_times = i
    mode = []
    for (num, count) in freq.items():
        if count == mode_times:
            mode.append(num)
    print("list =", lst)
    print("min =", min)
    print("max =", max)
    print("median =", median)
    print("mode(s) =", mode)
    print("-----")
def test():
    # 🔹 Caso 1: lista impar + con repetidos (activa moda y rama impar)
    stats([1, 2, 2, 3, 4])
    # 🔹 Caso 2: lista par (activa cálculo de mediana par)
    stats([10, 20, 30, 40])
    # 🔹 Caso 3: todos iguales (frecuencia alta)
    stats([5, 5, 5, 5])
    # 🔹 Caso 4: sin repetidos (todos frecuencia 1)
    stats([7, 1, 9, 3])
# Ejecutar
test()