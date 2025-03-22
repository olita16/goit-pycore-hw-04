from pathlib import Path
import colorama
import sys
import os
colorama.init()

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    print(colorama.Fore.RED + "Помилка: Не вказано шлях до директорії")
    sys.exit(1)

def print_path(path, depth=0):
    try:
        path_obj = Path(path)
        if path_obj.is_dir():
            print(colorama.Fore.BLUE + f"{' ' * depth}{path_obj.name}/")
            for item in path_obj.iterdir():
                    print_path(item, depth + 1)
        else:
            print(colorama.Fore.GREEN + f"{' ' * depth}{path_obj.name}")
    except Exception as e:
        print(colorama.Fore.RED +f"Помилка: {e}")

if not os.path.exists(path):
    print(colorama.Fore.RED + f"Помилка: Шлях '{path}' не існує")
    sys.exit(1)

print_path(path)

print(f"Поточна директорія: {os.getcwd()}")
