from docx2pdf import convert
from pdf2docx import Converter
from file_manager import find_files  # ← УБРАТЬ select_single_file

def pdf_to_docx_single(pdf_file):
    """Конвертирует один PDF файл в DOCX"""
    try:
        docx_file = pdf_file[:-4] + '.docx'
        pdf_conv = Converter(pdf_file)
        pdf_conv.convert(docx_file)
        pdf_conv.close()
        print(f'✓ Файл {pdf_file} успешно конвертирован в {docx_file}')
        return True
    except Exception as e:
        print(f'✗ Ошибка конвертации {pdf_file}: {e}')
        return False

def docx_to_pdf_single(docx_file):
    """Конвертирует один DOCX файл в PDF"""
    try:
        pdf_file = docx_file[:-5] + '.pdf'
        convert(docx_file, pdf_file)
        print(f'✓ Файл {docx_file} успешно конвертирован в {pdf_file}')
        return True
    except Exception as e:
        print(f'✗ Ошибка конвертации {docx_file}: {e}')
        return False

def pdf_to_docx(choice, docs):
    """Конвертирует PDF файлы в формат DOCX с выбором"""
    if int(choice) == 0:
        # Все файлы
        for file_path in list(docs.values()):
            pdf_to_docx_single(file_path)
    else:
        # Конкретный файл
        if type(docs) is dict:
            pdf_file = docs.get(int(choice))
            if pdf_file:
                pdf_to_docx_single(pdf_file)

def docx_to_pdf(choice, docs):
    """Конвертирует DOCX файлы в формат PDF с выбором"""
    if int(choice) == 0:
        # Все файлы
        for file_path in list(docs.values()):
            docx_to_pdf_single(file_path)
    else:
        # Конкретный файл
        if type(docs) is dict:
            docx_file = docs.get(int(choice))
            if docx_file:
                docx_to_pdf_single(docx_file)