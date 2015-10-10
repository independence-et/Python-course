__author__ = 'independence'


def plural(num, word):
    words = ['утюг', 'утюга', 'утюгов', 'ложка', 'ложки', 'ложек', 'гармошка',
             'гармошки', 'гармошек', 'чайник', 'чайника', 'чайников']
    if word in words:
        a = words.index(word)
        if a in [1, 2, 4, 5, 7, 8, 10, 11]:
            print('Похоже, вы и без меня справитесь.')
        elif 11 <= num % 100 <= 14:
            a = a + 2
        elif num % 10 == 1:
            a = a
        elif 2 <= num % 10 <= 4:
            a = a + 1
        else:
            a = a + 2
        print(num, words[a])
    else:
        print('Facepalm')
user_word = str(input())
user_num = int(input())
plural(user_num, user_word)
