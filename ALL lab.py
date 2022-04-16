######## 1st ########
# find the ordered pairs are in the relation 𝐑
# 𝐑𝟏 = {(𝐚, 𝐛) | 𝐚 𝐝𝐢𝐯𝐢𝐝𝐞𝐬 𝐛} 𝐑𝟐 = {(𝐚,𝐛) | 𝐚 ≤ 𝐛}

from itertools import product
with open("input.txt", "r", encoding="utf-8") as g:
    S = list(map(int, g.readlines()))
    print("S= "+str(S))
    res=[(i,j) for i,j in product(S,repeat=2) if i%j==0 or j%i==0]
    res2=[(i,j) for i,j in product(S,repeat=2) if i<=j]
    # printing result
print ("The pair list is for a/b : " + str(res))
print ("The pair list is for a<=b : " + str(res2))

############# 2nd #############
#(a, b) if 𝐚 ∈ 𝐀 , 𝐛 ∈ 𝐁 and 𝐚 > 𝐛.
# represent this relation in matrix form.

import numpy as np
with open("input.txt", "r", encoding="utf-8") as g:
    list1 = list(map(int, g.readlines()))
    with open("input.txt", "r", encoding="utf-8") as g:
        list2 = list(map(int, g.readlines()))
        # using list comprehension
        output = [(a, b) for a in list1 for b in list2 if a > b]
        output2 = [1 if a>b else 0 for a in list1 for b in list2]
        data = np.array(output2).reshape(4,4)
        print(output)
        print(data)


########## 3rd ##########
#Welch Powell algorithm

def color_nodes(graph):
  # Order nodes in descending degree
  nodes = sorted(list(graph.keys()), key=lambda x: len(graph[x]), reverse=True)
  color_map = {}

  for node in nodes:
    available_colors = [True] * len(nodes)
    for neighbor in graph[node]:
      if neighbor in color_map:
        color = color_map[neighbor]
        available_colors[color] = False
    for color, available in enumerate(available_colors):
      if available:
        color_map[node] = color
        break

  return color_map


if __name__ == '__main__':
  graph = {
    'a': list('bcd'),
    'b': list('ac'),
    'c': list('abdef'),
    'd': list('ace'),
    'e': list('cdf'),
    'f': list('ce')
  }
  print(color_nodes(graph))
  # {'c': 0, 'a': 1, 'd': 2, 'e': 1, 'b': 2, 'f': 2}

########  4th  ###########
# Floyd Warshall Algorithm in python

# The number of vertices
nV = 4

INF = 999


# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)


# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G =      [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
floyd_warshall(G)

##########  5th  ########
# R1 and R2 on a set A are represented by the matrices
# MR1uR2 and MR1@R2

def matrix_intersection(mat1, mat2):
    rows = len(mat1)
    cols = len(mat1[0])
    print('Rows=', rows, 'Cols=', cols)
    mat_inter = []
    for i in range(len(mat1)):
        mat_inter.append([mat1[i][j] and mat2[i][j] for j in
                          range(len(mat1[0]))])
        return mat_inter


def matrix_union(mat1, mat2):
    mat_union = []
    for i in range(len(mat1)):
        mat_union.append([mat1[i][j] or mat2[i][j] for j in
                          range(len(mat1[0]))])
    return mat_union


matrix1 = [[1, 0, 1],
           [1, 0, 0],
           [0, 1, 1]]
matrix2 = [[1, 0, 1],
           [0, 1, 1],
           [1, 0, 1]]
print('First Matrix=', matrix1)
print('Second Matrix=', matrix2)
mi = matrix_intersection(matrix1, matrix2)
print('Matrix Intersection', mi)
mu = matrix_union(matrix1, matrix2)
print('Matrix Union', mu)
v = ['p', 'q', 'r']
r1 = []
for i in range(len(mi)):
    for j in range(len(mi[0])):
        if mi[i][j] == 1:
            r1.append((v[i], v[j]))
            print(r1)
r2 = []
for i in range(len(mu)):
    for j in range(len(mu[0])):
        if mu[i][j] == 1:
            r2.append((v[i], v[j]))
print(r2)


###########  6th ##########
#Newton Gregory forward interpolation formula

def u_cal(u, n):
    temp = u;
    for i in range(1, n):
        temp = temp * (u - i);
    return temp;


# calculating factorial of given number n
def fact(n):
    f = 1;
    for i in range(2, n + 1):
        f *= i;
    return f;


# Driver Code

# Number of values given
n = 6;
x = [ 1911, 1921, 1931, 1941,1951,1961 ];

# y[][] is used for difference table
# with y[][0] used for input
y = [[0 for i in range(n)]
     for j in range(n)];
y[0][0] = 12;
y[1][0] = 15;
y[2][0] = 20;
y[3][0] = 27;
y[4][0] = 39;
y[5][0] = 52;


# Calculating the forward difference
# table
for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1];

# Displaying the forward difference table
for i in range(n):
    print(x[i], end="\t");
    for j in range(n - i):
        print(y[i][j], end="\t");
    print("");

# Value to interpolate at
value = 1946;

# initializing u and sum
sum = y[0][0];
u = (value - x[0]) / (x[1] - x[0]);
for i in range(1, n):
    sum = sum + (u_cal(u, i) * y[0][i]) / fact(i);

print("\nValue at", value,
      "is", round(sum, 6));


###############  7th  #########
#Newton Gregory backward interpolation formula

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


########   8th  #######
# Python3 program for implementing
# Newton divided difference formula

# Function to find the product term
def proterm(i, value, x):
    pro = 1;
    for j in range(i):
        pro = pro * (value - x[j]);
    return pro;


# Function for calculating
# divided difference table
def dividedDiffTable(x, y, n):
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                       (x[j] - x[i + j]));
    return y;


# Function for applying Newton's
# divided difference formula
def applyFormula(value, x, y, n):
    sum = y[0][0];

    for i in range(1, n):
        sum = sum + (proterm(i, value, x) * y[0][i]);

    return sum;


# Function for displaying divided
# difference table
def printDiffTable(y, n):
    for i in range(n):
        for j in range(n - i):
            print(round(y[i][j], 4), "\t",
                  end=" ");

        print("");

    # Driver Code


# number of inputs given
n = 6
y = [[0 for i in range(n)] for j in range(n)]
x = [4, 5, 7, 10, 11, 13]
print(x)


# y[][] is used for divided difference
# table where y[][0] is used for input
y[0][0] = 48
y[1][0] = 100
y[2][0] = 294
y[3][0] = 900
y[4][0] = 1210
y[5][0] = 2028
print(y)
# calculating divided difference table
y = dividedDiffTable(x, y, n);

# displaying divided difference table
printDiffTable(y, n);

# value to be interpolated
value = 15;

# printing the value
print("\nValue at", value, "is",
      round(applyFormula(value, x, y, n), 2))


value = 8
# printing the value
print("\nValue at", value, "is", round(applyFormula(value, x, y, n), 2))

############# 9th ###########
# Python3 program for implementation
# of Lagrange's Interpolation

# To represent a data point corresponding to x and y = f(x)
class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# function to interpolate the given data points
# using Lagrange's formula
# xi -> corresponds to the new data point
# whose value is to be obtained
# n -> represents the number of known data points
def interpolate(f: list, xi: int, n: int) -> float:
    # Initialize result
    result = 0.0
    for i in range(n):

        # Compute individual terms of above formula
        term = f[i].y
        for j in range(n):
            if j != i:
                term = term * (xi - f[j].x) / (f[i].x - f[j].x)

        # Add current term to result
        result += term

    return result


# Driver Code
if __name__ == "__main__":
    # creating an array of 4 known data points
    f = [Data(5, 12), Data(6, 13), Data(9, 14), Data(11, 16)]

    # Using the interpolate function to obtain a data point
    # corresponding to x=3
    print("Value of f(10) is :", interpolate(f, 10, len(f)))



######### 10th #####
# Python3 implementation of Bisection


def func(x):
    return x * x * x - 2 * x - 5


# Prints root of func(x)
# with error of EPSILON
def bisection(a, b):
    if (func(a) * func(b) >= 0):
        print("You have not assumed right a and b\n")
        return

    c = a
    while ((b - a) >= 0.0001):

        # Find middle point
        c = (a + b) / 2

        # Check if middle point is root
        if (func(c) == 0.0):
            break

        # Decide the side to repeat the steps
        if (func(c) * func(a) < 0):
            b = c
        else:
            a = c

    print("The value of root is : ", "%.4f" % c)


# Driver code
# Initial values assumed
a = -1
b = 3
bisection(a, b)


####### 11th ########
# False position method

MAX_ITER = 1000000


# An example function whose solution
# is determined using Bisection Method.
# The function is x^3 - x^2 + 2
def func(x):
    return (x * x * x - 2 * x -5)


# Prints root of func(x) in interval [a, b]
def regulaFalsi(a, b):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b")
        return -1

    c = a  # Initialize result

    for i in range(MAX_ITER):

        # Find the point that touches x axis
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))

        # Check if the above found point is root
        if func(c) == 0:
            break

        # Decide the side to repeat the steps
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
    print("The value of root is : ", '%.4f' % c)


# Driver code to test above function
# Initial values assumed
a = -200
b = 300
regulaFalsi(a, b)


