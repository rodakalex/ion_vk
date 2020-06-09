import Ion_vk
import time

vk = Ion_vk.Ion('', '')


public_id = [
    # https://vk.com/public26419239
    # Смейся до слёз :D
    -26419239,
    # https://vk.com/public45441631
    # ПРИКОЛЫ | Смеяка
    -45441631,
    # https://vk.com/public57846937
    # MDK
    -57846937,
]


def check_yesterday(date):
    return time.time() - date - 86400 < 0


def check_month(date):
    # 2678400 секунд в месяце
    return time.time() - date > 2678400


def test_photo_download():
    vk.photo(
        photos=['./file.jpg'],
        album_id=273055557
    )
