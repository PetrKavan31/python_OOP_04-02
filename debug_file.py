
# veta = 'Na železnici za Čelákovicemi ve směru na Prahu došlo k poruše trakčního vedení, potvrdil pro CNN Prima NEWS tiskový mluvčí Českých drah Filip Medelský. Incident je vyšetřován jako mimořádná událost.'
#
# #1
# mySet = set()
# for _ in veta:
#   mySet.add(_)
# print(mySet)
# #mySet = set(veta)
#
# #2
# for _ in mySet:
#   print(_  + " " + str(veta.count(_)))


# task 1 from ITNetwork for debugging
# n = 10
# for i in range(n):
#     for j in range(n):
#         print(i * j, end=" ")
#     print()



# task 2 from ITNetwork for debugging
import random


def bubble_sort(randomlist):
    for passnum in range(len(randomlist)-1, 0, -1):
        for i in range(passnum):
            if randomlist[i] > randomlist[i + 1]:
                temp = randomlist[i + 1]
                randomlist[i] = randomlist[i]
                randomlist[i + 1] = temp


randomlist = random.sample(range(1, 50), 5)
print(randomlist)

bubble_sort(randomlist)
print(randomlist)
