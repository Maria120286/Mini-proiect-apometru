from collections import defaultdict

data = defaultdict(dict)

months = ['ian', 'feb', 'mar', 'apr', 'mai', 'iun', 'iul', 'aug', 'sep', 'oct', 'nov', 'dec']

def add_reading():
    year = input("Introduceți anul: ")
    month = input("Introduceți luna: ").lower()

    if month not in months:
        print("Luna nu este corectă!")
        return

    if month in data[year]:
        print("Citire pentru luna specificată există deja!")
        return

    cold_water = int(input("Introduceți valoarea contorului de apă rece: "))
    hot_water = int(input("Introduceți valoarea contorului de apă caldă: "))

    if months.index(month) > 0:
        prev_month = months[months.index(month) - 1]
        if year in data and prev_month in data[year]:
            if cold_water < data[year][prev_month]['cold_water'] or hot_water < data[year][prev_month]['hot_water']:
                print("Valoarea contoarelor este invalidă!")
                return

    data[year][month] = {'cold_water': cold_water, 'hot_water': hot_water}
    print("Citire adăugată cu succes!")

def delete_reading():
    year = input("Introduceți anul: ")
    month = input("Introduceți luna: ").lower()

    if month not in months or year not in data or month not in data[year]:
        print("Nu există o citire pentru anul și luna introduse!")
        return

    del data[year][month]
    print("Citire ștearsă cu succes!")

def show_consumption():
    year = input("Introduceți anul: ")
    month = input("Introduceți luna: ").lower()

    if month not in months or year not in data or month not in data[year]:
        print("Nu există o citire pentru anul și luna introduse!")
        return

    if months.index(month) > 0:
        prev_month = months[months.index(month) - 1]
        if year in data and prev_month in data[year]:
            cold_water_consumption = data[year][month]['cold_water'] - data[year][prev_month]['cold_water']
            hot_water_consumption = data[year][month]['hot_water'] - data[year][prev_month]['hot_water']
            print(f"{month} {year} consum")
            print(f"Apă rece: {data[year][prev_month]['cold_water']} {cold_water_consumption}")
            print(f"Apă caldă: {data[year][prev_month]['hot_water']} {hot_water_consumption}")
        else:
            print("Nu există citire pentru luna precedentă!")
    else:
        print("Nu există citire pentru luna precedentă!")

def exit_app():
    print("Ieșire din aplicație.")
    exit(0)

actions = {
    '1': add_reading,
    '2': delete_reading,
    '3': show_consumption,
    '4': exit_app
}

while True:
    print("1. Adăugare citire")
    print("2. Ștergere citire")
    print("3. Afișare consum")
    print("4. Ieșire")

    action = input("Alegeți opțiunea: ")
    actions.get(action, lambda: print("Opțiune invalidă!"))()
