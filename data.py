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
        self.img_description = ""
        self.description = ""

# Subclass Data object for ship classes
class ShipClass(Ship):
    def __init__(self):
        super(ShipClass, self).__init__()
        # Sovereign class data
        sovereign = Ship()
        sovereign.header = "Sovereign Class"
        sovereign.armaments = "Type XII Phasers<br>Photon Torpedoes<br>Quantum Torpedoes"
        sovereign.defenses = "High Capacity Shields"
        sovereign.decks = "24"
        sovereign.crew = "130 officers<br>725 enlisted"
        sovereign.cruise_speed = "Warp 6"
        sovereign.max_cruise_speed = "Warp 9.7"
        sovereign.maximum_speed = "Warp 9.9 (12hrs)"
        sovereign.img_url = "sovereign-class.jpg"
        sovereign.img_description = "Sovereign Class Starship"
        sovereign.description = "The Sovereign class is Starfleet's newest and most technologically advance class of starship. When first conceived the Sovereign class was intended to carry out the same mission profile as the Ambassador and the Galaxy classes, with introduction coming late in the Galaxy class's life cycle. As new threats immerged in the mid-24th century, such as the return of the Romulan Empire and the Borg, the Sovereign class design was update to incorporate elements of a battleship, and lessening of the diplomatic and exploration roles. After the first Borg invasion the Sovereign class was rushed into service far earlier then planned. This allowed the class to play a pivotal role in the Dominion War and Reman incident."
        # Galaxy class data
        galaxy = Ship()
        galaxy.header = "Galaxy Class"
        galaxy.armaments = "Type X Phasers<br>Photon Torpedoes"
        galaxy.defenses = "High Capacity Shields"
        galaxy.decks = "42"
        galaxy.crew = "1014 officers and enlisted"
        galaxy.cruise_speed = "Warp 6"
        galaxy.max_cruise_speed = "Warp 9.2"
        galaxy.maximum_speed = "Warp 9.6 -9.9 (12hrs)"
        galaxy.img_url = "galaxy-class.jpg"
        galaxy.img_description = "Galaxy Class Starship"
        galaxy.description = "The Galaxy class is Starfleet's current flagship class. The Galaxy was designed to be a multi-purpose mission platform, intended to replace all older classes. The Galaxy class possesses the most advance general purpose scientific and exploration recourses of any Federation starship class; this makes the Galaxy ideal for long term exploration missions independent of Starfleet resources. The Galaxy class was also equipped with state of the art weapon and defensive systems when it was launched in the mid 24th century, along with saucer separation capability, which allowed the star drive section to serve as a mobile weapons platform when relieved of the bulk of its mass. Before the advent of the Federation battleships due to the Borg and Dominion threats, the Galaxy class was the choice class for defending the Federation borders and showing the flag as a deterrent for any hostile moves from neighboring species. Finally, the Galaxy class was also designed for diplomatic, evacuation, and first contact missions, fulfilling its role as the most capable Federation ship."
        # Excelsior class data
        excelsior = Ship()
        excelsior.header = "Excelsior Class"
        excelsior.armaments = "Type VIII-IX Phasers<br>Photon Torpedoes"
        excelsior.defenses = "Shields"
        excelsior.decks = "20"
        excelsior.crew = "750 officers and enlisted"
        excelsior.cruise_speed = "Warp 6"
        excelsior.max_cruise_speed = "Warp 8.2-9"
        excelsior.maximum_speed = "Warp 8.6-9.4 (12hrs)"
        excelsior.img_url = "excelsior-class.jpg"
        excelsior.img_description = "Excelsior Class Starship"
        excelsior.description = "The Excelsior class was originally designed as a test bed for Starfleet's first experimental transwarp drive. Having been sabotaged in the engines' first transwarp test and having failed in all subsequent attempts, the Excelsior prototype was refitted with a conventional warp drive. As full production started on the Excelsior class, the ship became the mainstay of the fleet in the late 23rd and early 24th centuries, replacing the older Constitution class as the flagship class. The Excelsior class remains in service today, more then 60 years after if was first launched, through a program of continuous enhancements to the ships systems, being the personal flagship of choice for many admirals. The Excelsior class has two major refit variants, the Enterprise-B type and the Lakota type. The Enterprise-B type, commissioned in the late 23rd century, has upgraded sensor and science systems. The Lakota type, commissioned in 2372 right before the outbreak of the Dominion war, brought the weapon and defensive systems up to standard with the Defiant and Sovereign classes."
        # Constitution class data
        constitution = Ship()
        constitution.header = "Constitution Class"
        constitution.armaments = "Type VI Phasers<br>Photon Torpedoes"
        constitution.defenses = "Shields"
        constitution.decks = "23"
        constitution.crew = "430 officers and enlisted"
        constitution.cruise_speed = "Warp 6"
        constitution.max_cruise_speed = "Warp 8.2-9"
        constitution.maximum_speed = "Warp 8.6-9.4 (12hrs)"
        constitution.img_url = "constitution-class.jpg"
        constitution.img_description = "Constitution Class Starship"
        constitution.description = "The Constitution class is Starfleet's most famous line of ships, they were the most advance class of ships ever built when they were commissioned with unparalleled speed, weaponry, defenses, scientific and diplomatic resources. The Constitution class ships were responsible for nearly all of the Federation's rapid expansion during the mid-23rd century, along with its defense and exploration. Several times the Constitution class and their crews were call on to decide the future of the Federation against the Klingons, Romulans, and other hostile species, each time proving themselves the best in the galaxy."
        # Intrepid class data
        intrepid = Ship()
        intrepid.header = "Intrepid Class"
        intrepid.armaments = "Type X Phasers<br>Photon Torpedoes<br>Tri-Colbat Devices"
        intrepid.defenses = "High Capacity Shields"
        intrepid.decks = "15"
        intrepid.crew = "40 officers<br>230 enlisted"
        intrepid.cruise_speed = "Warp 6"
        intrepid.max_cruise_speed = "Warp 8.2-9"
        intrepid.maximum_speed = "Warp 8.6-9.4 (12hrs)"
        intrepid.img_url = "intrepid-class.jpg"
        intrepid.img_description = "Intrepid Class Starship"
        intrepid.description = "The Intrepid class was designed to fulfill the roles of an exploration and science vessel along with a light combat capability; it is also one of the fastest and most agile ships in the fleet. As with many other recent ships classes, experience with loss of several of the initial multi-purpose Galaxy class ships alerted Starfleet that smaller ships with a more specific mission may be a better overall fleet strategy; thus the Intrepid class was designed to take on some of the Galaxy's exploration and science missions. Unlike the Galaxy class ships, the Intrepid is not heavily armed but is equipped well enough to defend itself; this combined with its speed and maneuverability makes it ideal for border patrol against lightly armed forces such as raiders and the Marquis, in locations that a massive Galaxy class would not be able to operate."
