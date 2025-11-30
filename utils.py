

import os
from datetime import datetime

def log_operation(operation, details):
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f"[{timestamp}] {operation}: {details}"
    
   
    print(log_message)
    

    with open('office_tweaks.log', 'a', encoding='utf-8') as f:
        f.write(log_message + '\n')

def validate_file_extension(filename, allowed_extensions):
    return filename.lower().endswith(tuple(allowed_extensions))

def get_file_size(file_path):
    try:
        size = os.path.getsize(file_path)
        if size < 1024:
            return f"{size} B"
        elif size < 1024*1024:
            return f"{size/1024:.1f} KB"
        else:
            return f"{size/(1024*1024):.1f} MB"
    except:
        return "Unknown"