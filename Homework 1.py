

# 1_task
from datetime import datetime
def get_days_from_today(date):
     num_date = datetime.strptime(date, "%Y-%m-%d") #Задаємо формат для дати з якою будемо порівнювати сьогоднішній день
     today = datetime.today() #Визначаємо сьогоднішню дату 
     return (today - num_date).days
# print(get_days_from_today("2026-02-03"))


# 2_task
import random

def get_numbers_ticket(min, max, quantity):  
  #Перевіряємо коректність вхідних параметрів 
    if not (
        min >= 1 and
        max <= 1000 and
        1 <= quantity <= (max - min + 1)
    ):
        return [] #

    return sorted(random.sample(range(min, max + 1), quantity)) #Повертаємо відсотртований список, якщо вик. умови 

# print(get_numbers_ticket(1, 49, 6))


# 3_task
import re

def normalize_phone(phone_number: str)-> str:
    #Прибираємо всі симовли окрім цифр
    digits = re.sub(r"\D", "", phone_number) 
    #Додаємо код 
    return (
        "+" + digits
        if re.search(r"^380", digits)
        else "+38" + digits
    )

# raw_numbers: list[str] = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


#4_task
from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    result = []

    for user in users:
        # Перетворення у дату
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Визначаємо поточний рік
        birthday_this_year = birthday.replace(year=today.year)

        # Перевіряємо чи вже минув день народження в цьому році
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        # Перевіряємо, чи входить у наступні 7 днів
        if today <= birthday_this_year <= end_date:
            congrat_date = birthday_this_year
            # Якщо вихідний — переносимо на понеділок
            if congrat_date.weekday() == 5:      
                congrat_date += timedelta(days=2)
            elif congrat_date.weekday() == 6:    
                congrat_date += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congraе_date": congrat_date.strftime("%Y.%m.%d")
            })

    return result

# users = [
#     {"name": "John Doe", "birthday": "1985.02.13"},
#     {"name": "Jane Smith", "birthday": "1990.02.08"}
# ]
# upcoming_birthdays = get_upcoming_birthdays(users)
# print("Список привітань на цьому тижні:", upcoming_birthdays)