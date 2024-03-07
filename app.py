# Import Dependencies
import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Title for Project
ui.page_opts(title="Shiny Project", fillable=True)

# Create a sidebar with a slider input
with ui.sidebar():
    # A a slider for the specifying nunber of bins in the histogram
    # The ui.input_slider function is called with five arguments:
    # A string id ("selected_number_of_bins") that uniquely identifies this input value.
    # A string label ("Number of Bins") to be displayed alongside the slider.
    # An integer representing the minimum number of bins (0).
    # An integer representing the maximum number of bins (100).
    # An integer representing the initial value of the slider (20).
    # A string id ("selected_number_of_bins") that uniquely identifies this input value.
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 40)

# Creating a Histogram
@render.plot(alt="A histogram showing data distribution")
def histogram():
    count_of_points: int = 437
    # Set a random see to ensure reproducibility
    np.random.seed(3)
    # Generate random data:
    random_data_array = 200 + 15 * np.random.rand(count_of_points)
    # Create a histogram of the random data using matplotlib's hist() function:
    plt.hist(random_data_array, input.selected_number_of_bins(), color = 'green', density=True)

# Creating a Scatterplot
@render.plot("Scatterplot", alt="A scatterplot showing data distribution")
def scatterplot():
    np.random.seed(15)  # Ensure reproducibility
    num_points = input.selected_number_of_bins()  
    x = np.random.rand(num_points)
    y = np.random.rand(num_points)
    plt.scatter(x, y, color = 'purple')
    plt.title("Random Scatter Plot with {} Points".format(num_points), color = 'green',)
    plt.xlabel("X-Axis Label", color = 'green')
    plt.ylabel("Y-Axis Label", color = 'green')
