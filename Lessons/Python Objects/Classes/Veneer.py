class Art:

    def __init__(self, artist, title, year, medium, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return "{artist}. {title}. {year}, {medium}. {owner}, {location}.\n".format(artist=self.artist, title=self.title, year=self.year, medium=self.medium, owner=self.owner.name, location=self.owner.location)


class MarketPlace:

    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, old_listing):
        self.listings.remove(old_listing)

    def show_listings(self):
        for listing in self.listings:
            print(listing)


class Client:

    def __init__(self, name, location, is_museum):
        self.name = name
        self.is_museum = is_museum
        if is_museum:
            self.location = location
        else:
            self.location = "Private Collection"

    def list_artwork(self, artwork, price):
        if artwork.owner == self:
            new_listing = Listing(artwork, price, self)
            veneer.add_listing(new_listing)
        else:
            print("Waring: That's not your's to sell.")

    def buy_artwork(self, artwork):
        if artwork.owner != self:
            art_listing = None
            for listing in veneer.listings:
                if listing.artwork == artwork:
                    art_listing = listing
                    break
            if art_listing != None:
                art_listing.artwork.owner = self
                veneer.remove_listing(art_listing)


class Listing:

    def __init__(self, artwork, price, seller):
        self.artwork = artwork
        self.price = price
        self.seller = seller

    def __repr__(self):
        return "Title: {title}. {price}".format(title=self.artwork.title, price=self.price)


veneer = MarketPlace()

edytta = Client("Edytta Halpirt", None, False)
girl_with_mandolin = Art("Picasso, Pablo",
                         "Girl with a Mandolin (Fanny Tellier)",
                         1910,
                         "Oil on Canvas",
                         edytta)
# print(girl_with_mandolin)

moma = Client("MOMA", "New York", True)
vetheuil_in_fog = Art("Monet, Claude",
                      "Vétheuil in the Fog",
                      1879,
                      "Oil on Canvas",
                      moma)
# print(vetheuil_in_fog)

# moma.list_artwork(vetheuil_in_fog, None)
edytta.list_artwork(girl_with_mandolin, "$6M (USD)")
# edytta.list_artwork(vetheuil_in_fog, None)
veneer.show_listings()
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
veneer.show_listings()


## Here are some more things you could try:

# Add a wallet instance variable to clients, update the buying and selling of artworks to also exchange dollar amounts.
# Create a wishlist for your clients, things that are listed but they’re not sure if they should purchase just yet.
# Create expiration dates for listings! Have out of date listings automatically removed from the marketplace.