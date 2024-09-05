import os

class InputHandler:
    def __init__(self, config):
        self.file_types = config['file_types']
        self.input_directory = config['input_directory']

    def get_input_files(self):
        if not os.path.exists(self.input_directory):
            print(f"Input directory does not exist: {self.input_directory}")
            return []

        return [
            f for f in os.listdir(self.input_directory) 
            if os.path.isfile(os.path.join(self.input_directory, f)) and 
            f.split('.')[-1].lower() in self.file_types
        ]