class Menu:

    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "Menu {menu_name} available {start_time} to {end_time}".format(
            menu_name=self.name, start_time=self.start_time, end_time=self.end_time)

    def calculate_bill(self, purchased_items):
        bill = 0
        print("Purchased Items: ")
        for item in purchased_items:
            print(item)
            bill += self.items[item]
        return "Total: " + str('${:,.2f}'.format(bill))


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return "\nFranchise address: {address}".format(address=self.address)

    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if menu.start_time <= time <= menu.end_time:
                available_menus.append(menu)
        for i in range(len(available_menus)):
            print(available_menus[i])


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


brunch_items = {'pancakes': 7.50,
                'waffles': 9.00,
                'burger': 11.00,
                'home fries': 4.50,
                'coffee': 1.50,
                'espresso': 3.00,
                'tea': 1.00,
                'mimosa': 10.50,
                'orange juice': 3.50}
brunch = Menu("Brunch", brunch_items, 1100, 1600)

earlybird_items = {'salumeria plate': 8.00,
                   'salad and breadsticks (serves 2, no refills)': 14.00,
                   'pizza with quattro formaggi': 9.00,
                   'duck ragu': 17.50,
                   'mushroom ravioli (vegan)': 13.50,
                   'coffee': 1.50,
                   'espresso': 3.00}
early_bird = Menu("Early Bird", earlybird_items, 1500, 1800)

dinner_items = {'crostini with eggplant caponata': 13.00,
                'ceaser salad': 16.00,
                'pizza with quattro formaggi': 11.00,
                'duck ragu': 19.50,
                'mushroom ravioli (vegan)': 13.50,
                'coffee': 2.00,
                'espresso': 3.00}
dinner = Menu("Dinner", dinner_items, 1700, 2300)

kids_items = {'chicken nuggets': 6.50,
              'fusilli with wild mushrooms': 12.00,
              'apple juice': 3.00}
kids = Menu("Kids", kids_items, 1100, 2100)

arepas_items = {'arepa pabellon': 7.00,
                'pernil arepa': 8.50,
                'guayanes arepa': 8.00,
                'jamon arepa': 7.50}
arepas_menu = Menu("Arepas", arepas_items, 1000, 2000)


print("Brunch " + (brunch.calculate_bill(
    ['pancakes', 'home fries', 'coffee'])))   # 13.50
print("EarlyBird " + early_bird.calculate_bill(
    ['salumeria plate', 'mushroom ravioli (vegan)']))  # 21.50


# FRANCHISING

flagship_store = Franchise("1232 West End Road", [
                           brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [
                            brunch, early_bird, dinner, kids])

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])


print(flagship_store)
flagship_store.available_menus(1700)

print(new_installment)
new_installment.available_menus(1700)


BastaFazoolin = Business("Basta Fazoolin' with my Heart",
                         (flagship_store, new_installment))
TakeaArepa = Business("Take a' Arepa", ())

print(arepas_place.address)
arepas_place.available_menus(1700)
