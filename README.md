# 💅 VSCODE Custom CSS Setup

## Usage

1. Modify the `custom.css` file to your liking. (For an easier time, you can open the HTML/CSS inspector in VSCode under the menu `Help > Toggle Developer Tools` or by pressing `ctrl+shift+i` and then copy the CSS rules you want to use from the inspector to the `custom.css` file.)

1. Run the `main.py` script

1. Open vscode

1. On the command pallette, run reload custom CSS and JS

1. Enjoy!

## Functioning.

What the script will do is:

1. Install the `Custom CSS and JS Loader` extension
1. Set the `'vscode_custom_css.imports'` setting to the path of the `custom.css` file.
1. Set the `'vscode_custom_css.policy'` setting to `true`.

## Caveats

### Linux/Mac

As of now, this script is has only been tested on Windows 10 using powershell and with VSCode installed in the default location.
