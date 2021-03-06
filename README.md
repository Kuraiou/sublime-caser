Caser
=====

Case-changing tools for Sublime Text 2 & 3


Installation 
-------------

1. add the repository to your package control via "Package Control: Add Repository"
    * enter "https://github.com/kuraiou/sublime-caser"
2. install the package via "Package Control: Install Package'
    * select "Sublime Caser"

Keyboard Shortcuts:
-------------------

-   Linux: <kbd>ctrl+c,ctrl+[COMMAND]</kbd>
-   Windows: <kbd>ctrl+c,ctrl+[COMMAND]</kbd>
-   OS X: <kbd>ctrl+c,ctrl+[COMMAND]</kbd>

Commands:

-   `s`: snake_case
-   `c`: CamelCase
-   `d`: downcase
-   `u`: UPCASE
-   `t`: Capitalize Each Word (Titleize)
-   `w`: split into words -- splits the snake_separator (`_`) into multiple words

If selection is empty and configuration entry
**use_entire_file_if_no_selection** is true, tries to change whole file.

Settings:
---------

* `use_entire_file_if_no_selection` - if set, selecting no regions is the same as selecting the whole file.
* `omit_comments` - if set, comment blocks will not be modified.
* `word_separator` - for "split into words". defaults to ' '
* `snake_separator` for snake_case and split into words. defaults to '_'
