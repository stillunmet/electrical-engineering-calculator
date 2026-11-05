
# Electrical Engineering Calculator
# My first Python project

print("================================")
print(" ELECTRICAL ENGINEERING CALCULATOR")
print("================================")

voltage = float(input("Enter voltage (V): "))
resistance = float(input("Enter resistance (Ohms): "))

current = voltage / resistance

power = voltage * current

print("\n----- RESULTS -----")
print("Voltage:", voltage, "V")
print("Resistance:", resistance, "Ohms")
print("Current:", current, "A")
print("Power:", power, "W")
