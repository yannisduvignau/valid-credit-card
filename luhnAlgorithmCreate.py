import random

def generate_card_number():
    # Generate the first 15 digits randomly
    card_numbers = [random.randint(0, 9) for _ in range(15)]
    
    # Step 1: Apply Luhn algorithm to calculate the last digit (checksum)
    card_numbers_with_checksum = card_numbers + [0]  # Placeholder for checksum
    card_numbers_with_checksum = step1(card_numbers_with_checksum)
    card_numbers_with_checksum = step2(card_numbers_with_checksum)
    
    total_sum = step3(card_numbers_with_checksum)
    
    # Calculate the last digit to make the sum a multiple of 10
    checksum = (10 - (total_sum % 10)) % 10
    
    # Add the checksum to complete the card number
    card_numbers.append(checksum)
    
    return "".join(map(str, card_numbers))

def step1(card_numbers: list):
    # Double every second digit starting from the end
    for i in range(len(card_numbers) - 2, -1, -2):
        card_numbers[i] *= 2
    return card_numbers

def step2(card_numbers: list):
    # If a number is greater than 9, sum its digits
    for i in range(len(card_numbers)):
        if card_numbers[i] > 9:
            card_numbers[i] = card_numbers[i] // 10 + card_numbers[i] % 10
    return card_numbers

def step3(card_numbers: list):
    # Return the total sum
    return sum(card_numbers)

# Generate and print a valid card number
if __name__ == "__main__":
    print("Generated valid card number:", generate_card_number())
