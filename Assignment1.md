# Assignment 1


### **Expectations**

1. **Submission Requirements**:
   - You must submit a **Jupyter notebook** with all your solutions.
   - Along with the notebook, submit a **recording** where you explain your solutions. 
     - The recording **must include your voice and face** (use your webcam).
   
2. **Solution Explanations**:
   - For **each question**, provide an explanation of your solution.
   - Use your **judgment** to determine how detailed the explanation should be based on the complexity of the question.
   
3. **Markdown Explanations**:
   - Write a **basic explanation** of each solution in a **Markdown cell** below the code.
   - Use **bullet points** or **jot notes**. Keep it brief and clear. 
   - **Do not write paragraphs**. The explanation is meant to help guide your verbal explanation in the recording.

4. **Recording Expectations**:
   - During your recording, use the Markdown notes as a reference to explain the code verbally.
   - Make sure you **verbally explain** the logic behind your code as you walk through each solution.
  
5. **Open Book**:
    - While this assignment may seem extensive, remember that it’s open book. Most of the material is already covered in the notebook I’ve provided, which includes working code, examples, and detailed narration in markdown cells.

**Important Note**: If I notice excessive overlap between solutions submitted by different individuals, both assignments will be given a score of 0. Please ensure that all work is your own.



### **Section A: Package Management**

Total Questions: `4` * 2 (For explanation)
Total Marks: `8`


#### A1. File Creation and Variable Definition
1. Create a file `lib.py` inside a folder called `utils` and define a variable with a value. This can be done either:
   - manually
   - using bash commands **hint**: `touch`, `echo`, `>`
   - `with open`

#### A2. Importing Variables
2. Import the variable using `import <>`.
3. Import the variable using `from <> import <>`.
4. Explain the difference between the two import methods and their pros and cons.

---

### **Section B: Data Types and Structures**

Total Questions: `20` * 2 (For explanation)

Total Marks: `40`


1. How can you explore all available methods and attributes that you can call on a list, string, or tuple object? Show examples for all three.
   - **Hint**: Use a built-in Python function that lists everything defined for an object, including methods and attributes. Try applying it to a list, string, and tuple.

2. How can you view the doc-string (documentation) of a specific method (e.g., a method from a set object)? Choose one method from the set object and demonstrate how to access its documentation.
   - **Hint**: Use a built-in Python function to get detailed information about a method. Try using this function on methods like `.add()` or `.remove()` from a set.

#### B1. Lists
3. Create a list of your favorite vegetables and order it from most to least favorite.
4. Print the index and the item in the list using the first method discussed in class.  
   - **Hint**: Use `enumerate()`.
5. Print the index and the item in the list using the second method discussed in class.
   - **Hint**: Use `range(len(vegetables_list))`.
6. Name one data structure that maintains the order of your list. Convert the object to this data type.
7. Name one data structure that does not maintain the order of your list. Convert the object to this data type.

#### B2. Conversion and Operations
8. Convert the list of your favorite vegetables into a tuple. 
9. Show the limitations of using a tuple by trying operations on them that will fail.
10. Convert the list of your favorite vegetables into a set.
11. Show the limitations of using a set by trying operations on them that will fail.
12. Demonstrate adding more values to your set.  
    - **Hint**: Use `dir` to see which methods you can call on your set.

#### B3. Membership Operator
13. Order the speed of using a membership operator in a set, list, and tuple. Explain why.  
    - **This is an explanation task and doesn’t require coding.**

14. Can we find the hash of a mutable object? Explain its relevance to the membership operator.  
    - **This is a quick one-liner task**.
15. Show me an example of how to find the hash of an immutable object.
16. Explain how hashing improves the "membership" operator (`in`).

#### B4. Nested Structures
17. Can a list contain a set? Explain why or why not.
18. Can a set contain a tuple? Explain why or why not.
19. Can a set contain another set? Explain why or why not.
20. Can a list contain another list? Explain why or why not.

---

### **Section C: Iterables vs Generators**

Total Questions: `2` * 2 (For explanation) * 3 (For Importance)

Total Marks: `12`


#### C1. Properties of Generators
1. Explain whether generators are iterable or not.
2. Can the membership operator (`in`) be performed on a generator? Show me an example of proving or disproving.

---

### **Section D: Dictionary Operations**

Total Questions: `1` * 2 (For explanation) * 2 (For Importance)

Total Marks: `4`

#### D1. Key Lookup
1. Write a function to return the key name of a dictionary given a value. Make sure to include doc string and type hinting.

---

### **Section E: Function Exercises**

Total Questions: `1` * 2 (For explanation) * 3 (For Importance)

Total Marks: `6`


#### E1. Simple Programs
1. Write a function that takes a series of single-digit numbers and returns their sum.
   - Use a for loop.
   - Use the `+=` operator.
   - Make sure to use `*args`. Explain how this works.

   e.g: 
   ```python
   sum_numbers(1, 2, 3, 4)
   sum_numbers(1, 2)
   ```

---

### **Section F: Control Flow Practice**

Total Questions: `3` * 2 (For explanation) 

Total Marks: `6`


#### F1. Basic Control Flow
1. Create a function to check if a number is positive, negative, or zero.
   - **Hint**: Use conditional statements (if, elif, else) to check the sign of the number.

#### F2. Loops and Tables
2. Write a loop to print a multiplication table for a number from 1 to 10.
3. Write a function that prints the multiplication table for all numbers from 1 to 20 (each number from 1 to 10).

---

### **Section G: List Manipulation**

Total Questions: `3` * 2 (For explanation) 

Total Marks: `6`


#### G1. List Operations
1. Create an unsorted list of integers from 1 to 8.
2. Add the number 9 to the unsorted list.
3. Print numbers in order not including the first and last index.  
   - **Hint**: Use `[1:-1]` for slicing.

---

### **Section H: Functions and Decorators**

Total Questions: `4` * 2 (For explanation) * 1.5 (Importance)

Total Marks: `12`


#### H1. Nested Functions
1. Write a function that defines another function inside it and uses a variable from the outer function in the inner one.  
   - Explain the concept of local and global variables through the code and examples (e.g., closure examples).

#### H2. Custom Decorators
2. Create a custom decorator that does not accept `*args`. Show how it fails when applied to a function that accepts parameters.
3. Update the custom decorator to accept `*args` and `**kwargs`.
4. Show two methods of applying decorators and explain which is better and why.

---

### **Section I: Comprehensions**

Total Questions: `3` * 2 (For explanation) 

Total Marks: `6`


#### I1. List and Set Comprehensions
1. Write a list comprehension to return odd numbers from a list of numbers from 1 to 10.
2. Write a set comprehension to remove duplicate letters from a string and print the unique characters.

#### I2. Dictionary Comprehension
3. Use a dictionary comprehension to create a dictionary where keys are numbers from 1 to 5 and values are their squares.

---

### **Section J: Dictionaries**

Total Questions: `5` * 2 (For explanation) 

Total Marks: `10`


#### J1. Nested Dictionaries and Grade Manipulation
1. Create a nested dictionary with student names as keys and another dictionary as values containing their grades.
2. Add a new subject and grade to one of the students' grades.

#### J2. Adding and Accessing Data
3. Show two methods for adding a new grade to a student’s record.
4. Demonstrate how to access a key in a dictionary that doesn't exist without throwing an error.

#### J3. Iterating Over Dictionaries
5. Write a function to iterate over a dictionary using `.items()` and print both keys and values.

---

### **Section K: Iterables and Recursion**

Total Questions: `1` * 2 (For explanation) * 3 (Importance)

Total Marks: `6`

#### K1. Recursive Functions
1. Write a recursive function to compute the nth Fibonacci number. Show me exactly how it works by adding print statements in the function and going over examples.

---

### **Hints for Section K1:**

1. **Understanding Fibonacci**:
   - The Fibonacci sequence is defined as:
     - `F(0) = 0`
     - `F(1) = 1`
     - For all other values: `F(n) = F(n-1) + F(n-2)`, where `n` is greater than 1.

2. **Base Cases**:
   - You need to define base cases for the recursion to stop:
     - If `n == 0`, return 0.
     - If `n == 1`, return 1.

3. **Recursive Step**:
   - For any number greater than 1, the Fibonacci number can be computed by recursively adding the previous two Fibonacci numbers: `F(n-1) + F(n-2)`.

4. **Suggested Structure**:
   ```python
   def fibonacci(n):
       # Base cases
       if n == 0:
           return 0
       elif n == 1:
           return 1
       else:
           # Recursive call for F(n-1) + F(n-2)
           return ____
   ```

---

### **Section L: Object-Oriented Programming (OOP)**

Total Questions: `2` * 2 (For explanation) 
Total Marks: `4`


#### L1. Basic OOP Concepts
1. List two properties of a class that are helpful while programming.
2. Explain whether an instance of a class is the same as an object.



### **Total Marks Calculation**

Here’s the table with only the **Total Questions** and **Total Marks** columns:

| Section  | Total Questions | Total Marks |
|----------|-----------------|-------------|
| Section A | 4               | 8           |
| Section B | 20              | 40          |
| Section C | 2               | 12          |
| Section D | 1               | 4           |
| Section E | 1               | 6           |
| Section F | 3               | 6           |
| Section G | 3               | 6           |
| Section H | 4               | 12          |
| Section I | 3               | 6           |
| Section J | 5               | 10          |
| Section K | 1               | 6           |
| Section L | 2               | 4           |

### **Total Questions: 49**  
### **Total Marks: 120**