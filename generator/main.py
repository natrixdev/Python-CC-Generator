import random
from datetime import datetime, timedelta

def generate_credit_card():
    card_number = input("Enter the credit card number: ")

    # Generate a random expiration date (valid for the next 10 years)
    current_year = datetime.now().year
    expiration_year = random.randint(current_year, current_year + 10)
    expiration_month = random.randint(1, 12)
    expiration_date = datetime(expiration_year, expiration_month, 1) + timedelta(days=30)
    expiration_date = expiration_date.strftime("%m/%Y")

    # Generate a random CVV (3-digit number)
    cvv = random.randint(100, 999)

    return card_number, expiration_date, cvv

# Generate the credit card details
card_number, expiration_date, cvv = generate_credit_card()

# Print the generated details
print("Generated Credit Card Details:")
print("Card Number:", card_number)
print("Expiration Date:", expiration_date)
print("CVV:", cvv)
