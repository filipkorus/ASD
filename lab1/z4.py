def main():
    list = [1]
    try:
        print(list[1]) # IndexError
    except IndexError:
        print('IndexError')
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except NameError:
        print('NameError')
    except:
        print('Unknown error')

    try:
        print(1 / 0) # ZeroDivisionError
    except IndexError:
        print('IndexError')
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except NameError:
        print('NameError')
    except:
        print('Unknown error')

    try:
        print(listttt) # NameError
    except IndexError:
        print('IndexError')
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except NameError:
        print('NameError')
    except:
        print('Unknown error')

if __name__ == '__main__':
    main()
