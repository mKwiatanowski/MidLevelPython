
import os

def CountWords(path):
    with open(path,'r', encoding='ulf-16') in f:
        count = f.read()
        word_count = len(count.split())
    return word_count


path = r'C:\temp\pogoda.txt'

if os.path.isfile(path):
    print("There are {} words in the file {}".format(CountWords(path), path))


# wyrażenie logiczne, którego wynik będzie taki sam jak w if
os.path.isfile(path) and print("There are {} words in the file {}".format(CountWords(path), path))


