import time
from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __hash__(self):  # Шифровка пароля
        return self.password


class Video:  # создает объекты видео
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:  # хранит: список пользователей, список видеофайлов, параметры текущего пользователя
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __str__(self):
        return f'{self.current_user}'



    def add(self, *args):  # проверяет наличие добавляемого файла video в список videos, если нет, добавляет
        video = []
        for i in args:  # перебирает переданные видеофайлы
            video = [i.title, i.duration, i.adult_mode]  # создает список из переданных параметров для видеофайла
            if not self.videos: # если в списке видео нет видеофайлов
                self.videos.append(video)  # видеофайл добавляется в список видео
            else:  # иначе, если видеофайлы в списке есть:
                for j in self.videos:  # перебирает видеофайлы в списке videos
                    if i.title != j[0]:  # если назван. переданного в.файла не совпадает с назв-ми в.файлов в списке
                        self.videos.append(video)
                    else:  # иначе если совпадает
                        break

    def get_videos(self, search_video):  # поиск в.файла в списке videos по строке
        self.search_video = search_video.lower()  # перевод в нижний регистр
        self.my_search_list = []  # создает пустой список
        for i in self.videos:  # перебирает в.файлы в списке
            my_str = i[0]  # присваивает переменной значение первого параметра в.файла (title)
            self.my_str = my_str.lower()  # перевод в нижний регистр
            if self.search_video in self.my_str:  # если строка есть в названии в.файла
                self.my_search_list.append(my_str)  # добавляем название файла в пустой список
        return self.my_search_list  # возвращаем список

    def watch_video(self, get_video):  # воспроизводит видео по названию
        self.get_video = get_video
        if self.current_user != None:  # проверяет авторизацию пользователя
            for i in self.videos:  # перебирает в.файлы в списке
                if i[0] == self.get_video and i[2] == True:  # если название совпдает с параметром и есть запрос age
                    self.current_duration = i[1]  # текущая длительность принимается из параметров в.файла
                    self.current_time_now = 0

                    if self.age > 18:                                # если возраст больше 18
                        for j in range(1, self.current_duration+1):  # перебирает длительность текущего видео
                            self.current_time_now = j                # если текущее время меньше длительности
                            print(end=' ')
                            print(self.current_time_now, sep=' ', end=' ')
                            time.sleep(0)                            # воспроизводит видео с паузой 1 сек
                        print(' Конец видео')
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        self.log_out()     # выход из аккаунта
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')



    def register(self, nickname, password, age):
        self.password = hash(password)
        self.age = age
        self.nickname = nickname
        self.user = [self.nickname, self.password, self.age]
        self.id_user = 0
        for user in self.users:
            if user[0] == self.nickname:
                self.log_in(self.nickname, self.password)
        if self.id_user == 0:
            self.users.append(self.user)
            self.log_in(self.nickname, self.password)
        elif self.id_user == 1:
            print(f'Пользователь {self.nickname} авторизован')
        elif self.id_user == 2:
            print(f'Пользователь {self.nickname} уже существует')



    def log_in(self, nickname, password):
        self.nickname = nickname
        self.password = password
        for user in self.users:
            if user[0] == self.nickname and user[1] == self.password:
                self.current_user = self.users[0]
                self.id_user = 1
            elif user[0] == self.nickname and user[1] != self.password:
                self.id_user = 2
        return self.id_user

    def log_out(self):
        self.current_user = None
        self.age = 0
        self.nickname = ""
        self.password = hash("")
        return



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)
'''
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
'''
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 1)
ur.watch_video('Для чего девушкам парень программист?')
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')


print(ur.current_user)





