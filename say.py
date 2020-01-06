class Say:

    def __init__(self, string):
        self.RAW_STRING = string
        self.ARG = ''
        self.parse_command()

    def parse_command(self):
        command_line = self.RAW_STRING

        if 'say' not in command_line:
            raise IncorrectSayCommand('No "say" keyword found in line.')
        else:
            self.ARG = command_line.split('say: ')[1]
            self.determine_command()

    def determine_command(self):
        if self.ARG == '"':
            self.display_string()
        elif '+' or '-' or '/' or '*' in self.ARG:
            self.display_string()

    def display_string(self):
        the_string = self.ARG[1:-1]
        print(the_string)

    def display_math(self):
        # TODO: create method to process math arguments
        pass


class IncorrectSayCommand(Exception):
    pass
