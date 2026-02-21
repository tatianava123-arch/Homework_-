import random
import re
from datetime import datetime, date, timedelta
from typing import List, Dict, Any


# --- Task 1 ---

def get_days_from_today(date_string: str) -> int:
    """
    Розраховує кількість днів між поточною датою та заданою датою.
    
    :param date_string: Дата у форматі 'РРРР-ММ-ДД'.
    :return: Кількість днів (позитивна, якщо дата в минулому).
    """
    num_date = datetime.strptime(date_string, "%Y-%m-%d")
    today = datetime.today()
    return (today - num_date).days


# --- Task 2 ---

def get_numbers_ticket(min_val: int, max_val: int, quantity: int) -> List[int]:
    """
    Генерує набір унікальних випадкових чисел для лотерейного квитка.
    """
    if not (1 <= min_val <= max_val <= 1000 and 1 <= quantity <= (max_val - min_val + 1)):
        return []

    return sorted(random.sample(range(min_val, max_val + 1), quantity))


# --- Task 3 ---

def normalize_phone(phone_number: str) -> str:
    """
    Нормалізує номер телефону до стандартного формату +380XXXXXXXXX.
    """
    digits = re.sub(r"\D", "", phone_number)
    
    if digits.startswith("380"):
        return "+" + digits
    else:
        # Випадок, якщо номер без коду країни (наприклад, починається з 0)
        # або містить лише частину коду.
        if not digits.startswith("38"):
             digits = "38" + digits if digits.startswith("0") else "380" + digits
        return "+" + digits


# --- Task 4 ---

def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Визначає список користувачів, яких потрібно привітати з днем народження 
    протягом наступних 7 днів.
    """
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    result = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if today <= birthday_this_year <= end_date:
            congrat_date = birthday_this_year
            
            # Якщо вихідний (5 - Субота, 6 - Неділя) — переносимо на понеділок
            if congrat_date.weekday() == 5:      
                congrat_date += timedelta(days=2)
            elif congrat_date.weekday() == 6:    
                congrat_date += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": congrat_date.strftime("%Y.%m.%d")
            })

    return result


# --- Main Entry Point ---

if __name__ == "__main__":
    print("--- Task 1: Days from today ---")
    print(f"Днів минуло: {get_days_from_today('2024-01-01')}\n")

    print("--- Task 2: Lottery Ticket ---")
    print(f"Ваші числа: {get_numbers_ticket(1, 49, 6)}\n")

    print("--- Task 3: Phone Normalization ---")
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678",
        "+380 44 123 4567",
        "380501234567",
    ]
    sanitized = [normalize_phone(num) for num in raw_numbers]
    print(f"Нормалізовані: {sanitized}\n")

    print("--- Task 4: Upcoming Birthdays ---")
    test_users = [
        {"name": "John Doe", "birthday": "1985.02.23"},
        {"name": "Jane Smith", "birthday": "1990.02.25"}
    ]
    print(f"Привітання: {get_upcoming_birthdays(test_users)}")