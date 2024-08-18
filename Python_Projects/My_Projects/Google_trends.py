from plotly.graph_objs import Bar, Layout
from plotly import offline


prog_langs = ['Python', 'Java', 'JavaScript', 'PHP', 'C++']
percentages = [33.1, 25.5, 22, 10.3, 9.1]

x_values = prog_langs
data = [Bar(x=x_values, y=percentages)]

x_axis_config = {'title': 'Languages'}
y_axis_config = {'title': 'Most Googled Language'}
my_layout = Layout(title='Most Googled programming Languages Worldwide',
                    xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='GT_Prog_langs.html')


