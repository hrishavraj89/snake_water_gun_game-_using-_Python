# **Snake, Water, Gun – Python CLI Game**

## **Description**
A simple Python command-line game that implements the classic Snake, Water, Gun game. It's a fun and beginner-friendly mini-project to understand how to use:
Dictionaries
Random module
Conditional logic
User input handling


## **This version uses:**
1 for Snake
-1 for Water
0 for Gun


## **Game Rules**
| Your Choice | Computer's Choice | Winner       |
| ----------- | ----------------- | ------------ |
| Snake       | Water             | You Win      |
| Snake       | Gun               | You Win      |
| Water       | Gun               | You Lose     |
| Water       | Snake             | You Lose     |
| Gun         | Snake             | You Lose     |
| Gun         | Water             | You Win      |
| Same        | Same              | It's a Draw! |


## **How It Works**
The computer randomly selects a value from [-1, 0, 1].
The user enters 's', 'w', or 'g'.
The game maps both inputs to integers, compares them, and prints the result.


## **Requirements**
 Python 3.x
 No external libraries


## **How to Run**
1. Clone this repo:
git clone https://github.com/yourusername/snake-water-gun-python.git
cd snake-water-gun-python

2. Run the script:
python snake_water_gun.py


## **File Structure**
snake-water-gun-python/
│
├── snake_water_gun.py   # Main game logic
├── README.md            # Project description


## **Future Improvements**
Add multiple rounds with scoring
GUI version using Tkinter
Input validation and replay option
Multiplayer version
