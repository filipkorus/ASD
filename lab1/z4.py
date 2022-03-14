def main():
    list = [1]
    try:
        print(list[1]) # IndexError
    except IndexError:
        print('IndexError')
    except:
        print('Unknown error')

    try:
        print(1 / 0) # ZeroDivisionError
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except:
        print('Unknown error')

    try:
        print(listttt) # NameError
    except NameError:
        print('NameError')
    except:
        print('Unknown error')

if __name__ == '__main__':
    main()
