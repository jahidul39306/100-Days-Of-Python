from turtle import Turtle, Screen
from prettytable import PrettyTable

timmy = Turtle()
timmy.color("red", "green")
timmy.shape("turtle")

x = 30
while True:
    x = int(x) + 10
    timmy.forward(100)
    timmy.left(x)

my_screen = Screen()
my_screen.exitonclick()
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)
