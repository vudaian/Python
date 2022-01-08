def fibonacci(n):
    if (n < 0):
        return -1;
    elif (n == 0 or n == 1):
        return n;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2);
 
sb = "";
x=int(input("Nhập số phần tử của dãy số: "))
print(x , " số đầu tiên của dãy số fibonacci: ");
for i in range(0, x):
    sb = sb + str(fibonacci(i)) + "  ";
print(sb)