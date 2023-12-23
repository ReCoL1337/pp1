# Medal data
medal_data = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7}
]

# Function to print a vertical bar chart for each type of medal
def print_vertical_bar_chart(medal_type):
    print(f"\n{medal_type} Medal Chart:")
    
    max_count = max(country_data[medal_type] for country_data in medal_data)

    for i in range(max_count, 0, -1):
        line = ' '.join('*'.ljust(10) if country_data[medal_type] >= i else ' '.ljust(10) for country_data in medal_data)
        print(line)

    country_names = ' '.join(country_data['country'].ljust(10) for country_data in medal_data)
    print(country_names)

# Print vertical bar charts for each type of medal
print_vertical_bar_chart("gold")
print_vertical_bar_chart("silver")
print_vertical_bar_chart("bronze")
