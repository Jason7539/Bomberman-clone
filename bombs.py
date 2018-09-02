# bombs have a damage radius
# pickups:
# increase amount of bombs you can place
# increase the radius of bombs
# bombs can only take out one block at a time

class Bomb():
    def __init__(self):
        self.raduis = 1

    def add_effects(effect):
        """takes a  Pickup object to modify the bomb"""
        name = effect.get_name()
        # if elif else
        pass


class PickUp():

    def __init__(self, name="Default"):
        self.name = name

    def get_name(self):
        return self.name

# make different typ of pickups