'''
Придумать класс самостоятельно, реализовать в нем методы экземпляра
класса, статические, методы, методы класса.
'''


class Music:
    genre = "Рок"

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    @classmethod
    def class_method(self):
        print(f"жанр музыки: {self.genre}")

    def play(self):
        print(f"Играет {self.title} исполнителя {self.artist}")

    @staticmethod
    def static_method():
        print("...слушаем музыку...")


song = Music(title="Zombie", artist="The Cranberries")

Music.class_method()
song.play()
Music.static_method()
