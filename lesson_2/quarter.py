# Квартал

def quarter_of_year(month):
    if 1 <= month <= 3:
        return "I квартал"
    if 4 <= month <= 6:
        return "II квартал"
    if 7 <= month <= 9:
        return "III квартал"
    if 10 <= month <= 12:
        return "IV квартал"
    return "Неверный номер месяца"


month = int(input("Введите номер месяца (1-12): "))
print(quarter_of_year(month))
