import matplotlib.pyplot as plt

year = [1990,1991,1992,1993,1994,1995,1996,1997,1998,2000,2001,2002,2003,2004]
pop = [2.480,2.280,2.180,2.80,2.420,2.580,2.780,2.3480,2.450,2.680,2.880,2.580,2.480,2.480,]

plt.plot(year, pop)

plt.xlabel('year')
plt.ylabel('pop')
plt.xlabel('World population Projections')

plt.show()

