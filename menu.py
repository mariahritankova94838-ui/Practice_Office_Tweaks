from converter import pdf_to_docx, docx_to_pdf
from file_manager import find_files, delete_files, current_directory
from image_processor import compress_img
import os

def main_menu():
    while True:
        print("\n" + "="*40)
        print("=== Office Tweaks v1.0 ===")
        print("="*40)
        print(f"Текущий каталог: {current_directory()}")
        print("\nВыберите действие:")
        print("0. Сменить рабочий каталог")
        print("1. Преобразовать PDF в Docx")
        print("2. Преобразовать Docx в PDF")
        print("3. Произвести сжатие изображений")
        print("4. Удалить группу файлов")
        print("5. Выход")
        
        choice = input("\nВаш выбор: ").strip()
        
        if choice == '5':
            print("До свидания!")
            break
        elif choice == '0':
            change_directory()
        elif choice == '1':
            pdf_to_docx_menu()
        elif choice == '2':
            docx_to_pdf_menu()
        elif choice == '3':
            compress_images_menu()
        elif choice == '4':
            delete_files_menu()
        else:
            print("Неверный выбор!")

def change_directory():
    new_dir = input("Введите путь к новому каталогу: ").strip()
    if new_dir and os.path.exists(new_dir):
        os.chdir(new_dir)
        print(f"✓ Каталог изменен на: {current_directory()}")
    else:
        print("✗ Каталог не существует!")

def pdf_to_docx_menu():
    print("\n--- Преобразование PDF в DOCX ---")
    files = find_files('.pdf', option=0)
    if not files:
        print("PDF файлы не найдены!")
        input("Нажмите Enter, чтобы вернуться в главное меню...")
        return
    
    # Показываем файлы
    print("\nНайдено файлов:")
    for num, filename in files.items():
        print(f"{num}. {filename}")
    
    file_choice = input("\nВведите номер файла (0 - все файлы, -1 - отмена): ").strip()
    
    if file_choice == '-1':
        return
    
    print("\nОбработка файлов...")
    pdf_to_docx(file_choice, files)
    print("✓ Операция завершена!")
    input("\nНажмите Enter, чтобы вернуться в главное меню...")

def docx_to_pdf_menu():
    print("\n--- Преобразование DOCX в PDF ---")
    files = find_files('.docx', option=0)
    if not files:
        print("DOCX файлы не найдены!")
        input("Нажмите Enter, чтобы вернуться в главное меню...")
        return
    
    # Показываем файлы
    print("\nНайдено файлов:")
    for num, filename in files.items():
        print(f"{num}. {filename}")
    
    file_choice = input("\nВведите номер файла (0 - все файлы, -1 - отмена): ").strip()
    
    if file_choice == '-1':
        return
    
    print("\nОбработка файлов...")
    docx_to_pdf(file_choice, files)
    print("✓ Операция завершена!")
    input("\nНажмите Enter, чтобы вернуться в главное меню...")

def compress_images_menu():
    print("\n--- Сжатие изображений ---")
    files = find_files('.jpg', '.jpeg', '.png', '.webp', '.gif', option=0)
    if not files:
        print("Изображения не найдены!")
        input("Нажмите Enter, чтобы вернуться в главное меню...")
        return
    
    # Показываем файлы
    print("\nНайдено изображений:")
    for num, filename in files.items():
        print(f"{num}. {filename}")
    
    file_choice = input("\nВведите номер файла (0 - все файлы, -1 - отмена): ").strip()
    
    if file_choice == '-1':
        return
    
    try:
        compression = int(input("Введите качество сжатия (1-100): "))
        if 1 <= compression <= 100:
            print("\nОбработка файлов...")
            compress_img(int(file_choice), files, compression)
            print("✓ Все файлы успешно сжаты!")
        else:
            print("✗ Качество должно быть от 1 до 100!")
    except ValueError:
        print("✗ Ошибка! Введите число от 1 до 100")
    
    input("\nНажмите Enter, чтобы вернуться в главное меню...")

def delete_files_menu():
    print("\n--- Удаление файлов ---")
    print("Выберите тип удаления:")
    print("1. По началу имени")
    print("2. По окончанию имени")
    print("3. По содержанию в имени")
    print("4. По расширению")
    print("0. Назад")
    
    choice = input("\nВаш выбор: ").strip()
    
    if choice == '0':
        return
    
    substr = input("Введите строку для поиска: ").strip()
    if substr:
        # Просто вызываем delete_files - теперь она сама спросит о выборе файла
        delete_files(choice, substr)
    else:
        print("✗ Строка поиска не может быть пустой!")
    
    input("\nНажмите Enter, чтобы вернуться в главное меню...")