#!../ex00/dhawkgir/bin/python3

import os


def install_libs():
    os.system("pip3 install beautifulsoup4 pytest $1>/dev/null")

def save_req():
    os.system('pip3 freeze > requirements.txt')
    os.system('cat requirements.txt')


if __name__ == '__main__':
    install_libs()
    save_req()
