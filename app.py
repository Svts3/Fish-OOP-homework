from ctypes import Union
from datetime import date
from urllib.parse import MAX_CACHE_SIZE
from multimethod import multimethod


class FishInfo:
    def __init__(self, name: str,
                 price_in_uah_per_kilo: float, origin: str,
                 catch_date: date, due_time: date, is_alive: bool) -> None:

        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.origin = origin
        self.catch_date = catch_date
        self.due_time = due_time
        self.is_alive = is_alive


class Fish(FishInfo):
    def __init__(self, name: str, price_in_uah_per_kilo: float,
                 origin: str, catch_date: date,
                 due_time: date, age_in_month: int, weight: float, is_alive: bool) -> None:
        super().__init__(name, price_in_uah_per_kilo,
                         origin, catch_date, due_time, is_alive)
        self.age_in_month = age_in_month
        self.weight = weight


class FishBox:
    def __init__(self, fish_info: FishInfo, weight: float,
                 package_date: date, height: float,
                 width: float, length: float,
                 is_alive: bool) -> None:
        self.fish_info = fish_info
        self.weight = weight
        self.package_date = package_date
        self.height = height
        self.width = width
        self.length = length
        self.is_alive = is_alive


class FishShop:
    def __init__(self, frozen_fish_boxes: dict[str:list[FishBox]],
                 fresh_fish_boxes: dict[str:list[FishBox]]) -> None:
        self.frozen_fish_boxes = frozen_fish_boxes
        self.fresh_fish_boxes = fresh_fish_boxes

    @multimethod
    def add_fish(self, fish_box: FishBox) -> None:
        if fish_box.fish_info.is_alive:
            self.fresh_fish_boxes[fish_box.fish_info.name] = [
                fish_box.fish_info.price_in_uah_per_kilo, fish_box.weight]
        elif fish_box.fish_info.is_alive == False:
            self.frozen_fish_boxes[fish_box.fish_info.name] = [
                fish_box.fish_info.price_in_uah_per_kilo, fish_box.weight]

    @multimethod
    def add_fish(self, fish: Fish, weight: float) -> None:
        if fish.is_alive:
            self.fresh_fish_boxes[fish.name] = [
                fish.price_in_uah_per_kilo, weight]
        if fish.is_alive == False:
            self.frozen_fish_boxes[fish.name] = [
                fish.price_in_uah_per_kilo, weight]

    def sell_fish(self, name: str, weight: float, is_fresh: bool)->None:

        if is_fresh and name in self.fresh_fish_boxes:
            self.fresh_fish_boxes[name][1] -= weight
            if self.fresh_fish_boxes[name][1] <= 0.0:
                self.fresh_fish_boxes.pop(name)
                return [name, weight]

        if is_fresh == False and name in self.frozen_fish_boxes:
            if self.frozen_fish_boxes[name][1] <= 0.0:
                self.frozen_fish_boxes.pop(name)
            self.frozen_fish_boxes[name][1] -= weight
            return [name, weight]

    def get_fish_sorted_by_price(self) -> None:
        sorted_fish_box = {}
        sorted_fish_box.update(self.frozen_fish_boxes)
        sorted_fish_box.update(self.fresh_fish_boxes)
        sorted_fish_box = sorted(sorted_fish_box.items(
        ), key=lambda key_for_sort: key_for_sort[1], reverse=False)
        print(sorted_fish_box)

    def get_fresh_fish_sorted_by_price(self) -> set[str, float]:
        sorted_fresh_fish_box = sorted(
            self.fresh_fish_boxes.items(), key=lambda key_for_sort: key_for_sort[1], reverse=False)
        print(sorted_fresh_fish_box)

    def get_frozen_fish_sorted_by_price(self) -> None:
        sorted_frozen_fish_box = sorted(
            self.frozen_fish_boxes.items(), key=lambda key_for_sort: key_for_sort[1], reverse=False)
        print(sorted_frozen_fish_box)


frozen_fish_boxes = {}
fresh_fish_boxes = {}
fish_shop = FishShop(frozen_fish_boxes, fresh_fish_boxes)
fish1 = Fish("Salmon", 100.25, "Norway", date.today(),
             date(2022, 3, 30), 0, 2.5, True)
fish2 = Fish("Pike", 85.25, "Norway", date.today(),
             date(2022, 3, 30), 0, 3.6, True)
fish3 = Fish("Shark", 1000, "Norway", date.today(),
             date(2022, 3, 30), 0, 10.5, False)
fish4 = Fish("Snook", 1200, "Norway", date.today(),
             date(2022, 2, 12), 0, 4.4, True)
fish5 = Fish("Carp", 200.50, "UA", date.today(),
             date(2022, 2, 12), 0, 4.4, False)
fish6 = Fish("Clownfish", 2300.50, "USA", date.today(),
             date(2022, 2, 12), 0, 0.5, False)

fish_box = FishBox(FishInfo("Fugu", 120.55, "UA", date(
    2021, 12, 5), date.today(), True), 30, date(2021, 12, 20), 20, 20, 20, True)


fish_shop.add_fish(fish1, 2.5)
fish_shop.add_fish(fish2, 3.6)
fish_shop.add_fish(fish3, 10.5)
fish_shop.add_fish(fish_box)
fish_shop.add_fish(fish4, 4.4)
fish_shop.add_fish(fish5, 4.4)
fish_shop.add_fish(fish6, 0.5)
print("\nFresh fish box: \n")
print(fish_shop.fresh_fish_boxes)
print("\nFrozen fish box: \n")
print(fish_shop.frozen_fish_boxes)

fish_shop.sell_fish("Salmon", 2.5, True)
print("Fresh fish box: \n")
print(fish_shop.fresh_fish_boxes)
print("Frozen fish box: \n")
print(fish_shop.frozen_fish_boxes)

print("\nFresh fish sorted by price: \n")
fish_shop.get_fresh_fish_sorted_by_price()
print("\nFrozen fish sorted by price: \n")
fish_shop.get_frozen_fish_sorted_by_price()
print("\nAll fish sorted by price: \n")
fish_shop.get_fish_sorted_by_price()
