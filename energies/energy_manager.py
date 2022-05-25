import numpy as np

import energies.one_pres_per_block as pe

class EnergyManager:
    NEURON_COUNT = 0
    TIME_UNITS_PER_PERSON = 0
    PRESIDENTS_FROM = 0
    PRESIDENTS_TO = 0
    STUDENTS_FROM = 0
    STUDENTS_TO = 0
    energies = []

    def __init__(self, neuron_count):
        self.energies = []
        self.weight_matrix = np.ones((neuron_count, neuron_count),dtype=bytes)  # TODO load
        self.load_energies()
        # TODO initialize values

    # loads energies using add energies
    def load_energies(self):
        (self
            .add_energy(pe.OnePresPerBlock()))

    def add_energy(self, energy):
        self.energies.append(energy)
        return self

    # initializes weight matrix to be used under iteration
    def init_weight_matrix(self):
        pass

    # calculates total energies to evaluate iteration
    def calculate_total_energy(self, neurons):
        total_energy = 0
        for energy in self.energies:
            total_energy += energy.calculate_energy_value(neurons)
        return total_energy

    def calculate_weights(self, neurons, index):
        total_value = 0
        for energy in self.energies:
            energy_value = 0
            for j, neuron in enumerate(neurons):
                energy_value += neuron * energy.weight(i=index, j=j)
            total_value += energy_value
        return total_value
