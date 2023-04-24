# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы. 


def generate_points(lang='ru'):
    en = {
        1: 'A, E, I, O, U, L, N, S, T, R'.lower().split(', '),
        2: 'D, G'.lower().strip().split(', '),
        3: 'B, C, M, P'.lower().strip().split(', '),
        4: 'F, H, V, W, Y'.lower().strip().split(', '),
        5: 'K'.lower(),
        8: 'J, X'.lower().strip().split(', '),
        10: 'Q, Z'.lower().strip().split(', '),
    }

    ru = {
        1: 'А, В, Е, И, Н, О, Р, С, Т'.lower().strip().split(', '),
        2: 'Д, К, Л, М, П, У'.lower().strip().split(', '),
        3: 'Б, Г, Ё, Ь, Я'.lower().strip().split(', '),
        4: 'Й, Ы'.lower().strip().split(', '),
        5: 'Ж, З, Х, Ц, Ч'.lower().strip().split(', '),
        8: 'Ш, Э, Ю'.lower().strip().split(', '),
        10: 'Ф, Щ, Ъ'.lower().strip().split(', ')
    }

    return ru if lang == 'ru' else en


def get_word_by_user():
    word = input('Enter your word: ').lower().strip()
    return word.lower()


def choose_language():
    lang = 'ru'
    user_choice = input('Choose language (en/ru): ').lower().strip()
    if user_choice == 'en':
        lang = 'en'
    return lang


def count_points_in_word(word, points_rules):
    points_sum = 0
    for letter in word:
        for point, letters in points_rules.items():
            if letter in letters:
                points_sum += point
                break
    return points_sum


def start_game():
    lang = choose_language()
    word = get_word_by_user()
    points_by_rules = generate_points(lang)
    print(count_points_in_word(word, points_by_rules))



if __name__ == '__main__':
    start_game()