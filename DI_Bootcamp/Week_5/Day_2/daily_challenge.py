import random as rd

class Gene:

    def __init__(self, gene):
        self.gene = gene

    def mutate(self):
        self.gene = rd.randint(0, 1)
        return self.gene

class Chromsome(Gene):

    def __init__(self, gene):
        super().__init__(gene)
        self.chromsome_list = []

    def chromsome_series(self):
        for i in range(10):
            self.mutate()
            self.chromsome_list.append(self.gene)
        return self.chromsome_list

class DNA(Chromsome):

    def __init__(self, gene):
        super().__init__(gene)
        self.dna_list = []

    def dna_series(self):
        for i in range(10):
            self.chromsome_series()
            self.dna_list.append(self.chromsome_list)
    
            
        print(self.dna_list)

gene_1 = DNA(0)

gene_1.dna_series()