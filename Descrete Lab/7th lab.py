import math

# read input value from file
file_name = input("Enter file name with extension: ")
f = open(file_name, "r")

data = f.read()
print(data)
data = data.split()
x, y = [], []
for i, j in zip(data[0::2], data[1::2]):
    x.append(float(i))
    y.append(float(j))
inp = float(input("Enter value of x for interpolation: "))
table = [y]
for l in range(len(y) - 1):
    yn = []
    for i, k in zip(y[1::1], y[0::1]):
        yn.append(i - k)
    table.append(yn)
    y = yn
# print table
formated_table = [["x", "f(x)", "∇f(x)"]]
for i in range(2, len(table)):
    formated_table[0].append("∇^" + str(i) + "f(x)")
for i in range(len(x)):
    row = []
    for j in range(len(table) - i):
        row.append(str(round(table[j][i], 5)))
    row.insert(0, str(x[i]))
    formated_table.append(row)
for row in formated_table:
    print(" \t".join(row))
# calculation of r
r = (inp - x[-1]) / (x[1] - x[0])
r_component = 1
partial_result = 0
for i in range(1, len(table)):
    r_component = r_component * (r + i - 1)
    partial_result = partial_result + (table[i][-1] * r_component)
math.factorial(i)
final_result = table[0][-1] + partial_result
print("f(" + str(inp) + ") = ", final_result)
