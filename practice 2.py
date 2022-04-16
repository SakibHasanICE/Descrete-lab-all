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