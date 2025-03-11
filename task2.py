импорт csv
импорт json
имя_файла_ввода = "input.csv"
output_filename = "output.json"
разделитель = ","
строка_завершения = "\n"
открыть с помощью (имя_файла_ввода, 'r', кодировка='utf-8') в качестве файла:
    csv = csv_reader.DictReader(файл, разделитель=разделитель)
    = данные [строка для строки в csv_reader]
открыть с помощью (output_filename, 'w', кодировка='utf-8') как json_файл:
    json.dump(данные, json_файл, отступ=4, ensure_ascii=False)
открыть с помощью (output_filename, 'r', кодировка='utf-8') в качестве файла:
    json = данные.загрузить(файл)
    вывести(json.dumps(данные, отступ=4, ensure_ascii=False), конец="")