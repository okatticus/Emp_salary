def calculate_salary(country: str, gross: float):
    if country.lower() == "india":
        deduction = gross * 0.10
    elif country.lower() in ("united states", "usa"):
        deduction = gross * 0.12
    else:
        deduction = 0

    return {
        "gross": gross,
        "deductions": deduction,
        "net": gross - deduction,
    }
