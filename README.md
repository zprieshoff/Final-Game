Game developed by: Zechariah Prieshoff and Professor Harris

Full game design document with diagrams: https://docs.google.com/document/d/131dR9YhsNOCy90gVAHNOYeH1XPZIqgidkbAo0-g7sQg/edit?usp=sharing

# Project Goals

* **My main goals** were to just have a working game and visuals that were pleasing to the eye. If I had a little more time with this project I think It could be a lot better, but for what I have now I am very happy with it.
* Here were my **milestones for this project:**
  1. Game scene with background image
  2. Add basic Ship sprite
  3. Add keyboard motion to Ship
  4. Add single fuel with reset, gliding and boundary behaviors
  5. Add collision effect between spaceship and fuel, sound effect
  6. Modify for multiple (5) fuels including collision behavior
  7. Add scorekeeping, timing, and appropriate labels
  8. Add startscreen class and state transition
  9. How to play scene with background image and label + button
  10. Add single asteroid with reset, gliding and boundary behaviors
  11. Add collision effect between spaceship and asteroid
  12. Modify for multiple (4) asteroids including collision behavior
  13. Add single speed boost with reset, gliding and boundary behaviors
  14. Add collision effect between spaceship and speed boost, sound effect
  15. Add single satellite with reset, gliding and boundary behaviors
  16. Add collision effect between spaceship and satellite, sound effect

* I didn't want to risk any copyright problems so I also had to create most of my sprites and the background image. Since I am not an artist I created some another set of **milestones that focused on visuals:**
1. Create game background image
2. Create ship image
3. Find fuel image
4. Create asteroid image
5. Create speed boost image
6. Create satellite image

* These were simple milestones but each image took about 45 minutes each, exluding the space ship.
* I am very happy with how each image turned out.

# Instructions for the player

* My game is very simple. Gameplay controls are your **up and down arrows.**
* When playing the game, from the left side of your window you'll **red fuel canisters and blue lightning bolts**, on the right side you'll see **asteroids**, and randomly on the screen there will be **satellites**.
1. The fuel canisters is what you want to catch, the more you catch the longer you play.
2. The lightning bolts are speed boosts, these don't do anything other than add to your ships speed. 
3. The asteroids are what you'll need to dodge. There are no lives so its a one-and-done kind of deal.
4. The satellites, just like the speed boosts, are optional to catch. These act kind of like space debris so if you collect one it lowers your speed.

* **I added the speed boost and asteroid to cater to players who prefer faster gameplay, and those who prefer slower.**
# Technologies and techniques

## The technologies used in the program:
* The main technoloy I used is Pygame. This creates my game window and is in control of the overall framework
* The other main technology is my professers simple game engine (SimpleGE). This handles pretty much everything that pygame doesn't. These are the sprites, labels, buttons and timer mechanics used, to name a few.
* Another technology is the import modules. I imported **random**, **pygame**, and **simpleGE**. Random is used almost exclusively in the sprite classes to determine where the sprites will spawn and how fast they will move.

## The techniques used in the program
* **Objects**: Objects were used throughout the program as properties of game elements/sprites like fuel and asteroids through classes.
* **Sprites**: This game is nothing without the sprites. They are used for all of the visual elements of the game. Each sprite has its own size, speed, and positions in the gameplay scene.
* **Loops**: The game is run inside of a while loop inside the main function using "keepGoing".

# External Citations

* **Fuel template**: https://www.pixilart.com/draw/gas-can-0d8faf0067e0f64
* **Powerup.wav**: Free sound from Freesound.
https://freesound.org/people/Romeo_Kaleikau/sounds/588251/
* **Item.wav**: Free sound from Freesound
https://freesound.org/people/MATRIXXX_/sounds/703886/#comments
* **Hit.wav**: Free sound from Freesound
https://freesound.org/people/leviclaassen/sounds/107789/
* **Retronoid-BZX3.ttf**: Free font from fontspace for non-commercial use
https://www.fontspace.com/retronoid-font-f31918
* **Other sprites**: Background image, spaceship, asteroid, speed boost, and satellite sprites were all created by me using:
https://www.pixilart.com/

# My process

## What I learned
I have never worked with pygame before, so pretty much everything I used in this program was taught to me by my professer through videos, documents, and emails. One of the parts that was annyoying- but fun to learn, was how to use the axis of each sprite. Testing a self.dx  axis code and seeing my sprite spin in circles and get stuck in a corner was always fun.
I enjoyed creating the classes and scenes, and after they were completed it felt really good to be able to click the buttons and see that they all work properly.

## Where I got stuck
My Satellite class is where I got stuck the longest. Left/right, up/down movement is easy but I really struggled with diagonal movement and letting the program move the sprite towards which ever corner it wanted to. 
I did get stuck on the asteroids movement but only because I thoguht I could just copy and paste from the fuel sprite code. 

## What I would like to improve
If I had the option, I wouuld use a bigger window to give the player more room, but I would also have liked to add the option to shoot.
I couldn't get my satellites movement 100% how I wanted it, even with my professors help. I thought I was on the right track, and I was, but not as good as I was hoping. Currently, the satellites spawn randomly on the screen and move towards an edge but I was wanting to be able to make them spawn on a random edge and also move towards a random edge.

## How I would do things differently
I'm not sure how much different my program would be if I were to do this again, maybe clean the sprite hit boxes up if I could? You only have to get close to a sprite for the collision code to happen, and although thats fine for a school project, I think if I ever wanted to release a game commercially I'd need to fix that.
Instead of a timer, I wanted to have a meter to the left of the screen that would be made up of blocks, and each block would represent a second. I wanted this to be used as the timer but I didn't want to fall behind in the rest of the program so I did not implement this. This would have gave the UI of the game a more "spaceship" feel.

## Did I stray from the game design document
In my original document, it was a side-to-side game and I did have the fuel meter drawn out, but in the game doc for the final version I think I was pretty exact with everything. It helped that I had some of it, like my init pseudo  code written out from previous versions. 

## How did I stay on track
My professor made it very clear to us in every assignment to do the necessary things first like making the game work, then work on visuals and other mechanics, so I just listened to that. Whenever I was creating the how to screen and class I always tested before adding the label or button. 
I spent way too much time trying to get my developer highscore so I strayed a little off course but I wanted to give the players an objective to beat. (and I enjoy my game!)





