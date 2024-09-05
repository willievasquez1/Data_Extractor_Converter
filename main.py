import os
import sys
import yaml
import logging
from data_extractor import DataExtractor
from output_formatter import OutputFormatter
from complex_content_handler import ComplexContentHandler

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'config.yaml')
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def main(input_file):
    config = load_config()
    
    data_extractor = DataExtractor(config['extraction'])
    output_formatter = OutputFormatter(config['output'])
    complex_handler = ComplexContentHandler(config['complex_content'])
    
    try:
        logging.info(f"Processing file: {input_file}")
        extracted_data = data_extractor.extract_data(input_file)
        processed_data = complex_handler.process_complex_content(extracted_data)
        output_formatter.format_output(processed_data, input_file)
        logging.info(f"Successfully processed: {input_file}")
        output_dir = os.path.join(os.path.dirname(input_file), f"{os.path.splitext(os.path.basename(input_file))[0]}_output")
        logging.info(f"Output saved in: {output_dir}")
    except Exception as e:
        logging.error(f"Error processing {input_file}: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file_path>")
        sys.exit(1)
    main(sys.argv[1])