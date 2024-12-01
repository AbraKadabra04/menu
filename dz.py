import os

def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return sum(1 for line in f)

def combine_files(input_files, output_file):
    files_with_line_counts = {}

    for filename in input_files:
        if os.path.isfile(filename):
            line_count = count_lines(filename)
            files_with_line_counts[filename] = line_count
        else:
            print(f"Файл {filename} не найден.")

    sorted_files = sorted(files_with_line_counts.items(), key=lambda x: x[1])

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for filename, line_count in sorted_files:
            out_file.write(f"Имя файла: {filename}\n")
            out_file.write(f"Количество строк: {line_count}\n")

            with open(filename, 'r', encoding='utf-8') as in_file:
                out_file.writelines(in_file.readlines())
            
            out_file.write("\n")

input_files = ['/Users/aleksandr/Desktop/menu/dz/new.txt', '/Users/aleksandr/Desktop/menu/dz/new_2.txt', 'dz/new_3.txt']
output_file = 'result.txt'

combine_files(input_files, output_file)