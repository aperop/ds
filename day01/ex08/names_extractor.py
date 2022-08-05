import sys


def extract():
    with open(sys.argv[1]) as f_in:
        with open("employees.tsv", mode='w') as f_out:
            for line in f_in:
                name = (line.split(".", 1))[0]
                surname = ((line.split(".", 1)[1]).split("@"))[0]
                f_out.write(name.capitalize() + "\t")
                f_out.write(surname.capitalize() + "\t")
                f_out.write(line)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        extract()