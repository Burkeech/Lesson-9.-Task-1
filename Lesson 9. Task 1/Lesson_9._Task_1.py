x=int(input("Введите количество элементов списка - "))

spisok = list(map(int, input("Введите через пробел элементы списка - ").split()))[:x]

e=set(spisok)

len(e)
print("Среди этих чисел различных - ", len(e))