# Superclass Data object for ship classes
class Ship(object):
    def __init__(self):
        self.header = ""
        self.armaments = ""
        self.defenses = ""
        self.decks = ""
        self.crew = ""
        self.cruise_speed = ""
        self.max_cruise_speed = ""
        self.maximum_speed = ""
        self.img_url = ""
        self.description = ""

class ShipClass(Ship):
    def __init__(self):
        super(ShipClass, self).__init__()
        # Sovereign class data
        self.header = "Sovereign Class"
        self.armaments = "Type XII Phasers<br>Photon Torpedoes<br>Quantum Torpedoes"
        self.defenses = "High Capacity Shields"
        self.decks = "24"
        self.crew = "130 officers<br>725 enlisted"
        self.cruise_speed = "Warp 6"
        self.max_cruise_speed = "Warp 9.7"
        self.maximum_speed = "Warp 9.9 (12hrs)"
        self.img_url = "sovereign-class.jpg"
        self.description = "The Sovereign class is Starfleet's newest and most technologically advance class of starship. When first conceived the Sovereign class was intended to carry out the same mission profile as the Ambassador and the Galaxy classes, with introduction coming late in the Galaxy class's life cycle. As new threats immerged in the mid-24th century, such as the return of the Romulan Empire and the Borg, the Sovereign class design was update to incorporate elements of a battleship, and lessening of the diplomatic and exploration roles. After the first Borg invasion the Sovereign class was rushed into service far earlier then planned. This allowed the class to play a pivotal role in the Dominion War and Reman incident."
