from collections import Counter
import sys

def parse_log_line(line: str) -> dict: # приймає рядок з логу як вхідний параметр і повертає словник з розібраними компонентами: дата, час, рівень, повідомлення.
    line = line.split(" ")    
    message = " ".join(line[3:])
    modified_message = message.replace("\n", '')
    outdict = {"data": line[0], "time": line[1], "level": line[2], "message": modified_message }
    return outdict

def load_logs(file_path: str) -> list: #відкриває файл, читає кожен рядок і застосовує для нього функцію parse_log_line
    outlist = []
    try:
        with open(file_path, "r", encoding = "UTF-8") as log_line:        
            for line in log_line:
                parse_line = parse_log_line(line)
                outlist.append(parse_line)
        return outlist
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
        sys.exit(1) 

def filter_logs_by_level(logs: list, level: str) -> list: # Фільтрує за рівнем логування
    print(f"Деталі логів для рівня '{level}'")  
    filter_logs = [f"{log['data']} {log['time']} - {log['message']}" for log in logs if log.get("level") == level]       
    for  element in filter_logs:
        print(element)
           
def count_logs_by_level(logs: list) -> dict: # проходить по всім записам і підраховує кількість записів для кожного рівня логування
    count_dict_key = "level"
    count_dict = dict(Counter(item[count_dict_key] for item in logs))
    return count_dict


def display_log_counts(counts_dict: dict): # форматує та виводить результати підрахунку в читабельній формі.
    print(f"{"Рівень логування".ljust(17)}| {"Кількість".rjust(9)}\n{"-"*30}") 
    for level, count in counts_dict.items():
        print(f"{level.ljust(17)}| {str(count).rjust(1)}")


if __name__ == "__main__":   
    if len(sys.argv) < 2:
        print("Використання: python script.py <лог-файл>")
        sys.exit(1)

    log_file_path = sys.argv[1]
    log_lines = load_logs(log_file_path)
    log_statistics = count_logs_by_level(log_lines)
    display_log_counts(log_statistics)

    if len(sys.argv) == 3:
        target_log_level = sys.argv[2]
        display_log_counts(log_statistics)
        log_lines = load_logs(log_file_path)                
        filter_logs_by_level(log_lines, target_log_level)