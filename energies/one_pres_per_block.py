from energies import energy as e


class OnePresPerBlock(e.Energy):

    def __init__(self, gamma):
        super().__init__(gamma)

    def weight(self, i, j):
        # TODO calculate weight ...
        pass

    def calculate_energy_value(self, neurons):
        # TODO calculate energy value :)
        pass



