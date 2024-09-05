import re
import unicodedata

class ComplexContentHandler:
    def __init__(self, config):
        self.handle_equations = config['handle_equations']
        self.handle_unfiltered_language = config['handle_unfiltered_language']

    def process_complex_content(self, content):
        if self.handle_equations:
            content = self.preserve_equations(content)
        if self.handle_unfiltered_language:
            content = self.filter_language(content)
        
        content = self.normalize_text(content)
        content = self.handle_special_content(content)
        
        return content

    def preserve_equations(self, text):
        equation_pattern = r'\b[A-Za-z]+\s*=\s*[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?'
        return re.sub(equation_pattern, lambda m: f'[EQ]{m.group()}[/EQ]', text)

    def filter_language(self, text):
        profanity_list = ['dope', 'sick']
        for word in profanity_list:
            text = re.sub(r'\b' + word + r'\b', '[FILTERED]', text, flags=re.IGNORECASE)
        return text

    def normalize_text(self, text):
        text = text.lower()
        text = ' '.join(text.split())
        return text

    def handle_special_content(self, text):
        text = re.sub(r'(https?://\S+)', r'[URL]\1[/URL]', text)
        text = re.sub(r'\S+@\S+', '[EMAIL]', text)
        return text