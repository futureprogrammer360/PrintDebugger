import sublime
import sublime_plugin


class PrintDebugCommand(sublime_plugin.TextCommand):
    def run(self, edit, before_and_after=False):
        settings = sublime.load_settings("PrintDebugger.sublime-settings")
        scope = self.view.scope_name(self.view.sel()[0].begin())
        extension = self.view.file_name().split(".")[-1]

        # Determine syntax
        for syntax in settings.get("syntax"):
            if syntax["scope"] in list(scope.split(" ")) or extension in syntax["extensions"]:
                current_syntax = syntax
                break
        else:
            sublime.error_message(
                f"No syntax found for the current scope ({scope.split(' ')[0]}) and extension ({extension}). Maybe you forgot to define the syntax in PrintDebugger.sublime-settings?"
            )
            return

        # Determine debug and print statements
        debug_statement = current_syntax["debug"]
        print_statement, back = current_syntax["print"]
        if settings.get("force_double_quotes"):
            debug_statement = debug_statement.replace("'", '"')
            print_statement = print_statement.replace("'", '"')

        region = self.view.sel()[0]
        if region.begin() == region.end():  # No selection
            selection = self.view.substr(self.view.word(region))
            if not selection.strip():  # Cursor not on a word, insert empty print statement
                self.view.run_command("insert", {"characters": print_statement})
                for _ in range(back):
                    self.view.run_command("move", {"by": "characters", "forward": False})
                return
        else:
            selection = self.view.substr(region)

        if before_and_after:
            self.view.run_command("run_macro_file", {"file": "res://Packages/Default/Add Line Before.sublime-macro"})
            self.view.run_command("insert", {"characters": debug_statement.replace("!!!", selection)})
            self.view.run_command("move", {"by": "lines", "forward": True})
            self.view.run_command("run_macro_file", {"file": "res://Packages/Default/Add Line.sublime-macro"})
            self.view.run_command("insert", {"characters": debug_statement.replace("!!!", selection)})
        else:
            self.view.run_command("run_macro_file", {"file": "res://Packages/Default/Add Line.sublime-macro"})
            self.view.run_command("insert", {"characters": debug_statement.replace("!!!", selection)})
