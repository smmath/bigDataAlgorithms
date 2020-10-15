from collections import namedtuple


def format_variable(variable):
    return f'| {variable.name}: {variable.value}'.ljust(variable.padding)


class AlgorithmPrinter:
    def __init__(self):
        self.step_data = []

    def push_variable(self, name, value, padding=12):
        Variable = namedtuple('Variable', 'name value padding')
        self.step_data.append(Variable(name, value, padding))

    def print_step(self):
        for s in self.step_data:
            print(format_variable(s), end='')
        print(' |')
        self.step_data = []
