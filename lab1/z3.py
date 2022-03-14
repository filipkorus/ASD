from time import time

def main():
    list = [5] * 100000000

    # 3.1
    start_py = time()
    for item in list:
        c = 100 + 200
    end_py = time()

    # 3.2
    start_cpp = time()
    for i in range(0, len(list)):
        c = 100 + 200
    end_cpp = time()

    print('C++ for time:', end_cpp - start_cpp)
    print('Python for time:', end_py - start_py)
    # 3.3
    # TAK, zwracaja takie same

if __name__ == '__main__':
    main()
