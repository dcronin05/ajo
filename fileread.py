class FileRead:

    def __init__(self, file_name):
        """file_name: name of the Ajo file to be ran."""
        self.FILE_NAME = file_name
        self.COMMANDS = []
        self.read()

    def read(self):
        file = open(self.FILE_NAME, 'r')
        commands = []

        for line in file:
            commands.append(line.split(';')[0])

        self.COMMANDS = commands
