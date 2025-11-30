from PIL import Image
import os

def compress_img(option, images, compression):
    """Сжимает изображения с заданным качеством"""
    if compression not in range(1, 101):
        print('✗ Ошибка: качество сжатия должно быть от 1 до 100!')
        return 0
    
    compressed_count = 0
    option = int(option)  # Преобразуем в число
    
    # Определяем какие файлы обрабатывать
    if option == 0:
        # Все файлы из словаря
        files_to_process = list(images.values())
        print(f"Обработка всех файлов ({len(files_to_process)} изображений)...")
    else:
        # Конкретный файл по номеру
        if type(images) is dict:
            specific_file = images.get(option)
            if specific_file:
                files_to_process = [specific_file]
                print(f"Обработка выбранного файла: {specific_file}")
            else:
                files_to_process = []
                print("✗ Файл с таким номером не найден!")
        else:
            files_to_process = []
    
    # Обрабатываем файлы
    for file_path in files_to_process:
        if file_path and os.path.exists(file_path):
            try:
                # Открываем изображение
                image_file = Image.open(file_path)
                
                # Создаем имя для сжатого файла
                output_file = 'compressed-' + file_path
                
                # Сохраняем с сжатием
                image_file.save(output_file, quality=compression, optimize=True)
                
                # Получаем размеры файлов для сравнения
                original_size = os.path.getsize(file_path)
                compressed_size = os.path.getsize(output_file)
                saved_percent = ((original_size - compressed_size) / original_size) * 100
                
                print(f'✓ {file_path} сжато -> {output_file}')
                print(f'  Размер: {original_size/1024:.1f}KB → {compressed_size/1024:.1f}KB (экономия {saved_percent:.1f}%)')
                compressed_count += 1
                
            except Exception as e:
                print(f'✗ Ошибка сжатия {file_path}: {e}')
        else:
            print(f'✗ Файл не найден: {file_path}')
    
    if compressed_count == 0:
        print("Ни одно изображение не было сжато")
    else:
        print(f"Успешно сжато изображений: {compressed_count}")
    
    return compressed_count