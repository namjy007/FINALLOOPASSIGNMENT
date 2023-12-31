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
# Create an instance of CatalystLab
lab = CatalystLab()

# Create herb reagents
herbs = [
    Herb('Irit', 1.0),
    Herb('Kwuarm', 1.2),
]

# Create catalyst reagents
catalysts = [
    Catalyst('Prismatic Dust', 1.8, 2.0)
]

# Add herbs and catalysts to the lab
for herb in herbs:
    lab.add_catalyst(herb)

for catalyst in catalysts:
    lab.add_catalyst(catalyst)
# Create a potion using the lab's catalysts
invisibility_potion = Potion('Invisibility', lab.catalysts)
# Display the initial properties of the potion
print(invisibility_potion)
# Refine the potion
invisibility_potion.refine()

# Display the refined properties of the potion
print(invisibility_potion)

