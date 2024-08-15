

from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline

class Roulette():
    
    def __init__(self, numbers=36):
        self.numbers = numbers
        
    def spin(self):
        return randint(0, self.numbers)
    
table = Roulette()

results = []

for num in range(1000):
    result = table.spin()
    results.append(result)
    
frequencies = []

for value in range(0, table.numbers+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
x_values = list(range(0, table.numbers+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of spinning a Roulette table 1000 times',
                  xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='RTable.html')

