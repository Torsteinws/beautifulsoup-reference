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
    
def print_soup_props(soup: BeautifulSoup) -> None:
    
    print(color.YELLOW, 'title ..........', color.END, soup.title)          # Html tag
    print(color.YELLOW, 'title.name .....', color.END, soup.title.name)     # Name of the tag  
    print(color.YELLOW, 'title.string ...', color.END, soup.title.string)   # Content of tag
    print(color.YELLOW, 'title.parent ...', color.END, soup.title.parent)   # Head
    print(color.YELLOW, 'title.parent ...', color.END, soup.title.parent)
    print('\n')

    # Can be done for any html elemt:
    print(color.YELLOW, 'p ..............', color.END, soup.p)          # Html tag
    print(color.YELLOW, 'p.name .........', color.END, soup.p.name)     # name of the tag
    print(color.YELLOW, 'a ..............', color.END, soup.a)          # Html tag
    print(color.YELLOW, 'a.string .......', color.END, soup.a.string)   # content of tag
    
    # print(soup.p)
    print('\n')

def find():

    pass

if __name__ == "__main__":
    clear_terminal()
    # The docs reccomend using lxml as parser (third party parser) because it is the fastest. 
    soup = BeautifulSoup(open("./index.html"), "lxml") # The docs reccommend using lxml over html.parser for speed
    
    print_soup_props(soup)


