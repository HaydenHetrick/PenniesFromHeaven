def calculate_pennies(pennies):
    dollars = pennies // 100
    pennies %= 100

    quarters = pennies // 25
    pennies %= 25

    dimes = pennies // 10
    pennies %= 10

    nickels = pennies // 5
    pennies %= 5

    return dollars, quarters, dimes, nickels, pennies

def main():
    try:
        pennies = int(input("Enter the amount in pennies: "))
        dollars, quarters, dimes, nickels, remaining_pennies = calculate_pennies(pennies)

        print(f"Dollars: {dollars}")
        print(f"Quarters: {quarters}")
        print(f"Dimes: {dimes}")
        print(f"Nickels: {nickels}")
        print(f"Pennies: {remaining_pennies}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
