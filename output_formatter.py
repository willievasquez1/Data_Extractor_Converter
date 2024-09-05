import os
import json
import csv

class OutputFormatter:
    def __init__(self, config):
        self.formats = config['formats']

    def format_output(self, data, input_file_path):
        input_dir = os.path.dirname(input_file_path)
        base_filename = os.path.splitext(os.path.basename(input_file_path))[0]
        
        output_dir = os.path.join(input_dir, f"{base_filename}_output")
        os.makedirs(output_dir, exist_ok=True)
        
        for format in self.formats:
            if format == 'txt':
                self.save_as_txt(data, output_dir, base_filename)
            elif format == 'csv':
                self.save_as_csv(data, output_dir, base_filename)
            elif format == 'json':
                self.save_as_json(data, output_dir, base_filename)

    def save_as_txt(self, data, output_dir, base_filename):
        output_path = os.path.join(output_dir, f"{base_filename}.txt")
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(data)

    def save_as_csv(self, data, output_dir, base_filename):
        output_path = os.path.join(output_dir, f"{base_filename}.csv")
        with open(output_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['content'])
            writer.writerow([data])

    def save_as_json(self, data, output_dir, base_filename):
        output_path = os.path.join(output_dir, f"{base_filename}.json")
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump({"content": data}, file, ensure_ascii=False, indent=4)