import os
from bs4 import BeautifulSoup

def clear_terminal():
    os.system('cls')

if __name__ == "__main__":
    clear_terminal()
    soup = BeautifulSoup(open("./index.html"), "html.parser")
    print(soup.prettify())