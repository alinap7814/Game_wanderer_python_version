# Game_wanderer_python_version
Game-> wanderer with characters like: monsters, big boss and hero. Python version.

1) class Boss -> initialisation boss class and loading the image
2) class character -> initialisation class, check and return position, check and returm statements: alive or not.
3) class Floor, class Path -> initialisation class, initialization map for game, add walls, check can we croos or not map. 
   Class Path -> path of Brick class, check abd show can be crossed or not, like you can when don`t have the monster on you possition.
4) class Brick -> initialisation class, has parameters which create canvas to draw, create and chec type of brick like: wall or path, 
     return coordinating x or y of brick. Crossability arguments it`s boolean, according to the type brick and check can we cross or not cross the brick.
5) class Level -> initialisation class, create level, check position(monster for example), start and show you fight and result...
6) anothr class, and package -> initialization class if it`s calss whith path of game like hero, wall ... create and loading the image, 
   check and calculate steps(package stap_path, calculate_path and checking_errors_path)
7) class Text -> Create and print txt information about game (like path with hero)
