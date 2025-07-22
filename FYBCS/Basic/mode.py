def calculate_mode(data):
    frequency_dict = {}
    for value in data: frequency_dict[value] = frequency_dict.get(value, 0) + 1
    max_frequency = max(frequency_dict.values())
    mode = [key for key, value in frequency_dict.items() if value == max_frequency]
    return mode

data_points = [3, 2, 5, 4, 6, 7, 4]
modes = calculate_mode(data_points)
print("Mode(s):", modes)
