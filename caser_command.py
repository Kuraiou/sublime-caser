import re
import sublime
import sublime_plugin
import types
from . import modifiers

class CaserCommand(sublime_plugin.TextCommand):
    def modify_regions(self, edit, modifier):
        regions = self.view.sel()
        use_whole_file =  modifiers.SETTINGS.get("use_entire_file_if_no_selection", True)

        selections = []
        for region in regions:
            if region.empty() and len(regions) == 1 and use_whole_file:
                selection = sublime.Region(0, self.view.size())
            else:
                selection = region

            base_str = self.view.substr(selection)

            modified_str = getattr(modifiers, modifier)(base_str)

            self.view.replace(edit, selection, modified_str)

        sublime.status_message('Casing changed')

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
        self.modify_regions(edit, 'snake_case')

class CaserCamelCaseCommand(CaserCommand):
    def run(self, edit):
        self.modify_regions(edit, 'camel_case')

class CaserWordCommand(CaserCommand):
    def run(self, edit):
        self.modify_regions(edit, 'snake_to_words')
