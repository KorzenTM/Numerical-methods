
def newton_method(number, number_iters = 500):
    a = float(number) 
    for i in range(number_iters): 
        number = (0.2) * (4*number + a / number**4) 
	  # x_(n+1) = 0.5 * (x_n +a / x_n)
    return number


num=float(input("Enter a value:"))
print(newton_method(num))

