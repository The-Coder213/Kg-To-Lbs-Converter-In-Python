print("This is a kg to lbs converter and vice versa")

def Convert():
    while True:
        # Get user inputs
        startingWeight = int(input("Enter the weight here: "))  # No error handling here
        startingUnit = input("Enter the unit here (kg, lbs): ").lower()
        
        # Perform conversion
        if startingUnit == "kg":
            finalWeight = startingWeight * 2.205
            print(f"{startingWeight} kg = {finalWeight} lbs")
        elif startingUnit == "lbs":
            finalWeight = startingWeight / 2.205
            print(f"{startingWeight} lbs = {finalWeight} kg")
        else:
            print("Invalid input! Please enter 'kg' or 'lbs'.")

        # Ask if the user wants to continue
      

Convert()
