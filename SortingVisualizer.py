import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim

# Function is used to update the figure for each frame in an animation
def update_plot(bars, array):
    # Use a for loop and a zip function(Combines both of the bar and array element into one object together)
    for bar_in_plot, array_value in zip(bars, array):
        bar_in_plot = set_height(array_value)
    

# Code is controlled from here
def main():
    # Ask for input
    print("Input the number of elements to be sorted:")
    array_size = input()
    print("Select which sorting algorithm to visualize:")
    algorithm_name = input()
    
    # Create a randomized array
    array = []

    for i in range(int(array_size)):
        array.append(i)

    random.shuffle(array)

    # Select which algorithm to be displayed
    if(algorithm_name == "Merge Sort"):
        title = "Merge Sort"
        #merge_sort(array)

    # Create a canvas for the animation using matplotlib 
    figure, axis = plt.subplots()
    axis.set_title(title)

    # Create the bar plot where each bar represents one number in the array
    bar = ax.bar(range(len(array)), array, align='edge')

    # Animate the plot by passing in the update plot function which takes in the bar and the sorted array
    aima = anim.FuncAnimation(figure, func=update_plot, fargs=(bar, array), frames=algo, interval=1, repeat=False)

    # Display plot after updating with the animation
    plt.show()


if __name__ == "__main__":
    main()