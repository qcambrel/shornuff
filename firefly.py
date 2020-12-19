# Algorithms for Optimization (Kochenderfer; Wheeler) pg. 159-161
# An implementation of the firefly algorithms in Python (originally Julia)
# NOTE: Requires some tweaks to line 34...

import math
import numpy as np
from scipy.stats import multivariate_normal
from scipy.linalg import norm
from branin import branin

def inverse_square_law(distance):
	intensity_wrt_distance = 1/(distance**2)
	return intensity_wrt_distance

def exponential_decay(light_absorption_coefficient, distance):
	# Avoid due to singularity at distance (r) = 0
	intensity_wrt_distance = math.exp(-1*light_absorption_coefficient*distance)
	return intensity_wrt_distance

def gaussian_brightness_dropoff(light_absorption_coefficient, distance):
	# A combination of the inverse square law and absorption (exponential decay)
	intensity_wrt_distance = math.exp(-1*light_absorption_coefficient*distance**2)
	return intensity_wrt_distance

# A firefly's attraction is proportional to its performance. Attraction affects only
# whether one fly is attracted to another fly, whereas intensity affects how much the
# less attractive fly moves.

def firefly(f, population, k_max, source_intensity=1, step=0.1, brightness=inverse_square_law):
	# The firefly algorithm takes an objective function f, a population flies consisting of
	# design points, a number of iterations k_max, source_intensity (beta), a random walk
	# step size (alpha), and an intensity function brightness (I).
	m = len(population[0])
	N = multivariate_normal.pdf(np.eye(m, M=m))
	for k in range(k_max):
		for a, b in population:
			if f(b) < f(a):
				distance = norm(b-a)
				a += source_intensity * brightness(distance) * (b - a) + step * np.random(N)
	return population[np.argmin([f(x) for x in population])]



if __name__ == '__main__':
	# Using Branin function as per the book example
	flies = np.eye(20, M=2)
	print(firefly(branin, flies, 20))


