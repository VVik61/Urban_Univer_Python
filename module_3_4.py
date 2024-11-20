# Самостоятельная работа по уроку "Произвольное число параметров"
# Функция должна составить новый список same_words только из тех слов\
# списка other_words, которые содержат root_word или наоборот root_word\
# содержит одно из этих слов

def single_root_words(root_word, *other_words):
    same_words = []
    for w in other_words:
        if root_word.upper() in w.upper() or w.upper() in root_word.upper():
            same_words.append(w)
    return same_words


result1 = single_root_words('rich', 'richiest',\
                             'orichalcum', 'cheers', 'richies')
print(result1)

result2 = single_root_words('Disablement', 'Able',\
                            'Mable', 'Disable', 'Bagel')
print(result2)