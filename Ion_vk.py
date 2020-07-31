import vk_api
import requests


def __download_photo__(url):
    with open('file.jpg', 'wb') as file:
        r = requests.get(url, allow_redirects=True)
        file.write(r.content)


class Ion:
    # def __init__(self, login, token):
    #     vk_session = vk_api.VkApi(login=login, token=token)
    #     vk_session.auth()
    #     self.vk = vk_session.get_api()
    #     self.upload = vk_api.VkUpload(vk_session)

    def __init__(self, login, password):
        vk_session = vk_api.VkApi(login, password)
        vk_session.auth()
        self.vk = vk_session.get_api()
        self.upload = vk_api.VkUpload(vk_session)

    # Получить записи со стены
    def wall_get(
            self, owner_id, domain=None, offset=None, count=None, filter=None,
            extended=None, fields=None
    ):
        """
        https://vk.com/dev/wall.get

        :param owner_id:
            Идентификатор пользователя или сообщества, со стены которого
            необходимо получить записи (по умолчанию — текущий пользователь).
            Для сообществ идентификатор должен быть отрицательным.


        :param domain:
            Короткий адрес пользователя или сообщества


        :param offset:
            Смещение, необходимое для выборки определенного подмножества
            записей.


        :param count:
            Количество записей, которое необходимо получить.
            Максимальное значение: 100


        :param filter:
            Определяет, какие типы записей на стене необходимо получить.

            Возможные значения:
                suggests — предложенные записи на стене сообщества. Доступно
                только при вызове с передачей access_token);
                postponed — отложенные записи (доступно только при вызове с
                передачей access_token);
                owner — записи владельца стены;
                others — записи не от владельца стены;
                all — все записи на стене (owner + others).


        :param extended:
            1 — в ответе будут возвращены дополнительные поля profiles и
            groups, содержащие информацию о пользователях и сообществах. По
            умолчанию: 0.


        :param fields:
            Список дополнительных полей для профилей и сообществ, которые
            необходимо вернуть. Обратите внимание, этот параметр учитывается
            только при extended=1.


        :return:
            Здесь будет описание тех JSON параметров, которые я буду в
            дальнейшем использовать
        """
        return self.vk.wall.get(
            owner_id=owner_id, domain=domain, offset=offset, count=count,
            filter=filter, extended=extended, fields=fields,
        )

    def upload_photo(self, photos, album_id, latitude=None, longitude=None,
                     caption=None, description=None, group_id=None):
        for i in photos:
            if i.split(':')[0] == 'https':
                __download_photo__(photos)
                photos = './file.jpg'

        self.upload.photo(
            photos=photos, album_id=album_id, latitude=latitude,
            longitude=longitude, caption=caption, description=description,
            group_id=group_id
        )

    def wall_post(
            self, owner_id, friends_only=None, from_group=None,
            message=None, attachments=None, services=None, signed=None,
            publish_date=None, lat=None, long=None, place_id=None,
            post_id=None, guid=None, mark_as_ads=None,
            close_comments=None, mute_notifications=None, copyright=None,
    ):
        """
        https://vk.com/dev/wall.post

        :param owner_id:
            Идентификатор пользователя или сообщества, на стене которого должна
            быть опубликована запись.


        :param friends_only:
            1 — запись будет доступна только друзьям, 0 — всем пользователям.
            По умолчанию публикуемые записи доступны всем пользователям.


        :param from_group:
            Данный параметр учитывается, если owner_id < 0 (запись публикуется
            на стене группы). 1 — запись будет опубликована от имени группы,
            0 — запись будет опубликована от имени пользователя (по умолчанию).


        :param message:
            Текст сообщения (является обязательным, если не задан параметр
            attachments)


        :param attachments:
            Список объектов, приложенных к записи и разделённых символом ",".

            Поле attachments представляется в формате:
                <type><owner_id>_<media_id>,<type><owner_id>_<media_id>

            <type> — тип медиа-приложения:
                  upload_photo — фотография;
                  video — видеозапись ;
                  audio — аудиозапись;
                  doc — документ;
                  page — wiki-страница;
                  note — заметка;
                  poll — опрос;
                  album — альбом;
                  market — товар;
                  market_album — подборка товаров;
                  audio_playlist — плейлист с аудио.

            <owner_id> — идентификатор владельца медиа-приложения (обратите
            внимание, если объект находится в сообществе, этот параметр должен
            быть отрицательным).

            <media_id> — идентификатор медиа-приложения.

            Например:
                photo100172_166443618,upload_photo-1_265827614

            Также в поле attachments может быть указана ссылка на внешнюю страницу,
            которую Вы хотите разместить в записи, например:
                photo66748_265827614,http://habrahabr.ru

            При попытке приложить больше одной ссылки будет возвращена ошибка.
            Параметр является обязательным, если не задан параметр message.


        :param services:
            Список сервисов или сайтов, на которые необходимо экспортировать
            запись, в случае если пользователь настроил соответствующую опцию.
            Например, twitter, facebook.


        :param signed:
            1 — у записи, размещенной от имени сообщества, будет добавлена
            подпись (имя пользователя, разместившего запись), 0 — подписи
            добавлено не будет. Параметр учитывается только при публикации на
            стене сообщества и указании параметра from_group. По умолчанию
            подпись не добавляется.


        :param publish_date:
            Дата публикации записи в формате unixtime. Если
            параметр указан, публикация записи будет отложена до указанного
            времени.


        :param lat:
            Географическая широта отметки, заданная в градусах (от -90 до 90).


        :param long:
            Географическая долгота отметки, заданная в градусах (от -180 до
            180).


        :param place_id:
            Идентификатор места, в котором отмечен пользователь.


        :param post_id:
            Идентификатор записи, которую необходимо опубликовать. Данный
            параметр используется для публикации отложенных записей и
            предложенных новостей.


        :param guid:
            Уникальный идентификатор, предназначенный для предотвращения
            повторной отправки одинаковой записи. Действует в течение одного
            часа.


        :param mark_as_ads:
            1 — у записи, размещенной от имени сообщества, будет добавлена
            метка "это реклама", 0 — метки добавлено не будет. В сутки может
            быть опубликовано не более пяти рекламных записей, из которых не
            более трёх — вне Биржи ВКонтакте.


        :param close_comments:
            1 — комментарии к записи отключены. 0 — комментарии к записи
            включены.


        :param mute_notifications:
            1 — уведомления к записи отключены. 0 — уведомления к записи
            включены.


        :param copyright:
            Источник материала. Поддерживаются внешние и внутренние ссылки.

        :return:
            Возвращает статус состояния

        """
        return self.vk.wall.post(
            owner_id=owner_id, friends_only=friends_only,
            from_group=from_group, message=message, attachments=attachments,
            services=services, signed=signed, publish_date=publish_date,
            lat=lat, long=long, place_id=place_id, post_id=post_id, guid=guid,
            mark_as_ads=mark_as_ads, close_comments=close_comments,
            mute_notifications=mute_notifications, copyright=copyright,
        )

    def friends_get(self, user_id=None, order=None, list_id=None, count=None,
                    offset=None, fields=None, name_case=None, ref=None):
        """
        https://vk.com/dev/friends.get

        :param user_id:
            Идентификатор пользователя, для которого необходимо получить
            список друзей. Если параметр не задан, то считается, что он равен
            идентификатору текущего пользователя (справедливо для вызова с
            передачей access_token).


        :param order:
            Порядок, в котором нужно вернуть список друзей.

            Допустимые значения:
                hints — сортировать по рейтингу, аналогично тому, как друзья
                сортируются в разделе Мои друзья (Это значение доступно только
                для Standalone-приложений с ключом доступа, полученным по схеме
                Implicit Flow.).
                random — возвращает друзей в случайном порядке.
                mobile — возвращает выше тех друзей, у которых установлены
                мобильные приложения.
                name — сортировать по имени. Данный тип сортировки работает
                медленно, так как сервер будет получать всех друзей а не только
                указанное количество count. (работает только при переданном
                параметре fields).

            По умолчанию список сортируется в порядке возрастания
            идентификаторов пользователей.


        :param list_id:
            Идентификатор списка друзей, полученный методом friends.getLists,
            друзей из которого необходимо получить. Данный параметр
            учитывается, только когда параметр user_id равен идентификатору
            текущего пользователя.

            Этот параметр доступен только для Standalone-приложений с ключом
            доступа, полученным по схеме Implicit Flow.


        :param count:
            Количество друзей, которое нужно вернуть. Положительное число, по
            умолчанию 5000


        :param offset:
            смещение, необходимое для выборки определенного подмножества
            друзей.


        :param fields:
            Список дополнительных полей, которые необходимо вернуть. Доступные
            значения: nickname, domain, sex, bdate, city, country, timezone,
            photo_50, photo_100, photo_200_orig, has_mobile, contacts,
            education, online, relation, last_seen, status,
            can_write_private_message, can_see_all_posts, can_post,
            universities


        :param name_case:
            Падеж для склонения имени и фамилии пользователя. Возможные
            значения: именительный – nom, родительный – gen, дательный – dat,
            винительный – acc, творительный – ins, предложный – abl. По
            умолчанию nom.


        :param ref:
            Строка, максимальная длина 255


        :return:
            Список друзей пользователя

        """
        return self.vk.friends.get(
            user_id=user_id, order=order, list_id=list_id, count=count,
            offset=offset, fields=fields, name_case=name_case, ref=ref)

    def photos_get(self, owner_id=None, album_id=None, photo_ids=None,
                   rev=None, extended=None, feed_type=None, feed=None,
                   photo_sizes=None, offset=None, count=None):
        return self.vk.photos.get(
            owner_id=owner_id, album_id=album_id, photo_ids=photo_ids,
            rev=rev, extended=extended, feed_type=feed_type, feed=feed,
            photo_sizes=photo_sizes, offset=offset, count=count
        )

    def groups_get(self, user_id=None, extended=None, filter=None, fields=None,
                   offset=None, count=None):
        # https://vk.com/dev/groups.get
        return self.vk.groups.get(
            user_id=user_id, extended=extended, filter=filter, fields=fields,
            offset=offset, count=count
        )

    def groups_getMembers(self, group_id=None, sort=None, offset=None,
                          count=None, fields=None, filter=None):
        # https://vk.com/dev/groups.getMembers
        return self.vk.groups.getMembers(
            group_id=group_id, sort=sort, offset=offset, count=count,
            fields=fields, filter=filter
        )

    def users_search(
            self, q: str = None, sort: bool = None, offset: int = None, count: int = None,
            fields: str = None, city: int = None, country: int = None,
            hometown: str = None, university_country: int = None,
            university: int = None, university_year: int = None,
            university_faculty: int = None, university_chair: int = None,
            sex: int = None, status: int = None, age_from: int = None, age_to: int = None,
            birth_day: int = None, birth_month: int = None, birth_year: int = None,
            online: int = None, has_photo: bool = None, school_country: int = None,
            school_class: int = None, school: int = None, school_year: int = None,
            religion: int = None, company: str = None, position: str = None,
            group_id: int = None, from_list: str = None
    ):
        # https://vk.com/dev/users.search
        return self.vk.users.search(
            q=q, sort=sort, offset=offset, count=count, fields=fields,
            city=city, country=country, hometown=hometown, sex=sex,
            university_country=university_country, university=university,
            university_year=university_year, university_chair=university_chair,
            university_faculty=university_faculty, status=status,
            age_from=age_from, age_to=age_to, birth_day=birth_day,
            birth_month=birth_month, birth_year=birth_year, online=online,
            has_photo=has_photo, school_country=school_country,
            school_class=school_class, school=school, school_year=school_year,
            religion=religion, company=company, position=position,
            group_id=group_id, from_list=from_list
        )

    def database_getCities(
            self, country_id=None, region_id=None, q=None, need_all=None,
            offset=None, count=None
    ):
        # https://vk.com/dev/database.getCities
        return self.vk.database.getCities(
            country_id=country_id, region_id=region_id, q=q, need_all=need_all,
            offset=offset, count=count
        )

    def execute(self, code=None):
        # https://vk.com/dev/execute
        return self.vk.execute(code=code)
