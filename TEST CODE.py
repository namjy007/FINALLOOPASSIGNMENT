
class Reagent:
    def __init__(self, name, potency, quality=None):
        self.name = name
        self.potency = potency
        self.quality = quality

    def __str__(self):
        return f'{self.name}: Potency {self.potency}'


class Herb(Reagent):
    pass


class Catalyst(Reagent):
    def __str__(self):
        return f'{self.name}: Potency {self.potency}, Quality {self.quality}'


class Potion:
    def __init__(self, name, reagents):
        self.name = name
        self.reagents = reagents

    def potency(self):
        return sum(reagent.potency for reagent in self.reagents)

    def quality(self):
        qualities = [reagent.quality for reagent in self.reagents if reagent.quality is not None]
        if qualities:
            return sum(qualities) / len(qualities)
        else:
            return None

    def __str__(self):
        reagent_list = ', '.join(str(reagent) for reagent in self.reagents)
        return f'{self.name} Potion: Reagents [{reagent_list}]'


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

# Add some catalysts to the lab
lab.add_catalyst(Catalyst('Base Catalyst', 1.0, 3.0))
lab.add_catalyst(Catalyst('Essence of Magic', 2.0, 2.5))
lab.add_catalyst(Catalyst('Mystic Shards', 1.5, 1.8))
lab.add_catalyst(Catalyst('Prismatic Dust', 1.8, 2.0))

# Find a catalyst by name
catalyst_name = 'Essence of Magic'
found_catalyst = lab.find_catalyst_by_name(catalyst_name)

# Display the found catalyst or a message if not found
if found_catalyst is not None:
    print(f'Found catalyst: {found_catalyst}')
else:
    print(f'Catalyst with name "{catalyst_name}" not found.')

# Attempt to refine "Eye of Newt"
eye_of_newt = Reagent('Eye of Newt', 1.2)
print(f'\nAttempting to refine {eye_of_newt}...')
refined_quality = eye_of_newt.quality  # Attempt to access the quality attribute
if refined_quality is None:
    print('Eye of Newt cannot be refined any further. Quality set to 10.')

# Add the refined "Eye of Newt" to the lab
lab.add_catalyst(eye_of_newt)

# Display all catalysts in the lab
print('\nCatalysts in the lab:')
for catalyst in lab.catalysts:
    print(catalyst)
