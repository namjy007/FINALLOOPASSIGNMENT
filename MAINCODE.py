class Reagent:
    def __init__(self, name, potency, quality=None):
        self.name = name
        self.potency = potency
        self.quality = quality

    def __str__(self):
        if self.quality is not None:
            return f'{self.name}: Potency {self.potency}, Quality {self.quality}'
        else:
            return f'{self.name}: Potency {self.potency}'
class Herb(Reagent):
    def refine(self):
        self.potency += 1.25
        print(f'{self.name} herb refined. Potency is now {self.potency}.')
class Potion:
    def __init__(self, name, reagents):
        self.name = name
        self.reagents = reagents