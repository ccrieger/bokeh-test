from bokeh.plotting import figure, output_file, show

x = [1, 2, 3, 4, 5]
y = [2, 5, 4, 1, 6]

output_file('index.html')

# adding plot
p = figure(
    title='Simple Example',
    x_axis_label='X',
    y_axis_label='Y'
)

# render
p.line(x, y, legend="Test", line_width=2)

# plot results
show(p)
