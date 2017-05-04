import sys
import math
import random

number_of_iterations = [10, 100, 1000, 10000, 1000000]

def in_circle(x, y):
    radius = 1
    if (math.sqrt((x**2) + (y**2)) <= radius):
        return True
    

def step():
    directions = [0, 1, -1]
    multiplier = random.uniform(0.2, 0.3)
    ret = random.choice(directions) * multiplier
    return ret

def new_point(last_position):
    a = step()
    b = step()
    a = last_position[0] + a
    b = last_position[1] + b
    x = [a, b]
    return x


def main():
    m = 1
    last_point = [0, 0]
    for i in range(0, 5):
        cnt = 0
        for j in range(0, number_of_iterations[i]):
            point = new_point(last_point)
            if (in_circle(point[0], point[1])):
                cnt += 1
                last_point = [point[0], point[1]]

        ans = (cnt/number_of_iterations[i])*4.0
        print("For iteration %d with amout count of iterations of %d answer is %f" %(m, i, ans))
        m += 1
        cnt = 0
        last_point=[0,0]

main()