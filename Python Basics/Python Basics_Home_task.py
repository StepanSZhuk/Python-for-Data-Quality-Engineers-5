# Import the library 'random'
import random

# 1. Create list of 100 random numbers from 0 to 1000 using 'random.randint' and list comprehension
random_list = [random.randint(0, 1000) for x in range(100)]


# 2. Sort list from min to max (without using sort())
# Using cycle 'for' to sort list 'random_list'
# iterate by list 'random_list'
for i in range(len(random_list)):
    # taking the next value after number 'i'
    for j in range(i + 1, len(random_list)):
        # comparing numbers
        if random_list[i] > random_list[j]:
            # sorting numbers by condition above
            random_list[i], random_list[j] = random_list[j], random_list[i]


# 3. Calculate average for even and odd numbers
# creating list of odd numbers using 'filter' and lambda functions using list 'random_list'
odd_list = list(filter(lambda x: (x % 2 != 0), random_list))
# creating list of even numbers using 'filter' and lambda functions using list 'random_list'
even_list = list(filter(lambda x: (x % 2 == 0), random_list))


# Calculate average for odd numbers
avg_odd_list = sum(odd_list)/len(odd_list)
# Calculate average for even numbers
avg_even_list = sum(even_list)/len(even_list)

# 4. Print both average result in console
# Print average for odd numbers
print(f"The average for odd numbers is {avg_odd_list}")
# Print average for even numbers
print(f"The average for even numbers is {avg_even_list}")
