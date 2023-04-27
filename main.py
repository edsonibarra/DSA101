# This is a sample Python script.
from src.data_structures.circular_linked_list.circular_linked_list import CicularLinkedListObj
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def main():
    cll = CicularLinkedListObj()
    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.append(4)
    cll.print_list()


if __name__ == "__main__":
    main()