# brownian_tree

A program that will trace the path of brownian motion on a particle. You can either enter parameters to run the program with (image size, starting position, starting color, etc) or let it run on it's own and it will use default parameters. When initialized, the program draws a white circle at the starting position with radius 5px. It includes functionality to have a colored path that changes over time. Every time that a multiple of 50,000 is reached, a small x will appear. The x starts out as black, but gradually changes to green. I am planning to add functionality that lets you input a boundary (circle, triangle, hexagon, etc) so that it will stop if it reaches the boundary, as well as functionality to have multiple particles moving at once and having the ability to spawn more particles.

There is a bug where the program will continue running if it hits the top boundary. I tried figuring that out before pushing, but I can't figure it out tonight.
