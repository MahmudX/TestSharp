def kitten(**kwargs):
    if len(kwargs):
        for i in kwargs:
            print(f'Kitten {i} says {kwargs[i]}')
        else:
            print('That was all animals.')
    else:
        print('There is no animal left.')


def main():
    x = {'Buffy': 'Meao', 'Zilla': 'Grr', 'Angel': 'rawr'}
    kitten(**x)


if __name__ == "__main__":
    main()
