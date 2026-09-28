class Bird:

    def fly(self):
        print("Bird is flying")


class Sparrow(Bird):

    def fly(self):
        print("Sparrow is flying")


class Penguin(Bird):

    def fly(self):
        raise NotImplementedError(
            "Penguin cannot fly"
        )


def make_bird_fly(bird):
    bird.fly()


sparrow = Sparrow()
make_bird_fly(sparrow)

penguin = Penguin()
make_bird_fly(penguin)