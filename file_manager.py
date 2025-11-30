import os
from utils import get_file_size

def find_files(*args, option: int = 0):
    searching_for = tuple([*args])
    file_list = os.listdir(os.getcwd())
    file_nums = {}
    
    if option == 0:
        if args:
            print(f'Поиск файлов с расширением {", ".join([*args])} в данном каталоге')
        else:
            print('Поиск всех файлов в каталоге')
    
    match option:
        case 0:
            for filename in file_list:
                if os.path.isfile(filename) and (not searching_for or filename.endswith(searching_for)):
                    file_nums[len(file_nums) + 1] = filename
                    size = get_file_size(filename)
                    print(f'{len(file_nums)}: {filename} ({size})')
        case 1:
            for filename in file_list:
                if os.path.isfile(filename) and filename.startswith(searching_for):
                    file_nums[len(file_nums) + 1] = filename
                    size = get_file_size(filename)
                    print(f'{len(file_nums)}: {filename} ({size})')
        case 2:
            for filename in file_list:
                if os.path.isfile(filename):
                    try:
                        end = filename.rindex('.')
                        if filename[:end].endswith(searching_for):
                            file_nums[len(file_nums) + 1] = filename
                            size = get_file_size(filename)
                            print(f'{len(file_nums)}: {filename} ({size})')
                    except ValueError:
                        continue
        case 3:
            for filename in file_list:
                if os.path.isfile(filename):
                    try:
                        end = filename.rindex('.')
                        name_without_ext = filename[:end]
                        for wanted in searching_for:
                            if wanted in name_without_ext:
                                file_nums[len(file_nums) + 1] = filename
                                size = get_file_size(filename)
                                print(f'{len(file_nums)}: {filename} ({size})')
                                break
                    except ValueError:
                        if any(wanted in filename for wanted in searching_for):
                            file_nums[len(file_nums) + 1] = filename
                            size = get_file_size(filename)
                            print(f'{len(file_nums)}: {filename} ({size})')
    
    if not file_nums:
        print('Файлы не найдены.')
    
    return file_nums

def delete_files(option, substr):
    files_to_delete = find_files(substr, option=int(option))
    deleted_count = 0
    
    if not files_to_delete:
        print("Файлы для удаления не найдены!")
        return deleted_count
    
    # Показываем файлы которые можно удалить
    print(f"\nНайдено файлов:")
    for num, filename in files_to_delete.items():
        print(f"{num}. {filename}")
    
    # Спрашиваем какие файлы удалять
    choice = input(f"\nВведите номер файла (0 - удалить все, -1 - отмена): ").strip()
    
    if choice == '-1':
        print("❌ Удаление отменено")
        return deleted_count
    
    if choice == '0':
        # Удалить все файлы
        confirm = input(f"Удалить ВСЕ {len(files_to_delete)} файлов? (y/N): ").lower()
        if confirm == 'y':
            for file_path in files_to_delete.values():
                try:
                    os.remove(file_path)
                    print(f'✓ Файл {file_path} удален успешно')
                    deleted_count += 1
                except PermissionError:
                    print('✗ Недостаточно прав для удаления!')
                except Exception as e:
                    print(f'✗ Ошибка удаления: {e}')
    elif choice.isdigit() and int(choice) in files_to_delete:
        # Удалить один конкретный файл
        file_path = files_to_delete[int(choice)]
        confirm = input(f"Удалить файл {file_path}? (y/N): ").lower()
        if confirm == 'y':
            try:
                os.remove(file_path)
                print(f'✓ Файл {file_path} удален успешно')
                deleted_count += 1
            except PermissionError:
                print('✗ Недостаточно прав для удаления!')
            except Exception as e:
                print(f'✗ Ошибка удаления: {e}')
    else:
        print("✗ Неверный выбор!")
    
    print(f"\nУдалено файлов: {deleted_count}")
    return deleted_count

def current_directory():
    return os.getcwd()

