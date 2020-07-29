import Ion_vk
import base

auth = Ion_vk.Ion(
    login='',
    token=''
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
        for city in cities:
            items = auth.users_search(
                group_id=public.public_id,
                city=city.city_id)['items']
            for i in items:
                print(f'Save user {i["first_name"]} {i["last_name"]}')
                base.save_user(
                    user_id=i['id'],
                    public_id=public.public_id,
                    first_name=i['first_name'],
                    last_name=i['last_name'],
                    city=city.city,
                    city_id=city.city_id,
                    is_closed=i['is_closed'],
                    is_target=public.is_target
                )


if __name__ == '__main__':
    pre_save_users_from_public()
