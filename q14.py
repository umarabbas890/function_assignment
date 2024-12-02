# Advanced Function Questions
# Create a function that converts a given temperature from Celsius to Fahrenheit and vice versa.
def convert_temperature(value, scale):
   
    if scale.upper() == 'C':  # Convert to Celsius
        return (value - 32) * 5 / 9
    elif scale.upper() == 'F':  # Convert to Fahrenheit
        return (value * 9 / 5) + 32
    else:
        raise ValueError("Scale must be 'C' for Celsius or 'F' for Fahrenheit.")

# Example usage
temperature = float(input("Enter the temperature: "))
target_scale = input("Convert to (C/F): ").strip()
converted = convert_temperature(temperature, target_scale)
print(f"The converted temperature is: {converted:.2f}°{target_scale.upper()}")
