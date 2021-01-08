import datetime

class RealMadrid:
    """A player for the greatest club in the world. Hala Madrid Y Nada Mas"""
    def start(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday 
        
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """Return the age of the player"""
        today = datetime.date(2021, 8, 1)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today - dob).days
        age_in_years = age_in_days/365
        return int(age_in_years)


player1 = RealMadrid("Karim Benzema", "19901004")
print(player1.name)
print(player1.first_name)
print(player1.last_name)
print(player1.birthday)

# player1 = RealMadrid()
# player1.first_name = "Sergio"
# player1.last_name = "Ramos"

# print(player1.first_name)
# print(player1.last_name)

# player2 = RealMadrid()
# player2.first_name = "Fede"
# player2.last_name = "Valverde"

# print(player2.first_name, player2.last_name)

# player1.age = 35
# player2.position = "Midfielder"

# print(player1.age)
# print(player2.position)

