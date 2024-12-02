# Real-world Scenarios
# Write a function that takes a list of employee salaries and calculates the average salary.
def calculate_average_salary(salaries):
    if not salaries:  # Check if the list is empty
        return 0  
    return sum(salaries) / len(salaries)  # Calculate the average

# Example usage
employee_salaries = [3500, 4500, 4000, 5000, 3000]
average_salary = calculate_average_salary(employee_salaries)
print(f"The average salary is: {average_salary}")

