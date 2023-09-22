import pandas as pd

# read & print csv file
sailboats_data = pd.read_csv("sailboats.csv")
print(sailboats_data)

# calculate mean of  nr_sailboats column
mean = sailboats_data['nr_sailboats'].mean()
print(mean)

# calculate standard deviation of nr_sailboats column
standard_deviation = sailboats_data['nr_sailboats'].std()
print(standard_deviation)

# calculate monthly cost of sailboats
fixed_monthly_cost = 30000
cost_per_sailboat = 4800
cost = fixed_monthly_cost + cost_per_sailboat * sailboats_data['nr_sailboats']
print(cost)

# calculate mean and standard deviation of monthly cost
mean_cost = cost.mean()
print(mean_cost)

standard_deviation_cost = cost.std() 
print(standard_deviation_cost)

# calculate monthly cost of sailboats when fixed cost is 53000
fixed_monthly_cost_b = 53000
cost_per_sailboat_b = 4800
cost_b = fixed_monthly_cost_b + cost_per_sailboat_b * sailboats_data['nr_sailboats']
print(cost_b)

# calculate mean and standard deviation of monthly cost
mean_cost_b = cost_b.mean()
print(mean_cost_b)

standard_deviation_cost_b = cost_b.std() 
print(standard_deviation_cost_b)

# calculate monthly cost of sailboats when fixed cost is 30000 and cost per sailboat is 7000
fixed_monthly_cost_c = 30000
cost_per_sailboat_c = 7000
cost_c = fixed_monthly_cost_c + cost_per_sailboat_c * sailboats_data['nr_sailboats']
print(cost_c)

# calculate mean and standard deviation of monthly cost
mean_cost_c = cost_c.mean()
print(mean_cost_c)

standard_deviation_cost_c = cost_c.std() 
print(standard_deviation_cost_c)

# Umbrella Sales
# read & print csv file
umbrella_data = pd.read_csv("umbrella.csv")
print(umbrella_data)

# calculate mean and standard deviation of umbrellas from department and outlet stores 
mean_department= umbrella_data['department'].mean()
print(mean_department)
mean_outlet = umbrella_data['outlet'].mean()
print(mean_outlet)

standard_deviation_department = umbrella_data['department'].std()
print(standard_deviation_department)
standard_deviation_outlet = umbrella_data['outlet'].std()
print(standard_deviation_outlet)

# calculate correlation between department and outlet stores
correlation = 0.7
correlation_total = correlation * standard_deviation_department * standard_deviation_outlet
print(correlation_total)

# set cost of umbrella
cost_department = 17
cost_outlet = 9

# calculate mean and standard deviation of cost of umbrella
mean_total = mean_department * cost_department + mean_outlet * cost_outlet
print(mean_total)
standard_deviation_total = correlation_total * cost_department * cost_outlet
print(standard_deviation_total)