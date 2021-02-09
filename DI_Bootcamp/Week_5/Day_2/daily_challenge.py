import random as rd

class Gene:

    def __init__(self):
        self.gene = rd.randint(0, 1)


    def mutate(self):
        self.gene = 1 if self.gene == 0 else 0
        # self.gene = int(not bool(self.gene)) same like up

    def __repr__(self):
        return f"{self.gene}"
        # Shows a string representation of the class
        

class Chromsome:

    def __init__(self):
        self.gene = [Gene() for _ in range(10)]

    def mutate(self):
        for gene in self.gene:
            if rd.random() > 0.5:
                gene.mutate()

    def __repr__(self):
        return f"{self.gene}"

class DNA:

    def __init__(self):
        self.gene = [Chromsome() for _ in range(10)]

    def __repr__(self):
        return f"{self.gene}"



c = DNA()
print(c.gene)