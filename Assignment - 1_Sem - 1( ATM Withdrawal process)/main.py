def atm_simulation():
    # A simple database (dictionary) to store account information.
    # Key: Card Number (string), Value: Another dictionary containing 'pin' and 'balance'.
    database = {
        "1234": {"pin": "4321", "balance": 1500.00},
        "5678": {"pin": "8765", "balance": 50.00}
    }
    
    print("--- Welcome to the ATM ---")
    # Prompt the user to "insert" their card by entering the card number.
    card = input("Please insert your Card (Enter Card Number, e.g., 1234): ")
    # Prompt the user to enter their PIN.
    pin = input("Enter your PIN: ")
    
    # Check for valid login:
    # 1. Check if the card number exists in the database.
    # 2. Check if the entered PIN matches the PIN associated with that card.
    if card in database and database[card]["pin"] == pin:
        # If login is successful, store the account data for easy access.
        account = database[card]
        print("\nLogin Successful. Welcome!")
        
        # Start the main transaction loop.
        while True:
            print("\n--- Main Menu ---")
            print("1. Cash Withdrawal")
            print("2. Check Balance")
            print("3. Cash Deposit")
            # Get the user's menu choice.
            choice = input("Enter your choice (1, 2, or 3): ")
            
            # --- Cash Withdrawal Logic ---
            if choice == '1':
                try:
                    # Prompt for the withdrawal amount and convert it to a float.
                    amount = float(input("Enter amount to withdraw: $"))
                    # Validate that the amount is positive.
                    if amount <= 0:
                        print("Withdrawal amount must be greater than zero.")
                    # Check for sufficient funds.
                    elif amount > account["balance"]:
                        print("Insufficient Funds. Your current balance is: $" + str(account["balance"]))
                    # Perform the withdrawal.
                    else:
                        account["balance"] -= amount  # Deduct amount from balance
                        print(f"Dispensing: ${amount}")
                        print("Transaction complete.")
                # Handle cases where the user enters non-numeric input for the amount.
                except ValueError:
                    print("Invalid input. Please enter a numerical amount.")
            
            # --- Check Balance Logic ---
            elif choice == '2':
                # Display the current account balance.
                print(f"Your current balance is: ${account['balance']}")
            
            # --- Cash Deposit Logic ---
            elif choice == '3':
                try:
                    # Prompt for the deposit amount and convert it to a float.
                    amount = float(input("Insert cash (Enter amount to deposit): $"))
                    # Validate that the amount is positive.
                    if amount <= 0:
                        print("Deposit amount must be greater than zero.")
                    # Perform the deposit.
                    else:
                        account["balance"] += amount  # Add amount to balance
                        print(f"Deposit Successful. New Balance is: ${account['balance']}")
                # Handle cases where the user enters non-numeric input for the amount.
                except ValueError:
                    print("Invalid input. Please enter a numerical amount.")
            
            # --- Invalid Choice Logic ---
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
            
            # Check if the user wants another transaction.
            continue_choice = input("\nWould you like another transaction? (Y/N): ").upper()
            # Exit the loop (and the program) if the choice is not 'Y'.
            if continue_choice != 'Y':
                print("\nThank you for banking with us. Please take your card.")
                break
                
    # This block executes if the initial card or PIN check failed.
    else:
        print("\nError: Invalid Card or PIN. Please try again.")

# Standard Python entry point: calls the main function when the script is run directly.
if __name__ == "__main__":
    atm_simulation()