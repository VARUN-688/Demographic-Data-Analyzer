# This entrypoint file to be used in development. Start by reading README.md
import demographic_data_analyzer
from unittest import main

# Test your function by calling it here
demographic_data_analyzer.calculate_demographic_data()

# Run unit tests automatically
main(module='test_module', exit=False)


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
