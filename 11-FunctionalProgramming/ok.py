def calculate_incorrect_percentage(bottle_capacity, tolerance, filled_bottles):
    tolerance_limit = bottle_capacity * tolerance / 100
    incorrect_bottles = list(filter(lambda x: abs(x - bottle_capacity) > tolerance_limit, filled_bottles))
    incorrect_percentage = (len(incorrect_bottles) / len(filled_bottles)) * 100
    return incorrect_percentage

# Input values
bottle_capacity = 500  # in ml
tolerance = 2  # in percentage
filled_bottles = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]

# Calculate and display the result
incorrect_percentage = calculate_incorrect_percentage(bottle_capacity, tolerance, filled_bottles)

print(f"Bottle capacity:    {bottle_capacity}ml")
print(f"Filling tolerance:  {tolerance}%")
print(f"Filled bottles:     {', '.join(map(str, filled_bottles))}")
print(f"Incorrectly filled: {incorrect_percentage}%")