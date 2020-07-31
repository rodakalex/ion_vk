import Ion_vk
import base
import time

global index
index = 0

auth = Ion_vk.Ion(
    login='',
    password=''
)


def save_city_target(cities):
    for i in cities:
        area = auth.database_getCities(
            region_id=1069004,
            country_id=1,
            q=i,
            count=1000
        )
        for j in area['items']:
            if j['region'] == 'Псковская область':
                base.save_city(city=j['title'], city_id=j['id'])


def pre_save_users_from_public():
    publics = base.get_publics()
    cities = base.get_city()
    for public in publics:
        parse_public(cities, public)


def parse_public(cities, public):
    for city in cities:
        parse_city(city, public)


def parse_city(city, public):
    response = auth.execute(
        'return API.users.search({'
        f'"group_id": {public.public_id}, '
        '"count": 1000, '
        f'"city": {city.city_id}'
        '});'
    )
    time.sleep(3)
    for user in response['items']:
        make_user(city, public, user)


def make_user(city, public, user):
    global index
    base.save_user(
        user_id=user['id'],
        first_name=user['first_name'],
        last_name=user['last_name'],
        city=city.city,
        city_id=city.city_id,
        is_closed=user['is_closed'],
        public_id=public.public_id,
        is_target=public.is_target
    )
    index += 1
    print(f'{index}. {user["first_name"]} {user["last_name"]} добавлен(а)')
    # time.sleep(1)


if __name__ == '__main__':
    pre_save_users_from_public()
