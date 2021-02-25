<p align="center">
 <img height=350px src="./simulation-output.png" alt="Traffic Signal Timer">
</p>

<h1 align="center">Basic Traffic Intersection Simulation</h1>

<div align="center">

[![Python version](https://img.shields.io/badge/python-3.1+-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

<h4>A simulation developed from scratch using [Pygame](https://www.pygame.org/news) to simulate the movement of vehicles across a traffic intersection having traffic lights with a timer.</h4>

</div>

-----------------------------------------
### Description

* It contains a 4-way traffic intersection with traffic signals controlling the flow of traffic in each direction. 
* Each signal has a timer on top of it which shows the time remaining for the signal to switch from green to yellow, yellow to red, or red to green. 
* Vehicles such as cars, bikes, buses, and trucks are generated, and their movement is controlled according to the signals and the vehicles around them. 
* This simulation can be further used for data analysis or to visualize AI or ML applications. 

The video below shows the final output of the simulation.

------------------------------------------
### Demo

<p align="center">
    <img height="600px" src="./Demo.gif">
</p>

------------------------------------------
### Prerequisites

[Python 3.1+](https://www.python.org/downloads/)

------------------------------------------
### Installation

 * Step I: Clone the Repository
```sh
      $ git clone https://github.com/mihir-m-gandhi/Adaptive-Traffic-Signal-Timer
```
  * Step II: Install the required packages
```sh
      # On the terminal, move into Basic-Traffic-Intersection-Simulation directory
      $ cd Basic-Traffic-Intersection-Simulation
      $ pip install pygame
```
* Step III: Run the code
```sh
      # To run simulation
      $ python simulation.py
```

------------------------------------------
### Author

Mihir Gandhi - [mihir-m-gandhi](https://github.com/mihir-m-gandhi)

------------------------------------------
### License
This project is licensed under the MIT - see the [LICENSE](./LICENSE) file for details.
