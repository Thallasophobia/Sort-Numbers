import statistics

# Take user input for numbers
user_input = input("Enter a list of numbers (space-separated): ")

# Split the input string into a list of numbers
numbers = [int(num) for num in user_input.split()]

# Sort the numbers
sorted_numbers = sorted(numbers)

# Calculate the mean
mean = statistics.mean(numbers)

# Calculate the median
median = statistics.median(numbers)

# Calculate the range
range_val = max(numbers) - min(numbers)

# Print the sorted numbers, mean, median, and range
print("Sorted numbers:", sorted_numbers)
print("Mean:", mean)
print("Median:", median)
print("Range:", range_val)
