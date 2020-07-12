# Tasks
## Inventory
A store stores its inventory in a dictionary, the keys to which are items and quantity values:
```
inv = {'cheese': 8, 'bread': 15, 'poppy': 10, 'dog joy': 2, 'pate': 10, 'mortadella': 4, 'sausage': 7}
```
Note: values are numbers (10) and not strings ("10").

Write the function stock(inventory, item) to tell how many product item we have in stock. If you had the above dictionary with inventory stored in the inv dictionary, the stock call (inv, "poppy") must return 10.
```
>>> stock (inv, "poppy")
10
```
Write a function sales(inventory, item, quantity) that reduces the quantity of an item in the inventory for quantity. The sales call (inv, "poppy", 3) (we sold three poppies) must change the inv dictionary by reducing the value of the "poppy" key by 3.
```
>>> inv
{'cheese': 8, 'bread': 15, 'poppy': 10, 'dog joy': 2, 'pate': 10, 'mortadella': 4, 'sausage': 7}
>>> sell (inv, "poppy", 3)
>>> inv
{'cheese': 8, 'bread': 15, 'poppy': 7, 'dog joy': 2, 'pate': 10, 'mortadella': 4, 'sausage': 7}
```
Tip: if you know too much and have already heard of arguments by value and by reference, abandon those thoughts until further notice, as they are not relevant to Python.

Write a function deficit(inventory, order) that receives two dictionaries: the first represents the current inventory, and the second what a customer orders; the order is presented with a dictionary of the same form as the inventory. The function must return a new dictionary in which it will be written how much we still have to buy so that we can supply the customer with everything he wants. If, for example, a customer wants three pâtés, nine sausages and one beer, the function must return the dictionary {"sausage": 2, "beer": 1}. Two sausages because we have seven and the customer wants nine. Pâtés will not need to be ordered as we have enough of them. But we need beer because we don’t have any.
```
>>> deficit (inv, {"pate": 3, "sausage": 9, "beer": 1})
{"sausage": 2, "beer": 1}
```
## The most common
Write the function most_often(s) that returns the word and character that appear most often in the given string. In the string 'in to in ono in to smo mi' the word 'in' and the sign ' '(space) appear most often.
```
>>> most common ('aa bb aa')
('aa', 'a')
>>> most often ('and this and that and this is us')
('in', '')
```
For those with quick fingers, write the most common_edit function, which returns all words and letters that appear in a given string, sorted by number of occurrences (arrange words and letters with the same number of occurrences in alphabetical order).
```
>>> najgostejse_urejene ('aa bb aa')
(['aa', 'bb'], ['a', '', 'b'])
>>> most often_organized ('and this and that and this are us')
(['in', 'to', 'mi', 'ono', 'smo'], ['', 'o', 'i', 'n', 'm', 't', 's' ])
```
## Randomly generated text
We want to write a program that will randomly generate text. Of course, it’s not good to just randomly choose words and glue them together, as that would get something completely unreadable. We will tackle the task a little smarter. Let’s say a program has some text available ('in to in ono smo mi') from which it can learn. We will start our random text with any word, say this. We continue by asking ourselves which words appear in the learning text after the word to. In our case, it’s just the word in. The process is then repeated with the word in. If a word in a learning text is followed by more than just one word, it is chosen at random. We will tackle the task step by step:

Write a function successor(txt) that builds a list of words that appear in the text after the word b for each word b in the string txt. Some examples:
```
>>> successors ('in in in in')
{'in': ['in', 'in', 'in']}
```
After the word in, the word in appears in three places.
```
>>> successors('in to in ono in to smo mi')
{'smo': ['mi'], 'to': ['in', 'smo'], 'ono': ['in'], 'in': ['to', 'ono', 'to']}
```
Only the word mi appears after the word mi, while, say, both the word mi and the word in appear after the word it.

Now write another function text(title, num_besed) that accepts a dictionary created by the successors function and generates random text long num_besed words.

You can test your program on Orwell's novella.
```
>>> import urllib.request
>>> txt = urllib.request.urlopen ('http://squeeb1134.tripod.com/1984.txt') .read () .decode ('utf8')
>>> text (successors (txt), 20)
'Big Brother had been drained out of the hands of me for his heart banged, seeming to grow less. Always'
```
Due to randomness, the task text is difficult to check with unittests. The enclosed test checks only the most basic properties.
## Family tree
The family tree is stored in the family list:
```
family = [('bob', 'mary'), ('bob', 'tom'), ('bob', 'judy'), ('alice', 'mary'),
    ('alice', 'tom'), ('alice', 'judy'), ('renee', 'rob'), ('renee', 'bob'),
    ('sid', 'slave'), ('sid', 'bob'), ('tom', 'ken'), ('ken', 'suzan'), ('rob', 'jim')]
```
Each tuple contains two names: the name of the parent and the name of the child. Tuple (‘bob’, ‘mary’) tells us that Bob is Mary’s father, terka (‘bob’, ‘tom’) tells us that Bob is Tom’s father, and so on.


<img src="https://ucilnica1819.fri.uni-lj.si/file.php/166/vaje/family.png" 
alt="tree" />

Write a family_tree(family) function that accepts a list of the family tree and returns a dictionary that lists all of its children for each parent.
```
>>> family_tree (family)
{'renee': ['rob', 'bob'], 'ken': ['suzan'], 'rob': ['jim'], 'sid': ['rob', 'bob'],. .., 'bob': ['mary', 'tom', 'judy']}
```
Write a function  children(tree, name), which returns a list of all the person's children in the family tree. In case the person does not have children, return an empty list.
```
>>> tree = family_tree (family)
>>> children (tree, 'alice')
['mary', 'tom', 'judy']
>>> children (tree, 'mary')
[]
```
Write a grandchildren(tree, name) function that returns a list of all the grandchildren of the person.
```
>>> grandchildren (tree, 'renee')
['jim', 'mary', 'tom', 'judy']
```
The next feature is a little more challenging than the others, so you can skip it. Write a successors(tree, name) function that returns a list of all the person's successors.
```
>>> successors (tree, 'tom')
['ken', 'suzan']
>>> successors (tree, 'sid')
['slave', 'bob', 'jim', 'mary', 'tom', 'judy', 'ken', 'suzan']
```
## code
The string '\x19\x14\x1c]\x19\x0f\x14\t\x13\x18\t]\x12\x0e[\n\x1a\t\x18\x15\x12\x13\x1c' can be decrypted with the following function:
```
def sifriraj(niz, kljuc):
    return ''.join(chr(ord(c) ^ (kljuc // 256**(i % 2) % 256)) for i, c in enumerate(niz))
```
The problem is that we don’t know the key. We only know that it is somewhere between 0 and 65536. We suspect that the original message is in English and that all the words are grammatically correct. Write a password function (string) that returns an encrypted message.
```
>>> sifriraj('strawberry pudding', 1337)
'JqKdNg\\wK|\x19uLa]lWb'
>>> sifriraj('JqKdNg\\wK|\x19uLa]lWb', 1337)
'strawberry pudding'
>>> sifra('JqKdNg\\wK|\x19uLa]lWb')  # TODO
'strawberry pudding'
```
Hint:
You do not need to understand the encrypt function.
Help yourself with a list of English words. You can read it with [words = [w for w in open ("Usr.dict.words")]; after that the words will be a list of words, but it might make sense to immediately process it into something more useful.
