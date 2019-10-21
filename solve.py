import random, os
from functools import reduce

def readData():
    with open("eil51-tsp.txt") as file:
        lines = file.read().splitlines()[6:-1]
        return list(map(lambda x: list(map(int, x.split(' ')))[1:], lines))

def getDistance(a, b):
    return pow(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2), 0.5)

def getTotalDistance(data):
    return sum([getDistance(j,  data[i-1]) for i, j in enumerate(data)])

def solve(current, n):
    k = 0
    while k < n:
        guess = swapValue(current[:])
        if getTotalDistance(guess) <= getTotalDistance(current):
            k = 0
            current = guess
            #print("update", getTotalDistance(guess))
        else:
            k = k + 1
    current.append(current[0])
    return current

def swapValue(data):
    a = [0 for i in range(2)]
    while a[0] == a[1]:
        a = [random.randint(0, len(data)-1) for i in range(2)]
    data[a[0]], data[a[1]] = data[a[1]], data[a[0]]
    return data

n = 10000
data = readData()
data = solve(data[:], n)
open("output.txt", "w")
for i in data:
    print(i[0], i[1], file=open("output.txt", "a"))
print("distance =", getTotalDistance(data))
os.system("gnuplot run.gp -p")
