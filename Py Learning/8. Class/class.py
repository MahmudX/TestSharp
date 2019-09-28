class Animal:
    def __init__(self, Type, Name, Sound):
        self.type = Type
        self.name = Name
        self.sound = Sound

    def Type(self):
        return self.type

    def Name(self):
        return self.name

    def Sound(self):
        return self.sound

class Animal2:
    def __init__(self, **kwargs):
        self.type = kwargs['type']
        self.name = kwargs['name']
        self.sound = kwargs['sound']

    def Type(self):
        return self.type

    def Name(self):
        return self.name

    def Sound(self):
        return self.sound

def PrintAnimal(animal):
    # if not isinstance(animal, Animal):
    if not isinstance(animal, Animal2):
        raise TypeError('Passed parameter must be an animal.')
    else:
        print(
            f'The {animal.Type()}\'s name is {animal.Name()} and it sounds {animal.Sound()}')


def main():
    # PrintAnimal(Animal('Duck', 'Donald', 'Quaaak!'))
    # cat = Animal('Kitten', 'Fluffy', 'Meaw')
    # PrintAnimal(cat)
    anotherCat = Animal2(type = 'Cat', sound = 'Rrrr', name = 'Tom')
    PrintAnimal(anotherCat)

if __name__ == "__main__":
    main()
