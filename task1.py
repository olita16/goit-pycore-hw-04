def total_salary(path) :
    salaries = []
    try:
        with open(path, 'r', encoding='utf-8') as file :
            for line in file :
                _, salary = line.split(",")
                salaries.append(int(salary))
        return (sum(salaries), sum(salaries) / len(salaries))
    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдений")
        return (0, 0)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return (0, 0)

print(total_salary('salary.txt'))