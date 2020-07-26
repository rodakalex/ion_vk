import Ion_vk
import base

auth = Ion_vk.Ion('', '')
# members = auth.groups_getMembers(group_id=150565101)

cities = [
    'Великие Луки', 34,
    'Остров', 1112,
    'Невель', 617,
    'Опочка',
    'Печоры',
    'Порхов',
    'Дно',
    'Дедовичи',
    'Новосокольники',
    'Струги Красные',
    'Пыталово',
    'Себеж',
    'Пушкинские Горы',
    'Идрица',
    'Пустошка',
    'Красногородск',
    'Гдов',
    'Бежаницы',
    'Локня',
    'Новоржев',
    'Кунья',
    'Сосновый Бор',
    'Плюсса',
    'Усвяты',
    'Палкино'
]

def counter_id(index):
    pass


def save_id(usr_id):
    pass


def start():
    for i in base.get_publics():
        group = i.public_id
        break
    index = 0
    while True:
        members = auth.groups_getMembers(
            group_id=group,
            offset=index,
            fields='city'
        )
        b_flag = len(members['items']) != 1000
        for i in members['items']:
            # base.save_user_in_the_public(i, group, 1)
            print(f'{i}')
        index += 1000
        if b_flag:
            break


if __name__ == '__main__':
    start()
