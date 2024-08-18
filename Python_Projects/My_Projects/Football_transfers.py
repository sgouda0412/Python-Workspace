from matplotlib import pyplot as plt

plt.style.use('seaborn')

years_x = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

la_liga = [31.87, 80.46, 65.06, 30.27, 29.21, 115.51, 57.36, 101.33, 27.88 ]

prem = [31.5, 42.3, 67.5, 68.4, 94.5, 76.23, 72, 78.3, 72]

serie_a = [15.93, 31.07, 19.92, 31.87, 71.7, 33.46, 93.2, 68.11, 57.36]

bund = [35.85, 29.48, 25.49, 34.25, 27.88, 33.06, 22.31, 63.73, 35.86]

plt.plot(years_x, la_liga, color='#cf1322', linewidth=1, label='La Liga')
plt.plot(years_x, prem, color='#8d13cf', linewidth=1, label='Premier League')
plt.plot(years_x, serie_a, color='#1227c4', linewidth=1, label='Serie A')
plt.plot(years_x, bund, color='#19191c', linewidth=1, label='Bundesliga')

plt.xlabel("Season's transfer window")
plt.ylabel('Millions spent on a single player in GBP')
plt.title('Top 4 Football leagues highest transfer spend')
plt.legend()
plt.grid()


plt.show()
