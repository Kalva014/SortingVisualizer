import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from SortingAlgorithms import *

# Function is used to update the figure for each frame in an animation
def update_plot(array, bars, number_of_operations):
    for bar_in_plot, array_value in zip(bars, array):
        bar_in_plot.set_height(array_value)

# Code is controlled from here
def main():
    # Ask for input
    print("Input the number of elements to be sorted:")
    array_size = int(input())
    print("Select which sorting algorithm to visualize:\n -Bubble Sort\n -Quick Sort\n -Merge Sort")
    algorithm_name = input()
    
    # Create a randomized array with user specified size
    array = list(range(1, array_size + 1))
    random.shuffle(array)

    # Select which algorithm to be displayed
    if algorithm_name == "Bubble Sort":
        title = "Bubble Sort"
        algorithm = bubble_sort(list(array), array_size)
    elif algorithm_name == "Quick Sort":
        title = "Quick Sort"
        algorithm = quick_sort(list(array), 0, array_size - 1)
    elif algorithm_name == "Merge Sort":
        title = "Merge Sort"
        algorithm = merge_sort(list(array), 0, array_size - 1)

    # Create the plot/gui for the animation using matplotlib 
    fig, ax = plt.subplots()
    ax.set_title(title)

    # Create the bar graph where each bar represents one number in the array
    bar = ax.bar(range(len(array)), array, align='edge')
    ax.set_xlim(0, array_size)
    ax.set_ylim(0, int(array_size * 1.1))

    # This could be used if you wanted to display the amount of operations done and is needed to take in all of the inputs
    number_of_operations = [0]

    # Animate the plot by passing in the update plot function which takes in the bar and the sorted array
    anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar, number_of_operations), frames=algorithm, interval=1, repeat=False)

    # Display plot after updating with the animation
    plt.show()

if __name__ == "__main__":
    main()
