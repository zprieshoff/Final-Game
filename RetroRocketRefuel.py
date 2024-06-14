#(lab) Final Game
#Zechariah Prieshoff
#June 4th, 2024
#A simple, space themed slide and catch game.

import pygame
import simpleGE
import random


class Satellite(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage('satellite.png')
        self.setSize(30, 30)
        self.minSpeed = 3
        self.maxSpeed = 7
        self.reset()


    def reset(self):
        self.x = random.randint(0, self.screen.get_width())
        self.y = random.randint(0, self.screen.get_height())
        self.dx = random.randint(-5, 5)
        self.dy = random.randint(-5, 5)

    def checkBounds(self):
        if self.left < 0:
            self.reset()
        if self.right > self.screenWidth:
            self.reset()
        if self.top < 0:
            self.reset()
        if self.bottom > self.screenHeight:
            self.reset()


class SpeedBoost(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("speedBoost.png")
        self.setSize(40, 30)
        self.speed = 18
        self.reset()

    def reset(self):
        self.x = 10
        self.y = random.randint(0, self.screen.get_height())
        self.dx = self.speed

    def checkBounds(self):
        if self.right > self.screen.get_width():
            self.reset()


class Asteroid(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("asteroid.png")
        self.setSize(40, 30)
        self.minSpeed = 3
        self.maxSpeed = 10
        self.reset()

    def reset(self):
        self.x = self.screen.get_width()
        self.y = random.randint(0, self.screen.get_height())
        self.dx = -random.randint(self.minSpeed, self.maxSpeed)

    def checkBounds(self):
        if self.left < 0:
            self.reset()


class Fuel(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("fuel.png")
        self.setSize(30, 30)
        self.minSpeed = 4
        self.maxSpeed = 8
        self.reset()

    def reset(self):
        self.x = 10
        self.y = random.randint(0, self.screen.get_height())
        self.dx = random.randint(self.minSpeed, self.maxSpeed)

    def checkBounds(self):
        if self.right > self.screen.get_width():
            self.reset()


class Ship(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("spaceshipv2.png")
        self.setSize(50, 40)
        self.position = (320, 240)
        self.movespeed = 7

    def process(self):
        if self.isKeyPressed(pygame.K_UP):
            self.y -= self.movespeed
        if self.isKeyPressed(pygame.K_DOWN):
            self.y += self.movespeed


class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time left: 10"
        self.center = (500, 30)


class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)


class Game(simpleGE.Scene):
    def __init__(self, numFuels = 5, numAsteroids = 4, numSpeedBoosts = 1, numSatellites = 1):
        super().__init__()
        self.setImage("arcadespace.jpg")

        self.soundFuel = simpleGE.Sound("item.wav")
        self.soundSpeed = simpleGE.Sound("powerup.wav")
        self.soundSatellite = simpleGE.Sound("hit.wav")

        self.numFuels = numFuels
        self.numAsteroids = numAsteroids
        self.numSpeedBoosts = numSpeedBoosts
        self.numSatellites = numSatellites

        self.score = 0
        self.lblScore = LblScore()
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 5
        self.lblTime = LblTime()

        self.ship = Ship(self)
        self.fuels = []
        self.asteroids = []
        self.speedBoosts = []
        self.satellites = []

        for i in range(self.numFuels):
            self.fuels.append(Fuel(self))
        for i in range(self.numAsteroids):
            self.asteroids.append(Asteroid(self))
        for i in range(self.numSpeedBoosts):
            self.speedBoosts.append(SpeedBoost(self))
        for i in range(self.numSatellites):
            self.satellites.append(Satellite(self))

        self.sprites = [self.ship, self.fuels, self.asteroids, self.speedBoosts, self.satellites, self.lblScore, self.lblTime]

    def process(self):
        for fuel in self.fuels:
            if fuel.collidesWith(self.ship):
                fuel.reset()
                self.soundFuel.play()
                self.score += 1
                self.timer.totalTime += 0.8
                self.lblScore.text = f"Score: {self.score}"

        for asteroid in self.asteroids:
            if asteroid.collidesWith(self.ship):
                print("Hit by an asteroid!")
                self.stop()

        for speedBoost in self.speedBoosts:
            if speedBoost.collidesWith(self.ship):
                speedBoost.reset()
                self.soundSpeed.play()
                self.ship.movespeed += .3

        for satellite in self.satellites:
            if satellite.collidesWith(self.ship):
                satellite.reset()
                self.soundSatellite.play()
                self.ship.movespeed -= .3

        self.lblTime.text = f"Fuel left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print("Lost in space!")
            print(f"Score: {self.score}")
            self.stop()


class HowToPlay(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("arcadespace.jpg")

        self.howToPlay = simpleGE.Label()
        self.howToPlay.text = "How To Play"
        self.howToPlay.size = (200, 35)
        self.howToPlay.center = (320, 90)
        self.howToPlay.fgColor = (0xFF, 0xEF, 0xD5)
        self.howToPlay.bgColor = (0x1F, 0x1F, 0x1F)

        self.instructions = simpleGE.MultiLabel()
        self.instructions.fgColor = (0xFF, 0xEF, 0xD5)
        self.instructions.bgColor = (0x1F, 0x1F, 0x1F)

        self.instructions.textLines = ["To move the ship, use your up and down arrows!", "In the intro screen, press" 
                                       " Space to play,", "Q to quit, "
                                       "and H to enter how to play.",
                                       "In the how to play screen press B to go back.",
                                       "All buttons can also be clicked with your mouse!",
                                       "Lightning bolts speed you up", " and Satellites slow you down!"]
        self.instructions.center = (320, 200)
        self.instructions.size = (550, 350)

        self.btnBack = simpleGE.Button()
        self.btnBack.text = "Back"
        self.btnBack.center = (320, 400)
        self.btnBack.size = (150, 30)
        self.btnBack.fgColor = (0xFF, 0xEF, 0xD5)
        self.btnBack.bgColor = (0x1F, 0x1F, 0x1F)

        self.sprites = [self.howToPlay, self.instructions, self.btnBack]

    def process(self):
        if self.btnBack.clicked or self.isKeyPressed(pygame.K_b):
            self.response = "Back"
            print("Loading title screen...")
            self.stop()


class StartScreen(simpleGE.Scene):
    def __init__(self, prevScore):
        super().__init__()

        self.prevScore = prevScore

        self.setImage("arcadespace.jpg")
        self.response = "Play"

        self.dev = simpleGE.Label()
        self.dev.fgColor = (0xFF, 0xEF, 0xD5)
        self.dev.bgColor = (0x1F, 0x1F, 0x1F)
        self.dev.text = "Developer high score: 53"
        self.dev.size = (250, 35)
        self.dev.center = (320, 450)

        self.directions = simpleGE.MultiLabel()
        self.directions.fgColor = (0xFF, 0xEF, 0xD5)
        self.directions.bgColor = (0x1F, 0x1F, 0x1F)
        self.directions.font = pygame.font.Font("Retronoid-BZX3.ttf", 20)
        self.directions.textLines = ["Welcome to Retro Rocket Refuel!", "Dodge the asteroids ",
                                     "and catch fuel to continue your journey!",
                                     "Good luck Space Ranger!"]
        self.directions.center = (320, 170)
        self.directions.size = (550, 250)

        self.btnHowTo = simpleGE.Button()
        self.btnHowTo.fgColor = (0xFF, 0xEF, 0xD5)
        self.btnHowTo.bgColor = (0x1F, 0x1F, 0x1F)
        self.btnHowTo.text = "How to play"
        self.btnHowTo.center = (320, 350)
        self.btnHowTo.size = (150, 30)

        self.btnPlay = simpleGE.Button()
        self.btnPlay.fgColor = (0xFF, 0xEF, 0xD5)
        self.btnPlay.bgColor = (0x1F, 0x1F, 0x1F)
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100, 400)
        self.btnPlay.size = (150, 30)

        self.btnQuit = simpleGE.Button()
        self.btnQuit.fgColor = (0xFF, 0xEF, 0xD5)
        self.btnQuit.bgColor = (0x1F, 0x1F, 0x1F)
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (540, 400)
        self.btnQuit.size = (150, 30)

        self.lblScore = simpleGE.Label()
        self.lblScore.fgColor = (0xFF, 0xEF, 0xD5)
        self.lblScore.bgColor = (0x1F, 0x1F, 0x1F)
        self.lblScore.text = "Last Score: 0"
        self.lblScore.center = (320, 400)
        self.btnQuit.size = (150, 30)
        self.lblScore.text = f"Last Score: {self.prevScore}"


        self.sprites = [self.directions, self.dev, self.btnHowTo, self.btnPlay, self.btnQuit, self.lblScore]

    def process(self):
        if self.btnPlay.clicked or self.isKeyPressed(pygame.K_SPACE):
            self.response = "Play"
            self.stop()
        elif self.btnQuit.clicked or self.isKeyPressed(pygame.K_q):
            self.response = "Quit"
            self.stop()
        elif self.btnHowTo.clicked or self.isKeyPressed(pygame.K_h):
            self.response = "How"
            self.stop()


def main():
    keepGoing = True
    lastScore = 0

    while keepGoing:
        startScreen = StartScreen(lastScore)
        startScreen.start()

        if startScreen.response == "How":
            print("Opening How To Play...")
            howToPlay = HowToPlay()
            howToPlay.start()

        if startScreen.response == "Play":
            print("Starting game...")
            game = Game()
            game.start()
            lastScore = game.score
        elif startScreen.response == "Quit":
            print("Closing game...")
            keepGoing = False


if __name__ == "__main__":
    main()
