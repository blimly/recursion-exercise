## Rekursioon

Et saada aru rekursioonist, pead sa kõigepealt aru saama rekursioonist.

![fixing_problems](https://imgs.xkcd.com/comics/fixing_problems.png)

Funktsioon on rekursiivne kui ta kutsub end enda sees välja.

```python
def recursion():
    print("recursion is")
    recursion()
```

Sellel funktsioonil pole lõppu seega jookseks ta virtuaalselt lõputult. Python aga viskab veateate kui rekursiooni sügavus on läinud liiga suureks. ``(RecursionError: maximum recursion depth exceeded)``

Et rekursioon oma töö lõpetaks on vaja baas juhtumit kus funktsioon ei kutsu enam iseennast välja vaid tagastab mingi teise väärtuse.

```python
def limited_depth(depth):
    if depth == 0:  # base case
        print("recursion ended")
    else:
        print(f"depth is {depth}")
        limited_depth(depth - 1)
```

## Abistavad lingid

- [Rekursioon (PyDoc)](https://ained.ttu.ee/pydoc/recursion.html)
- [Recursion (Wikipedia)](https://en.wikipedia.org/wiki/Recursion)

## Ülesanne

Sinu ülesanne on kirjutada kolm rekursiivset funktsiooni.

``def count_vowels(s: str)``: Funktsioon saab ette sõne ja tagastab kui palju täishäälikuid selles sõnes on. Lahendus peab olema rekursiivne.

``def permutations(s)``: Funktsioon, mis saab ette sõne ja tagastab kõik erinevad sõne permutatsioonid (ümberpaigutused). Lahendus peab olema rekursiivne. Oluline on, et tagastatud list ei sisaldaks duplikaate.

``def nested_sum(lst: list)``: Funktsioon, mis tagastab kõikide täisarvude summa pesastatud järjendis. (Hint: uuri  ``isinstance(lst, list)`` kohta)

## Mall

```python
"""The end is never the end is never... (version 0.1)"""


def count_vowels(s: str) -> int:
    """
    Return the number of vowels in string using recursion.
 
    count_vowels("") => 0
    count_vowels("abcde") => 2
 
    :param s: string
    :return: vowels in string
    """
    pass


def nested_sum(lst: list) -> int:
    """
    Return the sum of the integers in nested list.

    sum_nested([1, [2, [3, [4]]]]) => 10
    sum_nested([1, [1], [1, [1]], [1, [1], [1, [1]]]]) => 8

    :param lst: list
    :return: sum of numbers
    """
    pass


def permutations(s) -> list:
    """
    Return a list by permuting the characters of s.
    NB! the order of the list is important

    permutations("") => ['']
    permutations("xyz") => ['zyx', 'yzx', 'yxz', 'zxy', 'xzy', 'xyz']
    permutations("aab") => ['baa', 'aba', 'aab']

    :param s:
    :return:
    """
    pass

```

