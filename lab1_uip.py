import json
import os
from datetime import datetime

DATA_FILE = 'service_data.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_service(data):
    vin = input("Введіть VIN автомобіля: ").strip()
    if vin not in data:
        data[vin] = []
    service = input("Тип обслуговування (наприклад, Заміна масла): ")
    date = input("Дата (YYYY-MM-DD): ")
    mileage = input("Пробіг (км): ")
    data[vin].append({
        "service": service,
        "date": date,
        "mileage": mileage
    })
    print("Запис додано!")

def show_history(data):
    vin = input("Введіть VIN: ").strip()
    if vin in data:
        for entry in data[vin]:
            print(f"- {entry['date']} | {entry['service']} @ {entry['mileage']} км")
    else:
        print("Історії не знайдено.")

#Додаткова функція
def show_last_service(data):
    if not data:
        print("Немає записів.")
        return
    for vin, records in data.items():
        if records:
            last = sorted(records, key=lambda r: r['date'], reverse=True)[0]
            print(f"{vin}: {last['date']} | {last['service']} @ {last['mileage']} км")
        else:
            print(f"{vin}: немає обслуговувань")


def main():
    data = load_data()
    while True:
        print("\n1. Додати запис обслуговування\n2. Переглянути історію\n3. Вивести останнє обслуговування\n4. Вийти")
        choice = input("Оберіть дію: ")
        if choice == '1':
            add_service(data)
        elif choice == '2':
            show_history(data)
        elif choice == '3':
            show_last_service(data)
        elif choice == '4':
            break
        else:
            print("Невірний вибір.")
    save_data(data)

if __name__ == '__main__':
    main()
