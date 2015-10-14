__author__ = 'Independence'


def plural(num, words):
    if 11 <= num % 100 <= 14:
            return(words[2])
    elif num % 10 == 1:
            return(words[0])
    elif 2 <= num % 10 <= 4:
            return(words[1])
    else:
            return(words[2])
w_list = ['утюг', 'утюга', 'утюгов', 'ложка', 'ложки', 'ложек', 'гармошка',
          'гармошки', 'гармошек', 'чайник', 'чайника', 'чайников']
word = str(input())
num = int(input())
print(num, plural(num, w_list[w_list.index(word):(w_list.index(word))+3]))
