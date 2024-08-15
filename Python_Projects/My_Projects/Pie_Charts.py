import matplotlib.pyplot as plt

labels = 'Python', 'Java', 'Javascript', 'PHP', 'C++'
sizes = [33.1, 25.5, 22, 10.3, 9.1]

transform = (0.1, 0, 0, 0, 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=transform, labels=labels, 
        autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
plt.show()
