class Bird:

    def eat(self):
        print("Bird is eating")


class FlyingBird(Bird):

    def fly(self):
        print("Bird is flying")


class Sparrow(FlyingBird):

    def fly(self):
        print("Sparrow is flying")


class Penguin(Bird):

    def swim(self):
        print("Penguin is swimming")


def make_bird_eat(bird):
    bird.eat()


def make_flying_bird_fly(bird):
    bird.fly()


sparrow = Sparrow()
penguin = Penguin()

make_bird_eat(sparrow)
make_bird_eat(penguin)

make_flying_bird_fly(sparrow)

penguin.swim()