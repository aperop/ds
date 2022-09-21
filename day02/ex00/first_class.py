class Must_read:
    try:
        with open("data.csv", mode="r") as f_in:
            print(f_in.read())
    except:
        pass


if __name__ == '__main__':
    Must_read()
