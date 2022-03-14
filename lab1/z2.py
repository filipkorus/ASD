from array import *
from time import time

def main():
    start = time()
    L = array('d', [1, 2])
    for i in range(46):
        L.append((L[-1] + L[-2]) / (L[-1] - L[-2]))

    print(L)
    print('average =', sum(L) / len(L))
    print('median =', Median(L))

    counter = {item: L.count(item) for item in L}
    print('mod =', get_mod(counter))

    flag = True
    for el in counter:
        if counter[el] > 1:
            flag = False
            print(el)

    if flag:
        print('No elements found')

    print('time =', time() - start)

def get_mod(counter):
    #  counter[5.0] = 2
    #  counter[1] = 5
    counter_sorted = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
    counter_sorted_list = list(counter_sorted.values())

    first_element = counter_sorted_list[0]
    if counter_sorted_list.count(first_element) == len(counter_sorted):
        return 'no mod found'
    else:
        res_list = []
        for i in range(counter_sorted_list.count(first_element)):
            res_list.append(list(counter_sorted)[i])
        return res_list

def Median(L):
    L = sorted(L)
    return L[len(L) // 2] if len(L) % 2 == 1 else (L[len(L) // 2 - 1] + L[len(L) // 2]) / 2

if __name__ == '__main__':
    main()
