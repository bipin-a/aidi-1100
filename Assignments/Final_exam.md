# Instructions:

1. The questions which do not have an `🔊 Verbal` mark can be skipped and not required to be covered in the verbal explaination. Otherwise, when marked with  `🔊 Verbal`, you must explain it.
2. Give all answers in jot notes. Keep it short. If you are too verbose, you will lose marks.



# Questions

1. List and Dictionary Operations

Given the following lists:

```python
name = ['alfred','brian','craig','alice',] 
age = [10,40,20,15]
```

a. Use the `zip()` function to iterate through both lists and print pairs of names and ages.

b. Convert the two lists into a dictionary using `zip()`, where names are keys and ages are values.

2. Function Decorators

a. What are two common use cases for function decorators in Python?   `🔊 Verbal`

b. Write a simple decorator that prints the name of the author as a message before the function is executed.

3. Generators vs. Lists

a. Why would you choose to use a generator over a list?  `🔊 Verbal`

b. Provide examples of creating generators using both the generator expression syntax and the `yield` keyword.

4. Hash Values, Sets, and Dictionaries

a. What is a hash in python? What does it have to do with mutability?  `🔊 Verbal`

b. Are both set and dictionary objects hashable? What constraint does a set have as it relates to hash? What constraint does a dictionary have as it relates to hash?  `🔊 Verbal`

5. Enhancing Code Readability

Name two Python language features that improve code readability by providing explicit documentation and information within function definitions. Explain why they are useful.

# Pandas

Given the following Pandas DataFrame:

```python
import pandas as pd
data = {'mixed_data': ['apple', '{"name": "Bob", "age": 25}', 'cherry', '{"country": "Canada"}']}
df = pd.DataFrame(data)
print(df)
```

Use the `.apply()` method to calculate the length of each element in the `mixed_data` column.

# EDA (Exploratory Data Analysis)

1. List two functions that can be used to visualize the distribution of features in a dataset.
2. What are two reasons why analyzing correlations between features and between features and the target variable is important in EDA?  `🔊 Verbal`

# Database

1. What are the key differences between OLAP and OLTP databases in terms of normalization, indexing, and functional purpose?  `🔊 Verbal`
2. If a SQL query is taking too long to execute, suggest two strategies to improve its performance. Explain how each strategy works.  `🔊 Verbal`
3. What is the difference between the `WHERE` and `HAVING` clauses in SQL?

# Model Training and Evaluation

1. How can you determine if a model is overfitting or underfitting? How does this information help in hyperparameter tuning?  `🔊 Verbal`
2. What are three techniques to address overfitting and three techniques to address underfitting?  `🔊 Verbal`
3. Why is the ROC-AUC metric often preferred over accuracy for classification problems?
4. What are the limitations of IQR, PCA, and SMOTE techniques as it applied to your forecasting or classification project?  `🔊 Verbal`

# Model Deployment

1. Which type of database (OLAP or OLTP) is typically used as the data source for production systems?

# Model Monitoring

1. Why is it important to monitor the Population Stability Index (PSI) of data in machine learning models? Provide a real-world example.  `🔊 Verbal`

# APIs and Networking

1. On which layer of the TCP/IP model are FASTAPI applications typically built and deployed?
2. Explain the difference between GET and POST HTTP requests and their common use cases.
3. What are the three main components of a URL endpoint?



There are **20 questions** in total. Here's the breakdown by section:

- **Python**: 5 questions  
- **Pandas**: 1 question  
- **EDA**: 2 questions  
- **Database**: 3 questions  
- **Model Training & Model Evaluation**: 4 questions  
- **Model Deployment**: 1 question  
- **Model Monitoring**: 1 question  
- **APIs & Networking**: 3 questions