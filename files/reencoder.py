swaps = {   "й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",  
   "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",  
   "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",  
   "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",  
   "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",  
   "б": "b", "ю": "ju", "ё": "jo"}

def swap(s):
    res = ""
    for i in s:
        if i.lower() in swaps.keys():
            isBig = i.isupper()
            res += swaps[i.lower()].capitalize() if isBig else swaps[i]
        else:
            res += i
    return res

with open("cyrillic.txt", 'r') as from_file:
    with open("transliteration.txt", 'w') as to_file:
        for line in from_file:
            to_file.write(swap(line))
