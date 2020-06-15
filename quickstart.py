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
    print('\n')
    print(header_color + ':::::::::::::::::', text.upper(), ':::::::::::::::::', color.END)    

def common_props(soup :BeautifulSoup) -> None:
    header_print('text')
    print(soup.text)

def tag_object(soup :BeautifulSoup) -> None:
    # For this example the html tag 'title' is used. 
    # However, any html tag (such as 'a', 'p', 'img' ...) can be used instead
    header_print('The tag object ')
    print('soup.title .........', soup.title)           # The html tag object
    print('type ...............', type(soup.title))     # Type of the tag object 
    print('soup.title.name ....', soup.title.name)      # name of the tag
    print('soup.title.string...', soup.title.string)    # Content of the tag
    print('soup.title.attrs ...', soup.title.attrs)     # Attributes in the tag
    print('soup.title[id] .....', soup.title['id'])     # Attributes can be accesed like a dictionary


def searching_filters(soup :BeautifulSoup) -> None:
    
    # Finds every anchor (a tag) and returns them as a list
    header_print('tag filter: "a"')
    for anchor in soup.find_all('a'):
        print(anchor)

    # Finds all tags that matches 'b' or 'title'
    header_print('list filter: ["b", "title"]')
    for tag in soup.find_all(['b', 'title']):
        print(tag)

    # TODO: demo with regex filter

    # Finds entire document
    document = soup.find_all(True)      
    # print(document)

    # Use an anonymous function to find every element that has an id attribute
    header_print('function filter: has id')
    has_id = lambda tag : tag.has_attr('id')    # Returns true or false
    for tag_with_id in soup.find_all(has_id):
        print(tag_with_id)

    # The function filter can be as complicated as needed ...
    header_print('function filter: Anchors that contains Elsie')
    anchor_contains_elsie = lambda tag : tag.name == 'a' and tag.string == 'Elsie' 
    elsie = soup.find_all(anchor_contains_elsie)
    print(elsie)
    
def find_method_arguments(soup :BeautifulSoup) -> None:

    # Filter on tag attributes:
    header_print('Attributes keyword')
    # id attributes
    print('id = link1 ..............', soup.find(id='link1'))
    # class attributes
    for sister in soup.find_all(class_ = 'sister'):
        print('class_ = sister .........' ,sister)
    # has charset attribute
    print('charset = True ..........' ,soup.find_all(charset=True))

    # Search the content of by using the string keyword
    header_print('String keyword')
    print('string = Elsie ............', soup.find(string='Elsie'))
    print('(string = Elsie).parent ...', soup.find(string='Elsie').parent)
    print('"a", string = Elsie .......', soup.find('a', string='Elsie'))


def css_selectors(soup :BeautifulSoup) -> None:
    # css selectors can be used inside the select() method to find elements in the dom.

    header_print('Using css selectors with .select()')
    print('slector ........... result')

    # Select tag
    for title in soup.select('title'):  # .select() always returns a list
        print('title ............', title)
    # select nested tag
    for anchor in soup.select('body p a'):
        print('body p a .........', anchor)
    # select class
    for sister in soup.select('.sister'):
        print('.sister ..........', sister)
    # select id
    print('#title-id ........', soup.select('#title-id'))

if __name__ == "__main__":
    clear_terminal()
    # The docs reccomend using lxml (third party) over html.parser (built in) because it is faster 
    with open('./index.html') as markup:
        soup = BeautifulSoup(markup, 'lxml')

    # common_props(soup)
    # tag_object(soup)
    # searching_filters(soup)
    # find_method_arguments(soup)
    css_selectors(soup)