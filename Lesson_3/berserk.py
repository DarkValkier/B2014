from Lesson_2.character import Character
from colorama import Fore, Style


class Berserk(Character):
    def __init__(self, name='', health=100, damage=1, defence=0, color=Fore.LIGHTWHITE_EX):
        Character.__init__(self, name, health, damage, defence, color)
        self.max_health = health

    def get_additional_damage(self):
        return int(self.damage * (1 - self.health / self.max_health))

    def attack(self, target):
        target.take_damage(self.damage + self.get_additional_damage())

    def get_stats(self):
        return \
            f'{self.color}' \
            f'Имя: {self.name}\n' \
            f'Здоровье: {self.health}\n' \
            f'Урон: {self.damage} (+{self.get_additional_damage()})\n' \
            f'Защита {self.defence}\n'\
            f'{Style.RESET_ALL}'