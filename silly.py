# Pong Deluxe: Crazy Powerups Edition (Corrected for paddle collision bug)
# Requires Python 3.x and turtle (standard), winsound (Windows only, optional for sound)
import turtle
import random
import time
import math

# --- Setup Screen ---
wn = turtle.Screen()
wn.title("Pong Deluxe with Crazy Powerups!")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# --- Utility Functions ---
def play_sound(filename):
    try:
        import winsound
        winsound.PlaySound(filename, winsound.SND_ASYNC)
    except ImportError:
        pass

def clamp(val, minv, maxv):
    return max(minv, min(maxv, val))

def rgb(r,g,b):
    return "#%02x%02x%02x" % (int(r), int(g), int(b))

# --- Particle System ---
class Particle:
    def __init__(self, x, y, color):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        self.t.up()
        self.t.goto(x, y)
        self.t.shape("circle")
        self.t.shapesize(stretch_wid=0.2, stretch_len=0.2)
        self.t.color(color)
        self.t.showturtle()
        self.dx = random.uniform(-4,4)
        self.dy = random.uniform(-4,4)
        self.life = random.randint(8,18)
        self.gravity = random.uniform(0.05, 0.2)
        self.fade = random.randint(0,1)
    def update(self):
        self.t.setx(self.t.xcor() + self.dx)
        self.t.sety(self.t.ycor() + self.dy)
        self.dy -= self.gravity
        self.life -= 1
        if self.fade:
            self.t.shapesize(stretch_wid=0.2 * self.life/14, stretch_len=0.2 * self.life/14)
        if self.life <= 0:
            self.t.hideturtle()
            return False
        return True

# --- Paddle Class ---
class Paddle:
    def __init__(self, x, upk, downk, screen):
        self.t = turtle.Turtle()
        self.t.shape("square")
        self.t.shapesize(stretch_wid=5, stretch_len=1.5)
        self.t.color("white")
        self.t.penup()
        self.t.goto(x, 0)
        self.base_stretch = 5
        self.length = 1.5
        self.upk = upk
        self.downk = downk
        self.dy = 0
        self.max_speed = 18
        self.powerup = None
        self.powerup_timer = 0
        self.shield = False
        self.reverse = False
        self.freeze = False
        self.input_state = {"up": False, "down": False}
        self.screen = screen
    def move(self):
        if self.freeze:
            self.dy = 0
        else:
            if self.input_state["up"]:
                self.dy = self.max_speed if not self.reverse else -self.max_speed
            elif self.input_state["down"]:
                self.dy = -self.max_speed if not self.reverse else self.max_speed
            else:
                self.dy *= 0.8
        newy = clamp(self.t.ycor() + self.dy, -250, 250)
        self.t.sety(newy)
        if self.powerup_timer > 0:
            self.powerup_timer -= 1
            if self.powerup_timer == 0 and self.powerup:
                # End powerup effect
                if self.powerup == "grow":
                    self.t.shapesize(stretch_wid=self.base_stretch, stretch_len=self.length)
                elif self.powerup == "shrink":
                    self.t.shapesize(stretch_wid=self.base_stretch, stretch_len=self.length)
                elif self.powerup == "reverse":
                    self.reverse = False
                elif self.powerup == "freeze":
                    self.freeze = False
                elif self.powerup == "shield":
                    self.shield = False
                self.powerup = None

# --- Ball Class ---
class Ball:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape("circle")
        self.t.color("white")
        self.t.shapesize(stretch_wid=1.1, stretch_len=1.1)
        self.t.penup()
        self.t.goto(0,0)
        self.base_speed = 2.5
        self.max_speed = 7.5
        self.dx = random.choice([-self.base_speed, self.base_speed])
        self.dy = random.choice([-self.base_speed, self.base_speed])
        self.spin = 0
        self.spin_decay = 0.97
        self.powerup = None
        self.powerup_timer = 0
        self.ghost = False
        self.big = False
        self.small = False
        self.curve = False
        self.random = False
        self.split = False
    def update(self, paddles, particles):
        # Ball movement
        self.t.setx(self.t.xcor() + self.dx + self.spin)
        self.t.sety(self.t.ycor() + self.dy)
        self.spin *= self.spin_decay
        # Curve
        if self.curve:
            self.dy += random.uniform(-0.12,0.12)
        # Random erratic
        if self.random:
            self.dx += random.uniform(-0.6,0.6)
            self.dy += random.uniform(-0.6,0.6)
            self.dx = clamp(self.dx, -self.max_speed, self.max_speed)
            self.dy = clamp(self.dy, -self.max_speed, self.max_speed)
        # Powerup timer
        if self.powerup_timer > 0:
            self.powerup_timer -= 1
            if self.powerup_timer == 0 and self.powerup:
                # End effects
                if self.powerup == "big":
                    self.t.shapesize(stretch_wid=1.1, stretch_len=1.1)
                    self.big = False
                elif self.powerup == "small":
                    self.t.shapesize(stretch_wid=1.1, stretch_len=1.1)
                    self.small = False
                elif self.powerup == "curve":
                    self.curve = False
                elif self.powerup == "random":
                    self.random = False
                elif self.powerup == "ghost":
                    self.t.showturtle()
                    self.ghost = False
                elif self.powerup == "split":
                    self.split = False
                self.powerup = None
        # Bounce off top/bottom
        if self.t.ycor() > 290:
            self.t.sety(290)
            self.dy = -abs(self.dy)
            particles.append(Particle(self.t.xcor(), 290, "white"))
            play_sound("bounce.wav")
        if self.t.ycor() < -290:
            self.t.sety(-290)
            self.dy = abs(self.dy)
            particles.append(Particle(self.t.xcor(), -290, "white"))
            play_sound("bounce.wav")
        # Bounce off paddles
        for paddle in paddles:
            px, py = paddle.t.xcor(), paddle.t.ycor()
            ptop = py + 50 * paddle.t.shapesize()[0]
            pbot = py - 50 * paddle.t.shapesize()[0]
            pright = px + 18 * paddle.t.shapesize()[1]
            pleft = px - 18 * paddle.t.shapesize()[1]
            bx, by = self.t.xcor(), self.t.ycor()
            # Paddle collision
            if pright > bx > pleft and pbot < by < ptop:
                # If shield, reflect with huge spin
                if paddle.shield:
                    # Direction based on paddle's side
                    if paddle.t.xcor() < 0: # left paddle
                        self.dx = abs(self.dx) * 1.2
                    else: # right paddle
                        self.dx = -abs(self.dx) * 1.2
                    self.spin = random.choice([-2.1,2.1])
                    particles.append(Particle(px, by, "cyan"))
                    play_sound("powerup.wav")
                else:
                    # Direction based on paddle's side
                    if paddle.t.xcor() < 0: # left paddle
                        self.dx = abs(self.dx) * random.uniform(1.05,1.18)
                    else: # right paddle
                        self.dx = -abs(self.dx) * random.uniform(1.05,1.18)
                    self.spin = (self.t.ycor() - py) / 75
                    particles.append(Particle(px, by, "white"))
                    play_sound("bounce.wav")
                # Clamp speed
                self.dx = clamp(self.dx, -self.max_speed, self.max_speed)
                self.dy = clamp(self.dy, -self.max_speed, self.max_speed)
        # Fade ghost
        if self.ghost:
            self.t.hideturtle()
        else:
            self.t.showturtle()

# --- Powerup Class ---
class Powerup:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.shape("circle")
        self.t.penup()
        self.t.shapesize(stretch_wid=2.1, stretch_len=2.1)
        self.type = random.choice([
            "grow", "shrink", "reverse", "freeze", "shield",
            "big", "small", "curve", "random", "ghost", "split", "multi"
        ])
        color_map = {
            "grow": "cyan",
            "shrink": "red",
            "reverse": "orange",
            "freeze": "blue",
            "shield": "lightgreen",
            "big": "yellow",
            "small": "gray",
            "curve": "violet",
            "random": "pink",
            "ghost": "white",
            "split": "gold",
            "multi": "green"
        }
        self.t.color(color_map[self.type])
        self.t.goto(random.randint(-300,300), random.randint(-200,200))
        self.spawn_time = time.time()
        self.active = True
        self.float_phase = random.uniform(0,math.pi*2)
    def update(self):
        # Float up/down
        self.float_phase += 0.1
        y = self.t.ycor() + math.sin(self.float_phase) * 1.8
        self.t.sety(clamp(y, -230,230))
        # Despawn after 7s
        if time.time() - self.spawn_time > 7:
            self.t.hideturtle()
            self.active = False
            return False
        return True
    def collide(self, ball):
        return self.t.distance(ball.t) < 40

# --- Game Class ---
class PongGame:
    def __init__(self, screen):
        self.screen = screen
        self.screen.tracer(0,0)
        self.bg = turtle.Turtle()
        self.bg.hideturtle()
        self.bg.speed(0)
        self.bg.up()
        self.bg.goto(0,0)
        self.paddle_a = Paddle(-360, "w", "s", self.screen)
        self.paddle_b = Paddle(360, "Up", "Down", self.screen)
        self.ball = Ball()
        self.extra_balls = []
        self.particles = []
        self.powerups = []
        self.score_a = 0
        self.score_b = 0
        self.score_display = turtle.Turtle()
        self.score_display.hideturtle()
        self.score_display.speed(0)
        self.score_display.up()
        self.score_display.goto(0, 260)
        self.score_display.color("white")
        self.state = "title"
        self.menu_display = turtle.Turtle()
        self.menu_display.hideturtle()
        self.menu_display.up()
        self.menu_display.speed(0)
        self.game_over_display = turtle.Turtle()
        self.game_over_display.hideturtle()
        self.game_over_display.up()
        self.game_over_display.speed(0)
        self.paused = False
        self._setup_controls()
        self._draw_title()
    def _setup_controls(self):
        self.screen.listen()
        self.screen.onkeypress(lambda: self._set_input(self.paddle_a, "up", True), self.paddle_a.upk)
        self.screen.onkeyrelease(lambda: self._set_input(self.paddle_a, "up", False), self.paddle_a.upk)
        self.screen.onkeypress(lambda: self._set_input(self.paddle_a, "down", True), self.paddle_a.downk)
        self.screen.onkeyrelease(lambda: self._set_input(self.paddle_a, "down", False), self.paddle_a.downk)
        self.screen.onkeypress(lambda: self._set_input(self.paddle_b, "up", True), self.paddle_b.upk)
        self.screen.onkeyrelease(lambda: self._set_input(self.paddle_b, "up", False), self.paddle_b.upk)
        self.screen.onkeypress(lambda: self._set_input(self.paddle_b, "down", True), self.paddle_b.downk)
        self.screen.onkeyrelease(lambda: self._set_input(self.paddle_b, "down", False), self.paddle_b.downk)
        self.screen.onkeypress(self._pause, "p")
        self.screen.onkeypress(self._restart, "r")
        self.screen.onkeypress(self._start_game, "space")
        self.screen.onkeypress(self._show_howto, "h")
        self.screen.onkeypress(self._exit, "Escape")
    def _set_input(self, paddle, key, state):
        paddle.input_state[key] = state
    def _draw_title(self):
        self.menu_display.clear()
        self.bg.clear()
        self.bg.goto(0,0)
        self.bg.color("black")
        self.bg.write("PONG DELUXE", align="center", font=("Arial", 44, "bold"))
        self.menu_display.goto(0, -60)
        self.menu_display.color("yellow")
        self.menu_display.write("Press SPACE to Start\nH for How to Play\nESC to Exit", align="center", font=("Arial", 24, "bold"))
        self.state = "title"
    def _show_howto(self):
        self.menu_display.clear()
        self.menu_display.goto(0, -20)
        self.menu_display.color("cyan")
        self.menu_display.write(
            "Controls:\nPlayer A: W/S\nPlayer B: UP/DOWN\nP: Pause, R: Restart\nPowerups spawn randomly!\nHit them with the ball to activate!\n\nPress SPACE to Start",
            align="center", font=("Arial", 19, "normal"))
        self.state = "howto"
    def _pause(self):
        if self.state == "game":
            self.paused = not self.paused
            if self.paused:
                self.menu_display.goto(0,0)
                self.menu_display.color("orange")
                self.menu_display.write("PAUSED\nPress P to Resume", align="center", font=("Arial",30,"bold"))
            else:
                self.menu_display.clear()
    def _exit(self):
        self.screen.bye()
    def _restart(self):
        if self.state == "gameover":
            self.score_a = 0
            self.score_b = 0
            self.ball = Ball()
            self.extra_balls.clear()
            self.particles.clear()
            self.powerups.clear()
            self.game_over_display.clear()
            self.score_display.clear()
            self._draw_title()
    def _start_game(self):
        if self.state in ["title", "howto"]:
            self.menu_display.clear()
            self.bg.clear()
            self.score_display.clear()
            self.score_a = 0
            self.score_b = 0
            self.ball = Ball()
            self.extra_balls.clear()
            self.particles.clear()
            self.powerups.clear()
            self.state = "game"
            self.paused = False
            self._game_loop()
    def _game_over(self):
        self.state = "gameover"
        self.game_over_display.goto(0,0)
        self.game_over_display.color("red")
        self.game_over_display.write("GAME OVER\nPress R to Restart\nESC to Exit", align="center", font=("Arial",34,"bold"))
        play_sound("gameover.wav")
    def _spawn_powerup(self):
        if len(self.powerups) < 5 and random.random() < 0.08:
            power = Powerup()
            self.powerups.append(power)
    def _game_loop(self):
        while self.state == "game":
            if not self.paused:
                # Background
                self.bg.clear()
                self.bg.color("gray")
                self.bg.goto(0,0)
                self.bg.setheading(0)
                self.bg.pendown()
                self.bg.width(3)
                for i in range(-290, 300, 40):
                    self.bg.setpos(-2, i)
                    self.bg.setpos(2, i+20)
                self.bg.penup()
                # Move paddles
                self.paddle_a.move()
                self.paddle_b.move()
                # Move ball
                self.ball.update([self.paddle_a, self.paddle_b], self.particles)
                # Move extra balls
                for ball in self.extra_balls:
                    ball.update([self.paddle_a, self.paddle_b], self.particles)
                # Powerups
                self._spawn_powerup()
                for power in self.powerups[:]:
                    if power.active:
                        power.update()
                        # Ball collision
                        if power.collide(self.ball):
                            self._activate_powerup(power, self.ball, self.paddle_a if self.ball.t.xcor()<0 else self.paddle_b)
                        for eb in self.extra_balls:
                            if power.collide(eb):
                                self._activate_powerup(power, eb, self.paddle_a if eb.t.xcor()<0 else self.paddle_b)
                    else:
                        self.powerups.remove(power)
                # Particle update
                for p in self.particles[:]:
                    if not p.update():
                        self.particles.remove(p)
                # Score/Goal check
                self._check_goal(self.ball)
                for eb in self.extra_balls[:]:
                    self._check_goal(eb, extra=True)
                # Draw score
                self.score_display.clear()
                self.score_display.goto(-120, 262)
                self.score_display.color("green")
                self.score_display.write(str(self.score_a), font=("Arial", 32, "bold"))
                self.score_display.goto(120, 262)
                self.score_display.color("blue")
                self.score_display.write(str(self.score_b), font=("Arial", 32, "bold"))
            self.screen.update()
            time.sleep(1/60)
    def _check_goal(self, ball, extra=False):
        if ball.t.xcor() > 410:
            self.score_a += 1
            self.particles.append(Particle(ball.t.xcor(), ball.t.ycor(), "green"))
            play_sound("score.wav")
            if not extra:
                ball.t.goto(0, random.randint(-90,90))
                ball.dx = -ball.base_speed
                ball.dy = random.choice([-ball.base_speed, ball.base_speed])
                ball.spin = random.uniform(-2,2)
            else:
                ball.t.hideturtle()
                if ball in self.extra_balls: self.extra_balls.remove(ball)
            if self.score_a >= 10:
                self._game_over()
        if ball.t.xcor() < -410:
            self.score_b += 1
            self.particles.append(Particle(ball.t.xcor(), ball.t.ycor(), "blue"))
            play_sound("score.wav")
            if not extra:
                ball.t.goto(0, random.randint(-90,90))
                ball.dx = ball.base_speed
                ball.dy = random.choice([-ball.base_speed, ball.base_speed])
                ball.spin = random.uniform(-2,2)
            else:
                ball.t.hideturtle()
                if ball in self.extra_balls: self.extra_balls.remove(ball)
            if self.score_b >= 10:
                self._game_over()
    def _activate_powerup(self, power, ball, paddle):
        t = power.type
        # Powerup to paddle or ball
        if t == "grow":
            paddle.t.shapesize(stretch_wid=10, stretch_len=2.2)
            paddle.powerup = "grow"
            paddle.powerup_timer = 180
        elif t == "shrink":
            paddle.t.shapesize(stretch_wid=2.3, stretch_len=1.1)
            paddle.powerup = "shrink"
            paddle.powerup_timer = 160
        elif t == "reverse":
            paddle.reverse = True
            paddle.powerup = "reverse"
            paddle.powerup_timer = 160
        elif t == "freeze":
            paddle.freeze = True
            paddle.powerup = "freeze"
            paddle.powerup_timer = 110
        elif t == "shield":
            paddle.shield = True
            paddle.powerup = "shield"
            paddle.powerup_timer = 180
        elif t == "big":
            ball.t.shapesize(stretch_wid=2.6, stretch_len=2.6)
            ball.powerup = "big"
            ball.powerup_timer = 140
            ball.big = True
        elif t == "small":
            ball.t.shapesize(stretch_wid=0.6, stretch_len=0.6)
            ball.powerup = "small"
            ball.powerup_timer = 180
            ball.small = True
        elif t == "curve":
            ball.curve = True
            ball.powerup = "curve"
            ball.powerup_timer = 130
        elif t == "random":
            ball.random = True
            ball.powerup = "random"
            ball.powerup_timer = 110
        elif t == "ghost":
            ball.ghost = True
            ball.powerup = "ghost"
            ball.powerup_timer = 100
        elif t == "split":
            ball.split = True
            ball.powerup = "split"
            ball.powerup_timer = 1
            self._ball_split(ball)
        elif t == "multi":
            for i in range(2):
                eb = Ball()
                eb.t.goto(ball.t.xcor(), ball.t.ycor())
                eb.dx = random.choice([-eb.base_speed, eb.base_speed])
                eb.dy = random.choice([-eb.base_speed, eb.base_speed])
                self.extra_balls.append(eb)
        power.t.goto(1000,1000) # Move offscreen
        power.active = False
        play_sound("powerup.wav")
        for _ in range(7):
            self.particles.append(Particle(ball.t.xcor(), ball.t.ycor(), power.t.color()[0]))
    def _ball_split(self, ball):
        # Create two extra balls splitting in different directions
        for ang in [-1,1]:
            eb = Ball()
            eb.t.goto(ball.t.xcor(), ball.t.ycor())
            eb.dx = ang * eb.base_speed * random.uniform(1,1.3)
            eb.dy = random.choice([-eb.base_speed, eb.base_speed])
            self.extra_balls.append(eb)

# --- Main ---
if __name__ == "__main__":
    game = PongGame(wn)
    turtle.mainloop()