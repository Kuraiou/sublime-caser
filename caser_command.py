import re
import sublime
import sublime_plugin
import types

s = sublime.load_settings("caser.sublime-settings")

snake_case_pattern = re.compile(r'(?<!^)(?=[A-Z])')

def camel_case(string): # this will be rebound to the base string
    return ''.join(word.title() for word in string.split('_'))

def snake_case(string): # this will be rebound to the base string
    return snake_case_pattern.sub('_', string).lower()

class CaserCommand(sublime_plugin.TextCommand):
    def modify_regions(self, edit, modifier, alt_method = None):
        sublime.status_message("running")
        regions = self.view.sel()

        selections = []
        for region in regions:
            selected_entire_file = False
            if region.empty():
                if len(regions) > 1:
                    continue
                elif s.get("use_entire_file_if_no_selection", True):
                    selection = sublime.Region(0, self.view.size())
                    selected_entire_file = True
                else:
                    selection = region
            else:
                selection = region

            base_str = self.view.substr(selection)

            if alt_method is not None:
                modified_str = alt_method(base_str)
            else:
                modified_str = getattr(base_str, modifier)()

            self.view.replace(edit, selection, modified_str)

class CaserDowncaseCommand(CaserCommand):
    def run(self, edit):
        self.modify_regions(edit, 'lower')

class CaserUpcaseCommand(CaserCommand):
    def run(self, edit):
        self.modify_regions(edit, 'upper')

class CaserTitleizeCommand(CaserCommand):
    def run(self, edit):
        self.modify_regions(edit, 'title')

class CaserSnakeCaseCommand(CaserCommand):
    def run(self, edit):
        self.modify_regions(edit, 'snake_case', snake_case)

class CaserCamelCaseCommand(CaserCommand):
    def run(self, edit):
        self.modify_regions(edit, 'snake_case', camel_case)

