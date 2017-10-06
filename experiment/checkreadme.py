from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.checkreadme.api.manager import Manager

class CheckreadmeCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_checkreadme(self, args, arguments):
        """
        ::

          Usage:
                checkreadme --file=FILE

          This command checks if readme file is valid or not

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        arguments.FILE = arguments['--file'] or None

        print(arguments)

        m = Manager()

        if arguments.FILE:
            print("option a")
            m.list(arguments.FILE)

        elif arguments.list:
            print("option b")
            m.list("just calling list without parameter")

        # Read input file
        with open(arguments.FILE, 'r') as f:
            lines = f.readlines()

        all_lines = []
        for line in lines:
            all_lines.append(line.replace("\n",""))

        lines = all_lines

        # print(lines)

        # Loop through all the lines
        for line in lines:
            counter = counter + 1

            if not in_yaml and line.startswith('```'):
                in_yaml = True
            elif in_yaml and line.startswith("```"):
                in_yaml = False
            elif in_yaml:
                content.append(line)

        s = '\n'.join(content)

        try:

            d = yaml.load(s)
            print("The file is in a valid yaml format")

        except Exception as e:
            print ("ERROR: The file is not in a valid yaml format")
