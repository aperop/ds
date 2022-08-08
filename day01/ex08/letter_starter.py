import sys


def letter_starter():
    with open("employees.tsv") as f_in:
        lines = [emp.rstrip() for emp in f_in]
    for emp in lines:
        emp = emp.split("\t")
        if (emp[-1] == sys.argv[1]):
            print(f"Dear {emp[0]}, welcome to our team. "
            "We are sure that it will be a pleasure to work with you. "
            "That’s a precondition for the professionals that our company hires.")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        letter_starter()