
# Electrical Engineering Calculator
# Version 2.0

print("=" * 40)
print(" ELECTRICAL ENGINEERING CALCULATOR")
print("=" * 40)

try:
    voltage = float(input("Enter voltage (V): "))
    resistance = float(input("Enter resistance (Ohms): "))

    if resistance <= 0:
        print("Error: Resistance must be greater than zero.")

    else:
        current = voltage / resistance
        power = voltage * current

        print("\n----- RESULTS -----")
        print(f"Voltage: {voltage:.2f} V")
        print(f"Resistance: {resistance:.2f} Ohms")
        print(f"Current: {current:.2f} A")
        print(f"Power: {power:.2f} W")

except ValueError:
    print("Error: Please enter valid numbers.")


