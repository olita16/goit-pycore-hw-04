def get_cats_info(path):
    cats_info = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = [
                {'id': cat_data[0], 'name': cat_data[1], 'age': cat_data[2]}
                for line in file if (cat_data := line.strip().split(',')) and len(cat_data) == 3
            ]
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдений.")
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
    
    return cats_info


cats_info = get_cats_info("cats.txt")
print(cats_info)