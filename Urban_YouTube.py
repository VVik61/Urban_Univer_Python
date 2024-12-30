import hashlib


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def __str__(self):
        return (f'Пользователь: {self.nickname}\nС паролем '
                f'{self.password}\nЛет: {self.age}')

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, stored_password, provided_password):
        return stored_password == hashlib.sha256(
            provided_password.encode()).hexdigest()

    #  nickname(имя пользователя, строка),
    #  password(в хэшированном виде, число),
    # age(возраст, число)
# def __hash__(self): return hash((self.age, self.name))
# Источник: https://pythonim.ru/osnovy/funktsiya-hash-v-python

"""
title(заголовок, строка),
duration(продолжительность, секунды),
time_now(секунда остановки (изначально 0)),
adult_mode(ограничение по возрасту, bool (False по умолчанию))
"""

# +++++++++++++++++++
# +++++++++++++++++++
class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

        # if (isinstance(title, str) and
        #         isinstance(time_now, str) and
        #         isinstance(duration, int)):
        #     self.title = title
        #     self.duration = duration
        #     self.time_now = time_now
        #     self.adult_mode = adult_mode
        # else:
        #     print('Ошибка в атрибутах. Проверьте и введите их правильно!')
        #     exit()

# +++++++++++++++++++
# +++++++++++++++++++
class UrTube():
    def __init__(self):
        self.users = []   # [User1, User2    ..  UserN] объекты класса User
        self.videos = []  # [Video1, Video2  .. VideoN] объекты класса Video
        self.current_user = None # указывает на объект класса User из users

    def log_in(self, nickname, password):
        # hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user_entrance = User(nickname, password, 64)
        if user_entrance in self.users:
            print('ЕСТЬ!')
        else:
            print('НЕТ!')
            #
            #     (                (nickname, password) in users):
            # current_user = users[000]

# Атрибуты: users(список объектов User),
# videos(список объектов Video),
# current_user(текущий пользователь, User)

# Метод log_in, который принимает на вход аргументы: nickname, password
# и пытается найти пользователя в users с такими же логином и паролем.
# Если такой пользователь существует, то current_user меняется на найденного.
# Помните, что password передаётся в виде строки, а сравнивается по хэшу.
# +++++++++++++++++++
    def isexists(self, nickname, password):
        """
        проверка на то, есть ли пользователь с такими nickname, password
        в users = []
        """
        for nikn in self.users:
            if nikn == nickname:
                print('Есть!  Но надо проверить пароль!')

    def reister(self, nickname, password, age):
        pass
# Метод register, который принимает три аргумента: nickname, password, age,
# и добавляет пользователя в список,
# если пользователя не существует (с таким же nickname).
# Если существует, выводит на экран: "Пользователь {nickname} уже существует".
# После регистрации, вход выполняется автоматически.

    def log_out(self):
        """сброс текущего пользователя на None."""
        self.current_user = None

    def add(self, *videos):
        for video in videos.count():
            print(video)
            # if not video in self.videos:
            #     self.videos.__add__(video)
            # # if video == self.videos:
            #     pass
# Метод add, который принимает неограниченное кол-во объектов класса Video
# и все добавляет в videos, если с таким же названием видео ещё не существует.
# В противном случае ничего не происходит.

# Метод get_videos, который принимает поисковое слово и возвращает список
# названий всех видео, содержащих поисковое слово. Следует учесть,
# что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).

# Метод watch_video, который принимает название фильма,
# если не находит точного совпадения(вплоть до пробела),
# то ничего не воспроизводится, если же находит - ведётся отчёт
# в консоль на какой секунде ведётся просмотр.
# После текущее время просмотра данного видео сбрасывается.


# u1 = User('Витя', '123', 63)
# print(u1.__str__())


#
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
#
ur.log_in('Витя', 123)

#
# # Добавление видео
# ur.add(v1, v2)
#
# # Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')
#
#
#
# # Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')