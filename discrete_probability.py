import matplotlib.pyplot as plt
import numpy as np

age_distribution = {
    14: 1,
    15: 1,
    16: 3,
    22: 2,
    24: 2,
    25: 5,
}

# j
ages = [*age_distribution]
# N(j)
numbers = [age_distribution[age] for age in ages]

# Plot N(j) vs j
plt.bar(ages, numbers)
plt.ylim(0, 6)
plt.ylabel(r'$N(j)$')
plt.xlim(10, 27)
plt.xlabel(r'$j$')
# plt.show()

# N
total_number = sum(numbers)
print('N = {}'.format(total_number))

# P(15)
probability_distribution = {age: number/total_number for age, number in age_distribution.items()}
print('P(15) = {}'.format(probability_distribution[15]))

# sum of probabilities
probability_sum = sum(probability_distribution[age] for age in ages)
print('sum(P) = {}'.format(probability_sum))

# most probable age
most_probable_age = max(probability_distribution)
print('max(P) = {}'.format(most_probable_age))

# median age

cumulative=0.
for age in ages:
    if cumulative <.5:
        # median_age=int((age+ages.index(age)/2))
        cumulative+=probability_distribution[age]
        # print(age, median_age, cumulative)
# print('P  reaches 0.5 at j={}'.format(median_age))

# average age
mean_age = sum(age*age_distribution[age] for age in ages)/total_number
# or:
mean_age2 = sum(age*probability_distribution[age] for age in ages)
print('<j> = {} = {}'.format(mean_age, mean_age2))

# expectation value of j^2
age_squared_expectation = sum(age**2*probability_distribution[age] for age in ages)
print('<j^2> = {}'.format(age_squared_expectation))
print('<j>^2 = {}'.format(mean_age**2))

# Δj
delta_j = [age-mean_age for age in ages]
print('Δj = {}'.format(delta_j))

# <Δj>
delta_j_expectation = sum((age-mean_age)*probability_distribution[age] for age in ages)
print('<Δj> = {}'.format(delta_j_expectation))

# σ^2
probability_distribution_array = np.array([probability_distribution[age] for age in ages])
variance = np.sum(np.array(delta_j)**2*probability_distribution_array)
print('σ^2 = {} = {}'.format(variance, age_squared_expectation - mean_age**2))

# σ
standard_deviation = np.sqrt(variance)
print('σ = {}'.format(standard_deviation))
