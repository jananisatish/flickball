# Flickball

## What is Flickball?

Flickball is a game where you flick a ball and try to get it past a robotic goalie, which will try to block you. I used a sensor called Pixy2 to detect where the ball is and where it will end up.

![demo video](/images/flickball_demo.gif?raw=true)

## Set Up
### Gameboard
Flickball is played on a gameboard. I made my gameboard out of cardboard, but it could really be made of anything flat, movable, and hard to bend. The main board, where you will flick the ball, is 24 inches wide and 32 inches long. Behind this is another board, which is 24 inches wide and 6 inches long. This board is there because the 1/4 inch wide gap between it and the main board is used as a track for the robot so that it can move left and right in a straight line, similar to the use of train tracks for a train. This is an image of my gameboard:  
![set-up](/images/flickball.jpg?raw=true)

### Structure
I made a LEGO Mindstorms EV3 structure to hold the EV3 and Pixy2. It is very tall so that the Pixy2 can see the whole board and identify the ball wherever it is on the board. My structure is 4 inches wide and 18.25 inches high. You can build your structure with any materials you have, as long as it's sturdy, raises the Pixy2 high enough that it can see the whole board, and raises the EV3 high enough so that you can connect it to the Pixy2 with a cable. This is an image of my structure:
![structure](/images/structure.jpg?raw=true)

### Markings
The structure is right behind the minor part of the gameboard. I made markings on the minor board to show where the structure should go, so that I could place it in the same spot every time. The first mark, which represents where the left side of the structure should go, is 10 inches away from the left side of the minor board. The second mark, which represents where the right side of the structure should go, is 14 inches away from the left side of the minor board. I made these same markings at the edge of the main board, and used them to align the motor. I also drew a circle to show where the ball should go. The distance from the center of the circle to the top of the main gameboard is 5.5 centimeters, and the radius of the circle is 3 centimeters.
![gameboard markings](/images/board_markings.png?raw=true)

### Ball
The ball that I used for Flickball had a circumference of 7 inches. It is important that you choose the right colour when picking out the ball that you need, because it has to be distinguishable enough for the Pixy2 to detect it from a far distance. I used a bright blue ball with white swirls on it. However, it is better to use a ball with only one colour on it than a ball with many colours because Pixy2 can only use one colour to detect objects and it might not notice your ball if it has lots of other colours on it too. The best thing to do is to get many different colour balls and to teach Pixy2 each one and see which one is detected best at a far distance. 
![ball](/images/ball.jpg?raw=true)

### Pixy2
I used the Pixy2 sensor to recognize where the ball is. Pixy2 can detect objects using their colour, but you have to "teach" it to detect the object you want it to detect. To do this, you first have to install PixyMon, an app that lets you see what the Pixy2 is seeing. 
![Pixy2 vision](/images/pixy2_vision.png?raw=true)
This website has instructions on installing PixyMon (https://docs.pixycam.com/wiki/doku.php?id=wiki:v2:install_pixymon_on_windows_vista_7_8) and this website has instruction on teaching Pixy2 an object
(https://docs.pixycam.com/wiki/doku.php?id=wiki:v2:teach_pixy_an_object_2). The second website also talks about tuning the signatures so that it doesn't detect false positives or false negatives. These are the settings that we used: 
![Pixy2 settings](/images/pixy2_settings.png?raw=true)

