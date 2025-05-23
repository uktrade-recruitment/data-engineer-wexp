import argparse
from load_data import load_data
from exporters import get_countries, get_top_types_per_country


def test(arguments):
    if len(list(get_countries())) > 0:
        print("OK: There is some test data. Let's go.")
    else:
        print("ERROR: There is no test data.")


def show_countries(*args):
    for country in get_countries():
        print(country)


def show_top_types(*args):
    def top_three(items):
        return sorted(items, key=lambda i: i.value, reverse=True)[:3]

    for country in get_top_types_per_country().values():
        print(country)
        for index, export in enumerate(top_three(country.exports.values())):
            print(f"\t{index + 1}: {export}")


def show(commands):
    if commands == []:
        print("Incorrect syntax. \nUsage: wexp show <what>\n")
        return

    {"countries": show_countries, "top": show_top_types}[commands[0]](commands[1:])


def main():
    print()

    load_data()

    parser = argparse.ArgumentParser()
    parser.add_argument("command", nargs="+")
    arguments = parser.parse_args()

    command_functions = {"test": test, "show": show}

    command_functions[arguments.command[0]](arguments.command[1:])

    print()


main()
