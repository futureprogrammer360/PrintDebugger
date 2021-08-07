# 🤖 PrintDebugger

[PrintDebugger](https://packagecontrol.io/packages/PrintDebugger) is a [Sublime Text](https://www.sublimetext.com/) plugin that allows easy insertion of both debugging and empty print statements through keybindings.

If cursor is on a word, a print statement displaying the value of that variable will be inserted below the current line. If multiple words are selected, they are treated as one variable name. If cursor is not on a word, an empty print statement is inserted.

## 💻 Installation

The easiest way to install PrintDebugger is through Package Control. After it is enabled inside Sublime Text, open the command palette and find **Package Control: Install Package** and press `ENTER`. Then, find **PrintDebugger** in the list. Press `ENTER` again, and this plugin is installed!

## 📈 Usage

To print out a meaningful message containing the name and value of a variable:

* Click on or select that variable
* Press the `print_debug` keybinding (default is `ALT+D`)

To view the values of a variable before and after a line:

* Click on or select that variable
* Press the `print_debug` keybinding with `before_and_after` set to `true` (default is `ALT+SHIFT+D`)

To insert an empty print statement at the cursor:

* Press the `print_debug` keybinding (default is `ALT+D`)

## ⚙ Configuration

The PrintDebugger plugin is fully customizable. The syntax of several languages are included when the plugin is installed. The syntax of print/debug statements, scopes, and file extensions associated with each language can be customized. New syntax can also be added in settings.
