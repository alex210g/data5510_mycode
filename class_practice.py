class NBA_Player():
    def __init__(self, name, number, team, height, points):
        self.name = name 
        self.number = number #attribute
        self.team = team
        self.height = height 
        self.points = points 

    def __str__(self): 
        return self.name + "is an NBA player, who has a height of:" + self.height + "and he plays for the" + self.team + "and wears the number" + str(self.number) + "and has scored the following points in his last 4 games: " + str(self.points)

    def calc_avg_points(self): 
        return np.mean(self.points)

keyonte_player = NBA_Player("Keyonte", 3, "Jazz", "6'3", [23,25, 43, 10])
lebron_player = NBA_Player("Lebron", 23, "Sixers", "6'8", [30,29,27,22])

print(keyonte_player)
print(keyonte_player.calc_avg_points)

print(lebron_player)
print(lebron_player.calc_avg_points)
