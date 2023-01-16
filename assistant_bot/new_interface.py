from abc import ABC, abstractmethod
from input_error import input_error


class InterfaceABC(ABC):

    @abstractmethod
    def handler(self, command_dict, user_input):
        pass


class Interface(InterfaceABC):

    @input_error
    def handler(self, command_dict, user_input="help"):
        parsed_input =user_input.lower().strip().split()
        if parsed_input[0] in command_dict:
            if len(parsed_input) == 1:
                action = command_dict.get(parsed_input[0])()
            else:
                action = command_dict.get(parsed_input[0])(
                    (" ").join(parsed_input[1:]))
        else:
            raise KeyError
        return action
