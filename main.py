from bokeh.plotting import figure, output_file, show
import pandas

# Read from CSV (direct data source)
df = pandas.read_csv('cars.csv')

car = df['Car']
hp = df['Horsepower']
price = df['Price']

output_file('index.html')

# creating plot
p = figure(
    y_range=car,
    plot_width=1400,
    plot_height=700,
    title='Cars with most HP',
    x_axis_label='Horsepower',
    tools='save'
)

# render chart
p.hbar(
    y=car,
    right=hp,
    left=0,
    height=0.5,
    color='blue',
    fill_alpha=0.5
)

# plot results
show(p)
