def month_to_season(month):
    seasons = {
        1: "Зима", 2: "Зима", 12: "Зима",
        3: "Весна", 4: "Весна", 5: "Весна",
        6: "Лето", 7: "Лето", 8: "Лето",
        9: "Осень", 10: "Осень", 11: "Осень",
    }
    return seasons[month]


month = 2
result = month_to_season(month)
print(f"Месяц {month}: {result}")
