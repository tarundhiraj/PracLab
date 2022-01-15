"""
Write a program to generate first 'n' fibonacci series

Example usage:
--------------
    >>> fib(10)
    0 1 1 2 3 5 8 13 21 34 

    >>> fib(20)
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 
"""

def fib(n):
    if n < 0:
    	print(0)
    else:
    	a,b = 0,1
    	for i in range(n):
    		print(a, end=" ")
    		a,b = b, a+b

    	print()


def fib_list(n):
	series = [0,1]
	for i in range(n-2):
		series.append(series[-1] + series[-2])

	return series

if __name__ == '__main__':
    
    for i in fib_list(20):
    	print(i, i*i)

