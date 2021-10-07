import re
import sublime

SETTINGS = sublime.load_settings("caser.sublime-settings")
SNAKE_CASE_PATTERN = re.compile(r'(?<!^)(?=[A-Z])')

def camel_case(string): # this is a test
    separator = SETTINGS.get('snake_separator', '_')
    return ''.join(word.title() for word in string.split(separator))

def snake_case(string):
    separator = SETTINGS.get('snake_separator', '_')
    return SNAKE_CASE_PATTERN.sub(separator, string).lower()

def snake_to_words(string):
    word_separator = SETTINGS.get('word_separator', ' ')
    snake_separator = SETTINGS.get('snake_separator', '_')
    return word_separator.join(string.split(snake_separator))

def title(string):
    return string.title()

def upper(string):
    return string.upper()

def lower(string):
    return string.lower()
