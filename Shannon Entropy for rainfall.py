
import math

# Monthly rainfall measurements in millimeters (mm)
rainfall = {
    "New York": {
        "January": 85,
        "February": 78,
        "March": 102,
        "April": 110,
        "May": 105,
        "June": 95,
        "July": 100,
        "August": 98,
        "September": 90,
        "October": 88,
        "November": 82,
        "December": 87
    },

    "Seattle": {
        "January": 140,
        "February": 95,
        "March": 100,
        "April": 80,
        "May": 60,
        "June": 45,
        "July": 20,
        "August": 25,
        "September": 55,
        "October": 90,
        "November": 130,
        "December": 145
    },

    "Miami": {
        "January": 55,
        "February": 50,
        "March": 65,
        "April": 75,
        "May": 120,
        "June": 180,
        "July": 170,
        "August": 175,
        "September": 190,
        "October": 160,
        "November": 80,
        "December": 60
    },

    "Phoenix": {
        "January": 20,
        "February": 25,
        "March": 20,
        "April": 10,
        "May": 5,
        "June": 2,
        "July": 25,
        "August": 30,
        "September": 15,
        "October": 15,
        "November": 15,
        "December": 20
    }
}


def shannon_entropy(monthly_rainfall):
    # Calculate the total rainfall for the year
    total = sum(monthly_rainfall.values())

    # Start the entropy calculation at zero
    entropy = 0

    # Calculate the probability and entropy contribution for each month
    for rainfall_amount in monthly_rainfall.values():
        probability = rainfall_amount / total

        if probability > 0:
            entropy -= probability * math.log2(probability)

    return entropy


# Calculate and display entropy for each city
print("Monthly Rainfall Shannon Entropy")
print("-" * 40)

for city, monthly_rainfall in rainfall.items():
    entropy = shannon_entropy(monthly_rainfall)
    print(f"{city}: {entropy:.3f} bits")
