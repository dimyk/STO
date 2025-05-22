# car_service_tracker.py

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

def main():
    data = load_data()
    while True:
        print("\n1. Додати запис обслуговування\n2. Переглянути історію\n3. Вийти")
        choice = input("Оберіть дію: ")
        if choice == '1':
            add_service(data)
        elif choice == '2':
            show_history(data)
        elif choice == '3':
            break
        else:
            print("Невірний вибір.")
    save_data(data)

if __name__ == '__main__':
    main()
