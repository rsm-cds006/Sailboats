import scipy.stats as stats

# 3.4 a 
a = stats.norm.cdf(50000, 61000, 9000)
print(a)

# 3.4 c
c = stats.norm.cdf(57000, 61000, 9000) - stats.norm.cdf(42000, 61000, 9000)
print(c)

# 3.4 d
d = stats.norm.ppf(0.8, 61000, 9000) 
print(d)

# 3.18 b
b = stats.binom.cdf(5, 2000, 0.3)
print(b)

# 3.8 d
d2 = stats.norm.cdf(0.15, 0.12, 0.054) - stats.norm.cdf(0.1, 0.12, 0.054)
print(d2)