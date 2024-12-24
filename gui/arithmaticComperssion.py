# Initialize an empty dictionary to store the probabilities
probabilities = {}

# List of symbols
def get_valid_probability(symbol):
    while True:
        try:
            value = float(input(f"Enter probability for '{symbol}': "))
            if 0 <= value <= 1:  # Ensure the value is between 0 and 1
                return value
            else:
                print("Probability must be between 0 and 1. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
# List of symbols
#symbols = input("Enter symbols separated by spaces (e.g., 'a b c'): ").split()

# Ask user for the probability of each symbol
#print("Please enter probabilities for each symbol. The total must sum up to 1.")

# for symbol in symbols:
#     while True:
#         try:
#             value = float(input(f"Enter probability for '{symbol}': "))
#             if 0 <= value <= 1:  # Ensure the value is between 0 and 1
#                 probabilities[symbol] = value
#                 break
#             else:
#                 print("Probability must be between 0 and 1. Try again.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")

# Check if the sum of probabilities is equal to 1
# total = sum(probabilities.values())

# if total != 1.0:
#     print(f"Error: The probabilities sum to {total}. They must sum to 1.")
# else:
#     print("Probabilities entered successfully!")
#     print(probabilities)

def getCumulativeProbs(probs):
    cumulative_probs = {}
    cumulative_sum = 0.0
    for symbol, prob in probs.items():
        #print(f"Symbol: {symbol}, Probability: {prob}")
        cumulative_probs[symbol] = cumulative_sum
        cumulative_sum += prob
        #print(cumulative_sum)

    return cumulative_probs


def arithmetic_encode(sequence, probabilities, cumulative_probs):
    low = 0.0
    high = 1.0
    for symbol in sequence:
         range_width = high - low
         high = low + range_width * (cumulative_probs[symbol] +
         probabilities[symbol])
         low = low + range_width * cumulative_probs[symbol]
# Choosing a number within the final interval
    encoded_value = (low + high) / 2
    return encoded_value  


# Input the sequence from the user
#sequence = input("Enter the sequence to encode (e.g., 'abc'): ")
#print(f"Original Sequence: {sequence}")

# Encode the sequence
# Encode the sequence
#encoded_value = arithmetic_encode(sequence, probabilities, cumulative_probs)

# Display full decimal precision
#print(f"Encoded Value: {encoded_value:}")  # Adjust precision as needed
