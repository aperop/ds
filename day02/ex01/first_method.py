class Research:

    @staticmethod
    def file_reader():
        try:
            with open("data.csv", mode="r") as f_in:
                return f_in.read()
        except:
            pass


if __name__ == '__main__':
    print(Research().file_reader())
