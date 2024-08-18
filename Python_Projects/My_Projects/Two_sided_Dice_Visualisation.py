from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline


class Die:
    """A Class representing a single Die"""
    def __init__(self, num_sides=6):
        """Create a 6 Sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides"""
        return randint(1, self.num_sides)


# Creation of two dice
die_1 = Die()
die_2 = Die()

results = []

for num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []

max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two 6 sided dice, 1000 times', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='2_d6.html')
