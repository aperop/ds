def read_and_write():
    with open("ds.csv") as f_in:
        with open("ds.tsv", mode='w') as f_out:
            for line in f_in:
                f_out.write(("\"\t\"".join(line.split("\",\"")))
                            .replace(",true,", "\ttrue\t")
                            .replace(",false,", "\tfalse\t"))


if __name__ == '__main__':
    read_and_write()
