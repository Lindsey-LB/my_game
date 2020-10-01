# my_game

## Purpose
*This program uses Pygame to generate a simple game.*

**Note:** Pygame must be installed for the game to initialise
 
### Game objective:
*Avoid the enemies on the path to the prize. Collide with the prize,and win. Collide with the enemies, and lose.*

### Game content:
*The game contains:*
* 1 Player object
* Enemy objects
* 1 Prize object
* 1 Background object
* 1 Game icon

*These objects are required to be contained in the same folder as the program.*

### Starting Positions & Movement:
1. **Player** - *starts on the left boundary of the screen, at centre height, and is able to move in all directions using the arrow keys.*
2. **Enemies** - *start at random heights, just outside of the right boundary of the screen, and travel from right to left.*
*Once they pass the left boundary, they reappear on the right, at new random heights.*
3. **Prize** - *starts on the right boundary of the screen, at a random height. The prize does not move.*
