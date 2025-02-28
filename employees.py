company_employees = {
    "Engineering": {
        "Alice": {"age": 30, "role": "Software Engineer"},
        "Bob": {"age": 28, "role": "DevOps Engineer"}
    },
    "HR": {
        "Charlie": {"age": 35, "role": "HR Manager"}
    }
}


print("Company Employees:", company_employees)

def add_employee(department, name, age, role):
    if department not in company_employees:
        company_employees[department] = {}
    company_employees[department][name] = {"age": age, "role": role}

add_employee("Engineering", "David", 27, "Data Scientist")
print("Updated Company Employees:", company_employees)

def count_employees(company):
    return sum(len(dept) for dept in company.values())

print("Total Employees:", count_employees(company_employees))