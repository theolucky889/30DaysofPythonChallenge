# Exercise Level 1
'''
1. Python has the module called statistics and we can use this module to do all the statistical
calculations. However, to learn how to make function and reuse function, let us try to develop
a program, which calculates the measure of central tendency of a sample(mean, median, mode) and
measure of variability(range, variance, standard deviation). In addition to those measures, 
find the min, max, count, percentile, and frequency distribution of the sample. You can create
a class called Statistics and create all the functions that do statistical calculations as
methods for the statistics class.
Output:
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range() # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

# your output should look like this
print(data.describe())
Count: 25
Sum:  744
Min:  24
Max:  38
Range:  14
Mean:  30
Median:  29
Mode:  (26, 5)
Variance:  17.5
Standard Deviation:  4.2
Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
'''
from statistics import mean, median, mode, stdev, variance

class Statistics:
    def __init__(self, data):
        self.data = data
        self.count = len(data)
        self.sum = sum(data)
        self.min = min(data)
        self.max = max(data)
        self.range = self.max - self.min
        self.mean = mean(data)
        self.median = median(data)
        self.mode = mode(data)
        self.standarddeviation = stdev(data)
        self.variance = variance(data)
        self.frequencydistribution = self.calculate_frequency_distribution
    
    def calculate_frequency_distribution(self):
        frequency = {}
        for item in self.data:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1
        return sorted([(value, key)for key, value in frequency.items()])

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

stats = Statistics(ages)

print('Count:', stats.count) # 25
print('Sum: ', stats.sum) # 744
print('Min: ', stats.min) # 24
print('Max: ', stats.max) # 38
print('Range: ',stats.range) # 14
print('Mean: ', stats.mean) # 30
print('Median: ', stats.median) # 29
print('Mode: ', stats.mode) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', stats.standarddeviation) # 4.2
print('Variance: ', stats.variance) # 17.5
print('Frequency Distribution: ', stats.frequencydistribution) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

'''
# statistics_module.py

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        midpoint = n // 2
        if n % 2 == 1:
            return sorted_data[midpoint]
        else:
            return (sorted_data[midpoint - 1] + sorted_data[midpoint]) / 2

    def mode(self):
        frequency = {}
        for num in self.data:
            frequency[num] = frequency.get(num, 0) + 1
        max_frequency = max(frequency.values())
        modes = {value: count for value, count in frequency.items() if count == max_frequency}
        return modes

    def std(self):
        mean = self.mean()
        return (sum((x - mean) ** 2 for x in self.data) / (self.count() - 1)) ** 0.5

    def var(self):
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / (self.count() - 1)

    def freq_dist(self):
        frequency = {}
        for num in self.data:
            frequency[num] = frequency.get(num, 0) + 1
        total = self.count()
        return sorted([(round((count / total) * 100, 2), num) for num, count in frequency.items()], reverse=True)

# main.py or any Python script

from statistics_module import Statistics

# Data for analysis
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

# Create an instance of Statistics
data = Statistics(ages)

# Print the results using the methods from the Statistics class
print('Count:', data.count())  # Output will be 25
print('Sum: ', data.sum())  # Output will be 744
print('Min: ', data.min())  # Output will be 24
print('Max: ', data.max())  # Output will be 38
print('Range: ', data.range())  # Output will be 14
print('Mean: ', data.mean())  # Output will be 30
print('Median: ', data.median())  # Output will be 29
print('Mode: ', data.mode())  # Output will show modes and counts
print('Standard Deviation: ', data.std())  # Output will be approximately 4.2
print('Variance: ', data.var())  # Output will be approximately 17.5
print('Frequency Distribution: ', data.freq_dist())  # Output will show the frequency distribution

'''

# Exercise Level 2
'''
Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties
and it has total_income, total_expense, account_info, add_income, add_expense and account_balance
methods. Income is a set of incomes and its description. The same goes for expenses
'''

class PersonAccount:
    def __init__(self, account, firstname, lastname, expenses):
        self.account = account
        self.firstname = firstname
        self.lastname = lastname
        self.expenses = self.account - self.expenses
    
    
    def incomes(self, desc):
        income = self.account + self.incomes
        return(f'Your Total income is {income}')
    
    def expense_prop(self, total_income, total_expense, account_info, add_income, add_expense, account_balance):
        