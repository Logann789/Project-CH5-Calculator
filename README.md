Final Design
For each week we always want to lay out the final design. As this week is based
around the logic rather than how it looks, we’ll lay out the steps necessary to build our
calculator:
1. Ask the user for the calculation they would like to perform.
2. Ask the user for the numbers they would like to run the operation
on.
3. Check for correct input for the mathematical operation.
a. Convert numbers input to floats.
b. Perform operation and print result.
c. If an there is an error, an print error message.

Creating a Calculator
Last week we built a receipt printing program. With the lessons learned from this
week, we’re going to be building a simple calculator that accepts user input and
outputs the proper result.

Step #1: Ask User for Calculation to Be Performed
For each one of these steps, let’s put the code in separate cells. This will allow us to
section of the specific steps for our project, making it easier to test each step. The first
step is to ask the user to input the mathematical operation to be performed (add,
subtract, etc.):
Step #2: Ask for Numbers, Alert Order Matters
In the cell below step #1, we’ll need to create the next step of our logic. Here, we ask the
user to input a couple of numbers and output those numbers for testing purposes:
Step #3: Check for correct input
The third, and final step, is to try performing the operation. We must convert the user’s
input to floating data types. We should assume that they may not enter the proper input,
so we need to check whether or not the input is correct. Technically, we don't know
how to do this yet, so you could skip it and assume your user will always enter correct
input. If you want a more sophisticated approach, Google "python try except".
