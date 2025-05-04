# 9. Bank Transaction Analyzer (Representation & Clarity)
# Write a Python program that allows users to input a series of transactions (credits and debits). Your
# program should:
# • Record each transaction clearly.
# • Calculate and print the balance after each transaction.
# • Provide a final summary at the end.

def bank_transaction_analyzer():
    transactions = []
    balance = 0

    print("Enter your transactions (e.g., 'credit 1000', 'debit 500'). Type 'done' to finish.\n")

    while True:
        entry = input("Transaction: ").strip().lower()
        if entry == 'done':
            break

        try:
            t_type, amount_str = entry.split()
            amount = float(amount_str)

            if t_type == 'credit':
                balance += amount
                transactions.append((t_type, amount, balance))
            elif t_type == 'debit':
                balance -= amount
                transactions.append((t_type, amount, balance))
            else:
                print("Invalid transaction type. Use 'credit' or 'debit'.")
        except:
            print("Invalid format. Please enter like: 'credit 1000' or 'debit 500'.")

    # Print transaction history
    print("\nTransaction History:")
    print(f"{'Type':<10}{'Amount':<10}{'Balance'}")
    print("-" * 30)
    for t_type, amount, bal in transactions:
        print(f"{t_type:<10}{amount:<10.2f}{bal:.2f}")

    # Final summary
    print("\nFinal Balance:", balance)

# Run the analyzer
bank_transaction_analyzer()
