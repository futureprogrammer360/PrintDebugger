# 🤖 PrintDebugger

[PrintDebugger](https://github.com/futureprogrammer360/PrintDebugger) is a [Sublime Text](https://www.sublimetext.com/) plugin that allows easy insertion of both debugging and empty print statements.

## 💻 Installation

The easiest way to install PrintDebugger is through [Package Control](https://packagecontrol.io/packages/PrintDebugger). After it is enabled inside Sublime Text, open the command palette and find **Package Control: Install Package** and press `ENTER`. Then, find **PrintDebugger** in the list. Press `ENTER` again, and this plugin is installed!

## 📈 Usage

The plugin includes the command `print_debug`, which can be run in the command palette as `PrintDebugger: Print Debug`. There is a variant of the command with argument `before_and_after` set to `true`: `PrintDebugger: Print Debug (Before and After)`.

**To print out a meaningful message containing the name and value of a variable:**

* Click on or select that variable
* Run the `PrintDebugger: Print Debug` command

**To view the values of a variable before and after a line:**

* Click on or select that variable
* Run the `PrintDebugger: Print Debug (Before and After)` command

**To insert an empty print statement at the cursor:**

* Run the `PrintDebugger: Print Debug` command

## ⚙ Customization

The PrintDebugger plugin is fully customizable.

### 🔧 Preferences

The syntax of several languages are included by default when the plugin is installed. The syntax of print/debug statements, scopes, and file extensions associated with each language can be customized. New syntax can also be added in settings.

To modify or add print/debug syntax, run the `Preferences: PrintDebugger` command in the command palette.

### ⌨ Keybindings

Keybindings can be created for the commands.

* Run the `Preferences: PrintDebugger Key Bindings` command in the command palette.
* Add your keybindings!

Below is an example of the keybinding file:

```json
[
    {
        "keys": ["alt+d"],
        "command": "print_debug"
    },
    {
        "keys": ["alt+shift+d"],
        "command": "print_debug",
        "args": { "before_and_after": true }
    }
]
```
