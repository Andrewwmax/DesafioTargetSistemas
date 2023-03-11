# Python

def fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    if b != num:
        return False
    else:
        return True

def ehFibonacci(num):
	if num < 0:
		print('Entrada Incorreta, somente [\'num\' >= 0]')
	if fibonacci(num):
	    print(f'{num} pertence à sequência de Fibonacci.')
	else:
	    print(f'{num} não pertence à sequência de Fibonacci.')


# Lista dos 2000 primeiros números da sequência de Fibonacci neste link
# https://oeis.org/A000045/b000045.txt
num = 280571172992510140037611932413038677189525 # 200
ehFibonacci(num)