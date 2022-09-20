#!../ex02/dhawkgir/bin/python3

import os


def install_libs() -> None:
    os.system("pip install --upgrade pip")
    os.system("pip install beautifulsoup4 pytest $1>/dev/null")


def save_req() -> None:
    os.system('pip freeze > requirements.txt')
    os.system('cat requirements.txt')


if __name__ == '__main__':
    if os.environ['VIRTUAL_ENV'] != os.environ['PWD'] + '/dhawkgir':
        print(os.environ['VIRTUAL_ENV'])
        print(os.environ['PWD'] + '/dhawkgir')
        raise EnvironmentError
    install_libs()
    save_req()
