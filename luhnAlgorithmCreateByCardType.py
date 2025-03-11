import random

# Dictionary of card types with their prefixes and lengths
CARD_TYPES = {
    "visa": {"prefix": [4], "length": 16},
    "mastercard": {"prefix": list(range(51, 56)) + list(range(2221, 2721)), "length": 16},
    "amex": {"prefix": [34, 37], "length": 15},
    "discover": {"prefix": [6011, 65] + list(range(622126, 622926)), "length": 16}
}

def generate_card_number(card_type):
    card_type = card_type.lower()
    
    if card_type not in CARD_TYPES:
        raise ValueError("Unsupported card type. Choose from: Visa, Mastercard, Amex, Discover")

    # Choose a valid prefix
    prefix = str(random.choice(CARD_TYPES[card_type]["prefix"]))
    length = CARD_TYPES[card_type]["length"]

    # Generate the remaining digits except for the last one
    remaining_length = length - len(prefix) - 1
    random_digits = [random.randint(0, 9) for _ in range(remaining_length)]

    # Construct the base of the card number without the checksum
    card_numbers = [int(digit) for digit in prefix] + random_digits

    # Calculate the last digit (checksum) using the Luhn algorithm
    checksum = calculate_luhn_checksum(card_numbers)
    card_numbers.append(checksum)

    return "".join(map(str, card_numbers))

def calculate_luhn_checksum(card_numbers):
    """ Calculates the last digit to make the number valid according to Luhn """
    temp_numbers = card_numbers[:]  # Copy to avoid modifying the original list
    
    # Step 1: Double every second digit starting from the end
    for i in range(len(temp_numbers) - 1, -1, -2):
        temp_numbers[i] *= 2
        if temp_numbers[i] > 9:
            temp_numbers[i] = temp_numbers[i] // 10 + temp_numbers[i] % 10

    # Step 2: Compute the total sum
    total_sum = sum(temp_numbers)

    # Step 3: Calculate the last digit (checksum)
    return (10 - (total_sum % 10)) % 10

# Example usage
if __name__ == "__main__":
    card_type = input("Enter card type (Visa, Mastercard, Amex, Discover): ").strip().lower()
    try:
        card_number = generate_card_number(card_type)
        print(f"Generated valid {card_type.capitalize()} card number: {card_number}")
    except ValueError as e:
        print(e)
