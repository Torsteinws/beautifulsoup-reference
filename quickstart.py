import os
from bs4 import BeautifulSoup
from time import sleep

class color:
    YELLOW = '\033[33m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    END = '\033[m'    
        
def clear_terminal():
    os.system('cls')

def header_print(text :str, header_color :color = color.YELLOW) -> None:
    print(header_color, '::::::', text.upper(), '::::::', color.END)    

def print_soup_props(soup: BeautifulSoup) -> None:
    
    # print(color.YELLOW, '....... title ..........\n', color.END)
    header_print('title')
    print(soup.title)          # Html tag
    
    header_print('title.name')
    print(soup.title.name)     # Name of the tag  

    header_print('title.string')
    print(soup.title.string)   # Content of tag

    header_print('title.parent')
    print(soup.title.parent)   # Head

    # Can be done for any html elemt:
    header_print('p')
    print(soup.p)          # Html tag
    header_print('p.name')
    print(soup.p.name)     # name of the tag
    header_print('a')
    print(soup.a)          # Html tag
    header_print('a.string')
    print(soup.a.string)   # content of tag

    print('\n')

def find():

    pass

if __name__ == "__main__":
    clear_terminal()
    # The docs reccomend using lxml (third party) over html.parser (built in) because it is faster 
    soup = BeautifulSoup(open("./index.html"), "lxml")
    
    print_soup_props(soup)

    # 
    # print(soup.text)

    # print(soup.)
