class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue  # Sulfuras não muda

            self.update_sell_in(item)
            self.update_item_quality(item)

    def update_sell_in(self, item):
        item.sell_in -= 1

    def update_item_quality(self, item):
        if item.name == "Aged Brie":
            self.update_aged_brie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_pass(item)
        elif item.name.startswith("Conjured"):
            self.update_conjured_item(item)
        else:
            self.update_normal_item(item)

    def update_aged_brie(self, item):
        self.increase_quality(item)
        if item.sell_in < 0:
            self.increase_quality(item)

    def update_backstage_pass(self, item):
        if item.sell_in < 0:
            item.quality = 0
            return

        self.increase_quality(item)
        if item.sell_in < 10:
            self.increase_quality(item)
        if item.sell_in < 5:
            self.increase_quality(item)

    def update_conjured_item(self, item):
        self.decrease_quality(item)
        self.decrease_quality(item)
        if item.sell_in < 0:
            self.decrease_quality(item)
            self.decrease_quality(item)

    def update_normal_item(self, item):
        self.decrease_quality(item)
        if item.sell_in < 0:
            self.decrease_quality(item)

    def increase_quality(self, item):
        if item.quality < 50:
            item.quality += 1

    def decrease_quality(self, item):
        if item.quality > 0:
            item.quality -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    


items = [
    Item(name="Aged Brie", sell_in=10, quality=25),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
    Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
    Item(name="Conjured Mana Cake", sell_in=3, quality=6),
    Item(name="Normal Item", sell_in=5, quality=7)
]

gilded_rose = GildedRose(items)
gilded_rose.update_quality()

for item in items:
    print(item)