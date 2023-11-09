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