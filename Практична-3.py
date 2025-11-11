def main():
    students = {}

    print("Введіть ім'я студента та оцінку (від 1 до 12). Введіть 'stop' для завершення.")

    while True:
        name = input("Ім'я студента (або 'stop'): ").strip()
        if name.lower() == 'stop':
            break

        try:
            grade = int(input("Оцінка (1-12): "))
            if 1 <= grade <= 12:
                students[name] = grade
            else:
                print("Оцінка повинна бути від 1 до 12.")
        except ValueError:
            print("Будь ласка, введіть числове значення оцінки.")

    if not students:
        print("Дані не були введені.")
        return

    print("\nСписок студентів та їх оцінки:")
    for name, grade in students.items():
        print(f"{name}: {grade}")

    # Обчислення статистики
    grades = list(students.values())
    average = sum(grades) / len(grades)

    excellent = {name: g for name, g in students.items() if 10 <= g <= 12}
    good = {name: g for name, g in students.items() if 7 <= g <= 9}
    poor = {name: g for name, g in students.items() if 4 <= g <= 6}
    failed = {name: g for name, g in students.items() if 1 <= g <= 3}

    print(f"\nСередній бал по групі: {average:.2f}")
    print(f"Відмінники (10-12): {len(excellent)} - {', '.join(excellent.keys())}")
    print(f"Хорошисти (7-9): {len(good)}")
    print(f" Відстаючі (4-6): {len(poor)}")
    print(f"Не здали (1-3): {len(failed)}")

if __name__ == "__main__":
    main()
