import re
import sys
from collections import defaultdict
from typing import Callable

# Задача 1
def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


fib = caching_fibonacci()
print(fib(10))  # 55
print(fib(15))  # 610

# Задача 2
def generator_numbers(text: str):
    for match in re.finditer(r'\b\d+\.\d+\b|\b\d+\b', text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    return sum(func(text))

# Пример использования:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")  # 1351.46

# Задача 3
def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3].strip()
    }

def load_logs(file_path: str) -> list:
    logs = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            logs.append(parse_log_line(line))
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return counts

def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<20} | {'Кількість':<10}")
    print("-" * 31)
    for level, count in counts.items():
        print(f"{level:<20} | {count:<10}")

def main_log_analysis():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_log_file> [log_level]")
        sys.exit(1)

    log_file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(log_file_path)
    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level.upper())
        print(f"\nДеталі логів для рівня '{log_level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

# Задача 4
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact doesn't exist."
        except ValueError:
            return "Please enter the correct value."
        except IndexError:
            return "Insufficient arguments provided."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]

def main_bot():
    contacts = {}
    while True:
        command = input("Enter a command: ").strip().lower()
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command.startswith("add "):
            print(add_contact(command.split()[1:], contacts))
        elif command.startswith("change "):
            print(change_contact(command.split()[1:], contacts))
        elif command.startswith("phone "):
            print(show_phone(command.split()[1:], contacts))
        elif command == "all":
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main_log_analysis()
