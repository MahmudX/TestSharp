class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type']
        self._name = kwargs['name']
        self._sound = kwargs['sound']

    def type(self, t=None):
        if t:
            self._type = t
        return self._type

    def name(self, t=None):
        if t:
            self._name = t
        return self._name

    def sound(self, t=None):
        if t:
            self._sound = t
        return self._sound

    def __str__(self):
        return f'The {self.type()}\'s name is {self.name()} and it sounds {self.sound()}'


def PrintAnimal(animal):
    if not isinstance(animal, Animal):
        raise TypeError('Passed parameter must be an animal.')
    else:
        print(
            f'The {animal.type()}\'s name is {animal.name()} and it sounds {animal.sound()}')


def main():

    anotherCat = Animal(type='Cat', sound='Rrrr', name='Tom')
    print(anotherCat)
    anotherCat.type('tiger')
    PrintAnimal(anotherCat)


if __name__ == "__main__":
    main()
