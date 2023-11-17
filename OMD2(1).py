import csv
def load_data():
    data = {}
    with open('C:\\Users\\USER\\PycharmProjects\\pythonProject2\\venv\\Corp_Summary.csv', newline='', encoding='utf-8') as corp:
        reader = csv.DictReader(corp, delimiter=';')
        for row in reader:
            department = row['Департамент']
            team = row['Отдел']
            salary = int(row['Оклад'])

            if department not in data:
                data[department] = {'count': 0, 'salaries': [], 'teams': set()}
            data[department]['count'] += 1
            data[department]['salaries'].append(salary)
            data[department]['teams'].add(team)
    return data
def depart_teams():
    data = load_data()
    for department, department_data in data.items():
        teams = department_data['teams']
        teams_str = ', '.join(teams)
        print(f"{department}: {teams_str}")
def consolidated_report():
    data = load_data()
    for department, values in data.items():
        count, salaries = values['count'], values['salaries']
        min_salary, max_salary = min(salaries), max(salaries)
        avg_salary = sum(salaries) / len(salaries)

        print(
            f"Департамент {department}:\n"
            f"\tЧисленность: {count}\n"
            f"\tВилка: {min_salary} - {max_salary}\n"
            f"\tСредняя зарплата: {avg_salary:.2f}"
        )
def save_report():
    data = load_data()
    with open('data_new.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(["Департамент", "Численность", "Вилка", "Средняя зарплата"])

        for department, values in data.items():
            count, salaries = values['count'], values['salaries']
            min_salary, max_salary = min(salaries), max(salaries)
            avg_salary = sum(salaries) / len(salaries)
            writer.writerow([department, count, f"{min_salary}-{max_salary}", avg_salary])
def menu():
    options = {'1': depart_teams, '2': consolidated_report, '3': save_report}

    print("Меню:\n1: Департаменты и команды\n2: Сводный отчёт\n3: Сохранить отчёт")
    option = input('Выберите опцию: ')

    while option not in options:
        print("Выберите правильную опцию (1, 2 или 3): ")
        option = input()
    options[option]()

if __name__ == '__main__':
    menu()
