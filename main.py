import numpy as np
import matplotlib.pyplot as plt
from wag_the_dog import wag_the_dog
from wave_functions import plot_wave_function


def main():
    # Infinite square well wag the dog
    # well_width = 1.0
    # positions = np.linspace(0., well_width)
    # k_squared = (np.pi / well_width)**2  # k_1 = pi/a ==> k_1^2 = pi^2 / a^2
    # wag_range = np.linspace(3.5, 5.5, num=5)
    # adjustable_coefficients = k_squared * wag_range
    # initial_conditions = (0., 1.)  # psi(0), psi'(0)
    # wag_the_dog('infinite square well', adjustable_coefficients, well_width, positions, initial_conditions)

    # Harmonic oscillator plot
    n = int(input('Input Energy State:'))
    potential_width = 1.0
    positions = np.linspace(-3 * potential_width, 3 * potential_width, num=1000)
    indices = np.arange(0, 4)
    wag_range = np.linspace(.99, 1.01, num=5)
    k = 2*n + 1
    adjustable_coefficient = k * wag_range
    if n == (0, 2):
        initial_conditions = (0., 1.)
    else:
        initial_conditions = (1, 0)
    plot_wave_function('harmonic oscillator', potential_width, positions, indices, plot_probability=True)
    wag_the_dog('harmonic oscillator', adjustable_coefficient, potential_width, positions, initial_conditions)


if __name__ == "__main__":
    main()

