import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FONT = ("Courier", 24, "bold")
SMALL_FONT = ("Courier", 14, "normal")

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Car Crossing by PRAYANSHU")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_started = False
game_paused = False

# --- Start message (click anywhere to begin) ---
start_text = Turtle()
start_text.hideturtle()
start_text.penup()
start_text.color("black")
start_text.goto(0, 0)
start_text.write("Click anywhere to start", align="center", font=FONT)

# --- Pause button (top-right corner) ---
pause_button = Turtle()
pause_button.hideturtle()
pause_button.penup()
pause_button.color("black")
pause_button.goto(180, 260)
pause_button.write("Pause (P)", align="left", font=SMALL_FONT)


def start_game(x, y):
    global game_started
    if not game_started:
        game_started = True
        start_text.clear()


def toggle_pause():
    global game_paused
    if game_started:
        game_paused = not game_paused
        pause_button.clear()
        pause_button.goto(180, 260)
        label = "Resume (P)" if game_paused else "Pause (P)"
        pause_button.write(label, align="left", font=SMALL_FONT)


screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(toggle_pause, "p")
screen.onclick(start_game)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if not game_started or game_paused:
        continue

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()