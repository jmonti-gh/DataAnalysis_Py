#bokeh0

from bokeh.plotting import figure, output_file, show

g = figure(title= 'The Title')

y = [i for i in range(9, 0, -1)]
x = y[::-1]

y1 = [i for i in range(1, 9)]

g.line(x, y)
g.line(x, y1)

show(g)