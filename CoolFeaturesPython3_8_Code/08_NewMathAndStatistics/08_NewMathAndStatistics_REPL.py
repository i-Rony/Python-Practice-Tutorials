# Example 01
import math
math.prod((2, 8, 7, 7))

2 * 8 * 7 * 7

# Example 02
import math
math.isqrt(9)

math.sqrt(9)

math.isqrt(15)

math.sqrt(15)

# Example 03
import math
point_1 = (16, 25, 20)
point_2 = (8, 15, 14)

math.dist(point_1, point_2)

math.hypot(*point_1)

math.hypot(*point_2)

# Example 04
import statistics
data = [9, 3, 2, 1, 1, 2, 7, 9]
statistics.fmean(data)

statistics.geometric_mean(data)

statistics.multimode(data)

statistics.quantiles(data, n=4)

# Example 05
import random
import statistics
from timeit import timeit

# Create 10,000 random numbers
data = [random.random() for _ in range(10_000)]

# Measure the time it takes to run mean() and fmean()
t_mean = [timeit("statistics.mean(data)", number=100, globals=globals())
            for _ in range(30)]
t_fmean = [timeit("statistics.fmean(data)", number=100, globals=globals())
            for _ in range(30)]

# Create NormalDist objects based on the sampled timings
n_mean = statistics.NormalDist.from_samples(t_mean)
n_fmean = statistics.NormalDist.from_samples(t_fmean)

# Look at sample mean and standard deviation
n_mean.mean, n_mean.stdev

n_fmean.mean, n_fmean.stdev

# Calculate the lower 1 percentile of mean
n_mean.quantiles(n=100)[0]
