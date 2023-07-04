# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


def recr (a,b,multi):
    if b==0:
        return a
    return recr(a*multi, b-1, multi)

a = int(input())
b = int(input())
print(recr(1,b,a))