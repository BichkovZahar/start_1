#Задано дві змінні a і b зі значеннями 5 та 10
#відповідно. Напишіть функцію swap(a, b), яка обмінює
#значеннями змінних a і b. Напишіть код, що демонструє
#роботу функції та показує значення змінних a і b до та
#після виклику функції
a = 5
b = 10
def swap(a,b):
    a , b = b , a
    return a , b
print(f'До обміну a = {a} , b = {b}')
a , b = swap(a, b)
print(f'Після обміну a = {a} , b = {b}')
