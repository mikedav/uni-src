"""
Давыдов М
сумму ряда (1.3)**(н-1) / (н + 1)!
"""

arg_value, eps, max_iter = map(float, input("Введите X Eps N: ").split())

max_iter = int(max_iter)

num_iter = 1
cur_value = 1/2
sum_value = cur_value

while not (num_iter > max_iter or cur_value < eps):
    cur_value *= (1/3) / (num_iter + 1)
    sum_value += cur_value
    num_iter += 1

if cur_value > eps:
    print("За указанное число итераций необходимой точности достичь не удалось")
    
print(f"Значение суммы {sum_value:6g} вычислено за {num_iter} итераций")
