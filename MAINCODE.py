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
class Catalyst(Reagent):
    def refine(self):
        self.quality += 3.0
        print(f'{self.name} catalyst refined. Quality is now {self.quality}.')       
class Potion:
    def __init__(self, name, reagents):
        self.name = name
        self.reagents = reagents
    def refine(self):
        for reagent in self.reagents:
            reagent.refine()
class CatalystLab:
    def __init__(self):
        self.catalysts = []

    def add_catalyst(self, catalyst):
        self.catalysts.append(catalyst)

    def find_catalyst_by_name(self, catalyst_name):
        try:
            return next(catalyst for catalyst in self.catalysts if catalyst.name == catalyst_name)
        except StopIteration:
            return None
