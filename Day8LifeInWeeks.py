
def life_in_weeks(age):
    weeks_in_a_year = int(365 / 7)
    weeks_in_90 = weeks_in_a_year * 90
    weeks_in_user_age = weeks_in_a_year * age
    remaining_weeks = weeks_in_90 - weeks_in_user_age
    print(f"You have {remaining_weeks} weeks left.")

life_in_weeks(int(input("What is your age?\n>")))