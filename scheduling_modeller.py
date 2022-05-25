import numpy as np

import utils
from import_export import input
from energies import energy_manager as em
import copy
import random

file_name = "Input_teljesZV/input01_beosztas_output.xlsx"


def activation_function(value, iter_count, fun):
    return fun(value, iter_count)


# Returns true if the Hopfield Network is stable
def network_is_stable(old_state, new_state):
    for i, _ in enumerate(old_state):
        if old_state[i] != new_state[i]:
            return False
    return True


class SchedulingModeller:
    NO_PRESIDENTS = 0
    NO_SECRETARIES = 0
    NO_INSTRUCTORS = 0
    NO_STUDENTS = 0
    NO_TIMESLOTS = 0
    NO_TIMESLOTS_PER_HOUR = 12
    NO_TIMESLOTS_PER_DAY = 0
    NO_HOURS_PER_DAY = 10
    NO_DAYS = 0
    NO_HOURS = 0
    NO_NEURONS = 0
    NO_ROOMS = 4

    def __init__(self):
        self.input = input.InputManager(file_name, SchedulingModeller.NO_TIMESLOTS_PER_HOUR)

        self.students = self.input.process_students()
        self.instructors = self.input.process_instructors()
        self.courses = self.input.process_courses()

        SchedulingModeller.NO_TIMESLOTS = self.input.time_slices
        SchedulingModeller.NO_HOURS = SchedulingModeller.NO_TIMESLOTS // SchedulingModeller.NO_TIMESLOTS_PER_HOUR
        SchedulingModeller.NO_DAYS = SchedulingModeller.NO_HOURS // SchedulingModeller.NO_HOURS_PER_DAY
        SchedulingModeller.NO_TIMESLOTS_PER_DAY = SchedulingModeller.NO_TIMESLOTS // SchedulingModeller.NO_DAYS
        SchedulingModeller.NO_STUDENTS = len(self.students)
        SchedulingModeller.NO_INSTRUCTORS = len(self.instructors)
        SchedulingModeller.NO_PRESIDENTS = self.num_of_instructors(lambda i: i.president)
        SchedulingModeller.NO_SECRETARIES = self.num_of_instructors(lambda i: i.secretary)
        self.neurons = []
        self.initialize_neural_network()
        self.energy_manager = em.EnergyManager(self.NO_NEURONS)

    def initialize_neural_network(self):
        # Count of neurons
        # X0 constant 1 neuron
        # Rooms = 4
        SchedulingModeller.NO_NEURONS = 1  # Constant neuron with value of 1
        SchedulingModeller.NO_NEURONS += (2 * SchedulingModeller.NO_ROOMS * SchedulingModeller.NO_DAYS *
                                          (SchedulingModeller.NO_PRESIDENTS + SchedulingModeller.NO_SECRETARIES +
                                           SchedulingModeller.NO_TIMESLOTS_PER_DAY))
        SchedulingModeller.NO_NEURONS += (SchedulingModeller.NO_ROOMS * 3 * SchedulingModeller.NO_INSTRUCTORS
                                          * SchedulingModeller.NO_TIMESLOTS)
        SchedulingModeller.NO_NEURONS += (SchedulingModeller.NO_ROOMS * SchedulingModeller.NO_STUDENTS
                                          * SchedulingModeller.NO_TIMESLOTS)
        self.neurons = np.ones(SchedulingModeller.NO_NEURONS, int)
        self.random_seed(self.neurons[1:])
        self.neurons[0] = 1
        # TODO heuristics

    def random_seed(self, neurons):
        for neuron in neurons:
            neuron = random.randint(0, 1)

    def solve_hopfield(self):
        self.general_solver(utils.step)

    def solve_boltzmann(self):
        self.general_solver(utils.sigmoid_choose_random)

    def general_solver(self, activation_fun):
        stable = False
        iteration_count = 0
        previous_state = copy.deepcopy(self.neurons)
        while not stable:
            iteration_count += 1
            for i, neuron in enumerate(self.neurons[1:], 1):
                weight_sum = self.energy_manager.calculate_weights(self.neurons, i)
                neuron = activation_function(weight_sum, iteration_count, activation_fun)
            stable = network_is_stable(previous_state, self.neurons)

    def num_of_instructors(self, condition):
        return len(list(filter(condition, self.instructors)))
