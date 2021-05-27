"""As second task: you have the list of symbols (example: a, b, c, c, a (it’s very primitive)).
You should write function that returns the first repeating element from this list (in our example it’s “c”)."""

import time
from collections import Counter

lst = input('Enter your text: ').split(' ')

em1 = []
em2 = set()
em3 = Counter(lst)

def first_repeat_1(a):
    for i in lst:
        if i in em1:
            print(i)
            break
        else:
            em1.append(i)
    tm = time.time()-start
    print('Lead time 1: ' + str(tm) + ' sec')

def first_repeat_2(a):
    for i in lst:
        if i in em2:
            print(i)
            break
        else:
            em2.add(i)
    tm = time.time()-start
    print('Lead time 2: ' + str(tm) + ' sec')

# def first_repeat_2(a):
# start = time.time()
# for i in em3:
#     if em3[i] > 1:
#         print(i)
#         break
# tm = time.time()-start
# if len(em3) == len(lst):
#     print('No repeating words')
# print('Lead time 3: ' + str(tm) + ' sec')

start = time.time()
first_repeat_1(lst)
if len(em1) == len(lst):
    print('No repeating words')

start = time.time()
first_repeat_2(lst)
if len(em2) == len(lst):
    print('No repeating words')