from matplotlib import pyplot as plt

plt.style.use("ggplot")

year_x = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

# % of Python questions asked on Stack Overflow
py_growth = [3.90, 4.20, 5.30, 6.00, 7.10, 8.20, 10.40, 12.00, 13.80]

plt.plot(year_x, py_growth, color="b", marker="o", linewidth=3, 
    label="Python Questions asked on Stack Overflow")

plt.xlabel("Year")
plt.ylabel("% of Stack Overflow Questions")
plt.title("Growth of Python since 2012")
plt.grid(True)
plt.legend()
plt.show()
