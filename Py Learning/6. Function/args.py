def kitten(*args):
    if len(args):
        for i in args:
            print(i)
        else:
            print('That was all animals.')
    else:
        print('There is no animal left.')


def main():
    kitten()


if __name__ == "__main__":
    main()
