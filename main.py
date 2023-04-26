s = input("Введіть текст: ")
def count_vowels(s):
    abs = 'qeyuioaQEYUIOA'
    count = 0
    for finish in s :
        if finish in abs:
            count += 1
    print()
    print('Текст:' , s)
    print('Кількість гласних в тексті' , count)
count_vowels(s)
print()