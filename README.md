# Resistor Calculator
A python script for finding the best combination of resistors in a limited set to be used in a non-inverting op amp or voltage divider.

### Has this ever happened to you???
You're working on a circuit late at night, and discover that an output voltage is either much larger or much smaller than it should be. 
To fix this, you can just amplify it with an op amp, or scale it down with a voltage divider. But oh no! You only have a limited set of resistors to use! 
How can you possibly find the best pair of resistors for your circuit if they are all unusual values?

### Well then this python script is for you!
Just plug the resistor values that you have into the resistors.csv file, and then run resistor_calc.py. 
This will prompt you to enter the input voltage for either the amplifier or voltage divider, as well as your desired output voltage. 
Then, the script will parse every possible combination of resistors, until it finds the pair best fit to reach your output voltage. Hooray!

### How fast is it?
Not very fast! I wrote this late at night and had a small mental breakdown when I realized that this problem is kinda like the knapsack problem 
and would require dynamic programming in order to solve it correctly. So I didn't do that! This algorithm just brute-forces it's way through every combination. 
So just don't load in too many resistors and it will be okay!
