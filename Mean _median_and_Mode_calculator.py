
list = [2, 4,2, 5, 2, 6, 7,2, 3, 6, 1, 3, 8,3]

# Finding the mean
mean =(sum(list)/len(list))
print(f"mean:{mean:.2f}")

# Finding the median
sorted_data = sorted(list)
n = len(list)
if n % 2 == 0:
    median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
else:
    median = sorted_data[n // 2]
print(f"Median: {median}")

# Finding the mode
frequency = {}
for num in list:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

max_freq = 0
mode = []
for key in frequency:
    if frequency[key] > max_freq:
        max_freq = frequency[key]
        mode = [key]
    elif frequency[key] == max_freq:
        mode.append(key)

# If there are multiple modes, sort them
mode.sort()
print(f"Mode: {mode}")
