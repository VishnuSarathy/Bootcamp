# Assignment 1 – ROS Nodes, Topics, Publishers, Subscribers, and Services

## MISSION:

The task is to inspect the surrounding area using a TurtleBot. To achieve this, the TurtleBot employs a unique method: teleporting to strategic positions and performing circular rotations for thorough exploration.

The input given to the TurtleBot will consist of teleportation coordinates (x, y) and a radius.

The TurtleBot first teleports to the specified coordinates.

It then moves in the positive x-direction along the given radius.

Finally, it moves in a circular path of the desired radius.

## Steps:

Create a catkin workspace for the assignments. You can name it whatever you want. (e.g. catkin_ws the _ws is just a convention)
Create a package called turtle_pub in the workspace.
Create nodes to publish on cmd_vel topic.
Create a service called draw_circle that will take three inputs (x,y,radius) and returns bool Success when runed properly.
Deadline: 10th September, 2025

## Submission Format:

You have to create a pull request against the ros branch.
Your PR should contain the src folder from the workspace.
Your PR should contain the README.md file with all the details about how to run your code and the procedure you followed
Essentially the folder structure will look like:
```plaintext
Bootcamp
├── RollNo.
│   ├── README.md
│   └── src
│       └── turtle_pub
│           ├── srv
│           ├── CMakeLists.txt
│           ├── package.xml
│           └── src
│               └── scripts
└── README.md

