import turtle

toto = turtle.Screen()
toto.bgcolor("black")
# toto = le screen (donc toto.bgcolor("black") c'est la couleur du bg)
titi = turtle.Turtle()
titi.color("red")
# titi = le pointer (donc toto.color("red") c'est la couleur du tracé)
for i in range(3):
    titi.right(90)
    titi.circle(42)
# Boucle pour faire trois cercles
# titi.right = incline de 90deg vers la droite au debut de boucle
# titi.circle = trace cercle de rayon de 42 deg
toto.exitonclick()
# exit au click
