from ast import For
from dataclasses import dataclass
from datetime import date
from decimal import DecimalTuple
from operator import indexOf
from sqlite3 import Date
from tkinter.messagebox import NO
from typing import List, Union
from unicodedata import name
# method
# attributes


class Fish:

    def __init__(self, name: str, price_in_uah_per_kilo: float, catch_date: date, origin: str, body_only: bool, weight: float) -> None:
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.catch_date = catch_date
        self.origin = origin
        self.body_only = body_only
        self.weight = weight


class FishShop:
    def __init__(self) -> None:
        self.fish_storage = []

    def add_fish(self, fish: Fish) -> None:
        self.fish_storage.append(fish)
        print(fish.name+" was added!")

    def get_fish_names_sorted_by_price(self) -> None:
        self.fish_storage.sort(
            key=lambda key_for_sort: key_for_sort.price_in_uah_per_kilo, reverse=True)
        print("Name", "price", sep="\t")
        for fish_iterator in self.fish_storage:
            print(fish_iterator.name+"\t" +
                  str(fish_iterator.price_in_uah_per_kilo)+" ₴")

    def sell_fish(self, fish: Fish) -> None:
        index = self.fish_storage.index(fish)
        del(self.fish_storage[index])
        print(fish.name+" was sold!")

    def cast_out_old_fish(self) -> None:
        for fish_iterator in self.fish_storage:
            difference_between_catch_dates = abs(
                fish_iterator.catch_date - date.today())
            if difference_between_catch_dates.days > 150:
                self.fish_storage.remove(fish_iterator)
                print(fish_iterator.name+" was cast out!")


class Seller:
    pass


class Buyer:
    def __init__(self, money) -> None:
        pass

    def Buy_fish(self, fish: Fish, fish_shop: FishShop) -> None:
        pass


fish = Fish(name="Salmon", price_in_uah_per_kilo=125.5,
            catch_date=date(2022, 1, 12), origin="Norway", body_only=False, weight=1.2)

fish2 = Fish(name="Hake", price_in_uah_per_kilo=300.25,
             catch_date=date(2022, 1, 26), origin="Spain", body_only=False, weight=1.5)

fish3 = Fish(name="Tuna", price_in_uah_per_kilo=500.4,
             catch_date=date(2022, 1, 20), origin="Canada", body_only=False, weight=2)

fish4 = Fish(name="Trout", price_in_uah_per_kilo=780.50,
             catch_date=date(2022, 1, 26), origin="USA", body_only=False, weight=2.5)

fish5 = Fish(name="Carp", price_in_uah_per_kilo=576.6,
             catch_date=date(2019, 10, 24), origin="Ukraine", body_only=False, weight=1.7)


fish_shop = FishShop()

fish_shop.add_fish(fish)
fish_shop.add_fish(fish2)
fish_shop.add_fish(fish3)
fish_shop.add_fish(fish4)
fish_shop.add_fish(fish5)
fish_shop.sell_fish(fish4)
fish_shop.cast_out_old_fish()
fish_shop.get_fish_names_sorted_by_price()
