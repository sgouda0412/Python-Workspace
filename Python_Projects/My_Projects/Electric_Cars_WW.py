from matplotlib import pyplot as plt

plt.style.use("ggplot")

year_x = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

# Number of electric cars worldwide, in Millions
ecars_y = [0.11, 0.22, 0.4, 0.72, 1.18, 1.93, 3.27, 4.79]

plt.plot(year_x, ecars_y, color="b", marker="o", linewidth=3, label="Electric Cars")

plt.xlabel("Year")
plt.ylabel("Electric Cars in Millions")
plt.title("Increase of Electric Car use worldwide")
plt.grid(True)
plt.legend()
plt.show()
