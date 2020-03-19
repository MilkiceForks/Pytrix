from interaction.control import Control, commandDict, commandFunc, commandArgs, argsAlias
import copy

class OptionsParser:
    def __init__(self, command, args):
        self.command = str(command);
        self.args = args;
    def parse(self):
        if self.command not in commandFunc:
            return False, "No such command", None, None
        result = copy.deepcopy(commandArgs[self.command])
        values = []
        argValue = False
        prevOpt = ""
        for option in self.args:
            if argValue:
                if option.startswith("-"):
                    return False, "Missing argument values for {}".format(prevOpt), None, None
                result[prevOpt]['value'] = option
                argValue = False
                continue
            if option.startswith("--"):  # Full arg name
                optName = option[2:]
                if optName not in result:
                    return False, "Unknown args {}".format(optName), None, None
                if result[optName]['isSwitch']:  # Switch
                    result[optName]['value'] = not result[optName]['value']
                else:  # Need extra info
                    argValue = True
                    prevOpt = optName
            elif option.startswith("-"):  # Parse each char
                for c in option[1:]:
                    if c not in argsAlias[self.command]:
                        return False, "Unknown args {}".format(c), None, None
                    optName = argsAlias[self.command][c]
                    if result[optName]['isSwitch']:
                        result[optName]['value'] = not result[optName]['value']
                    else:
                        if len(option[1:]) > 1:  # More than one abbreviated arguments
                            return False, "Arguments that requires extra info should not be abbreviated with other arguments.", None, None
                            return
                        argValue = True
                        prevOpt = optName
            else:  # normal values
                values.append(option)
        if argValue:
            return False, "Missing argument values for {}".format(prevOpt), None, None
        return True, None, result, values

