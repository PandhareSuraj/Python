def calculate_mean(data):
    return sum(data) / len(data)

def calculate_standard_deviation(data):
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_deviation = variance ** 0.5
    return std_deviation


data_points = [2, 4, 4, 4, 5, 5, 7, 9]
std_dev = calculate_standard_deviation(data_points)
print("Standard Deviation:", std_dev)