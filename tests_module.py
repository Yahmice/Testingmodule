stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

maximum = max(stats.values()) # максимальное значение в словаре

def get_key(stats, value):  # функция для получения ключа по значению
    for k, v in stats.items():
        if v == value:
            return k

###########################################


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def converter(id):
    for number in id.values():
        return set(number)

###########################################

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]


def country(geo_log):
    for visit in geo_log:
        for spisok in visit.values(): 
            if spisok[1] == 'Россия':
                found = spisok
    return found
