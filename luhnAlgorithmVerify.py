import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <credit_card_number>")
        return
    
    card_number = sys.argv[1]

    # Verify that the input consists only of digits
    if not card_number.isdigit():
        print("Error: The card number must contain only digits.")
        return

    # Convert to a list of integers
    card_numbers = [int(digit) for digit in card_number]

    # Step 1: Double every second digit, starting from the end
    card_numbers = step1(card_numbers)

    # Step 2: Add the digits of numbers greater than 9
    card_numbers = step2(card_numbers)

    # Step 3: Calculate the sum
    total_sum = step3(card_numbers)

    # Step 4: Validate the card number
    if total_sum % 10 == 0:
        print("Valid card")
    else:
        print("Invalid card")

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

if __name__ == "__main__":
    main()
