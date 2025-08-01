
def calculate_total_salary(basic):
    hra = 0.20 * basic
    da = 0.10 * basic
    total_salary = basic + hra + da
    return total_salary


for i in range(1, 6):
    basic = float(input(f"Enter the basic pay for employee {i}: "))
    total = calculate_total_salary(basic)
    print(f"Total monthly salary for employee {i}: ₹{total:.3f}")
