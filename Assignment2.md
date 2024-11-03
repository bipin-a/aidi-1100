# Assignment 2


### **Expectations**

1. **Submission Requirements**:
   - You must submit a **.ipynb file** with all your solutions.
   - Along with the notebook, submit a **recording** where you explain your solutions. 
     - The recording **must include your voice and face** (use your webcam).
   
2. **Solution Explanations**:
   - For **each question**, provide an explanation of your solution.
   - Use your **judgment** to determine how detailed the explanation should be based on the complexity of the question.
   - Explain the what, why and how. 
   
3. **Markdown Explanations**:
   - Write a **basic explanation** of each solution in a **Markdown cell** below the code.
   - Use **bullet points** or **jot notes**. Keep it brief and clear. 
   - **Do not write paragraphs**. The explanation is meant to help guide your verbal explanation in the recording.
   - Do **not** read word to word

4. **Recording Expectations**:
   - During your recording, use the Markdown notes as a reference to explain the code verbally.
   - Make sure you **verbally explain** the logic behind your code as you walk through each solution.
  
5. **Open Book**:
    - While this assignment may seem extensive, remember that it’s open book. Most of the material is already covered in the notebook I’ve provided, which includes working code, examples, and detailed narration in markdown cells.

**Important Note**: If I notice excessive overlap between solutions submitted by different individuals, both assignments will be given a score of 0. Please ensure that all work is your own.

---

### Learnings from Assignment 1 Submissions:

- Missing Submission Requirements (Future Assignments that not not meet criteria will receive 0%)
- Explanations Not Submitted
- Missing Screen Recordings
- Webcam Disabled
- .ipynb File Not Submitted
- Access to Video Not Granted
- Wrong Files Uploaded
- Audio Too Quiet
- .rar compression instead of .zip
- Reading word by word off a script! More time spent reading markdown notes than reviewing code.
- Blocks of code instead of having them split into different cells.
- Contradictory comments to code to what is verbalized.
- Complex type hints were used but not explained.
- Inadequate explanations.


---

### Dataset Loading and Initial Validation

1. **Download and Validate Datatypes**:
   - Download the `taxis` dataset from Seaborn. `sns.load_dataset`
   - Validate that the `pickup` and `dropoff` columns are of datetime type.
   
2. **Calculate Trip Duration**:
   - Compute the time it took for each ride using the `pickup` and `dropoff` columns.
   - hint: `data.dt.total_seconds() / 60` gives you total minutes. Convert seconds to hours


3. **Calculate Dollar Metrics**:
   - Calculate `$ per hour` earned for each ride. hint: maths
   - Calculate `$ per km` for each ride. hint: maths

4. **Correlations**:
   - Show the correlation between `color` and `$ per hour`.
   - Show the correlation between `passengers` and `$ per hour`.
   - Show the correlation between `pickup_borough` and `$ per km`.
   - Rationalize the results? What is the strongest theoretical correlation possible and weakest? 

### Visualizations

5. **Distribution Plots**:
   - Plot the distribution of `$ per hour` and `$ per km` using two visualizations:
     - Two subplots placed side by side.
     - One subplot overlaying the distributions on each other.
     - Make sure I can see the distributions. Don't make a silly mistake with yaxis here.

### Synthetic Column Creation and Currency Normalization

6. **Create a Synthetic Currency Column**:
   - Create a new column `currency` which chooses between `GBP`,`USD`,`EUR`,`MXN`,`AUD` using `random.choice`.
   - Hint: Do this in a list comp where `i in range(len(taxis_df))`
   
7. **Normalize Currency to CAD**:
   - Normalize the currency to CAD using any of the following strategies:
     - `apply`
     - `lambda`
     - `iterrows`
   - Do not apply a bad solution.
  
    **note**: You will not be using this normalized amount in later questions. For all references to total, use the original `total` from the dataset.

### Date Extraction

8. **Extract Date Components**:
   - Create a column named `date` with components `year`, `month`, and `day` extracted from `pickup`.

### Pivot Tables

9. **Pivot for Sum by Multiple Columns**:
   - Create a pivot table to show the total sum grouped by  `date`, `color`, `passengers`, `pickup_borough`, and `dropoff_borough`. 

10. **Pivot for Average Dollar per Hour by Multiple Columns**:
   - Create a pivot table to show the average `$ per hour` grouped by `date`, `color`, `pickup_borough`, and `dropoff_borough`.
   - Assign this table to `taxis_dollar_hr_rate`.

11. **Reverse Pivot Table**:
   - Tell me if `taxis_dollar_hr_rate` can be reversed back to the original `taxis` dataframe.
   - Can `melt` be used, such that all information is `taxis` maintained?

### Time Series Analysis

12. **Sum Dollar per Day**:
   - Using `resample` or `groupby` by daily frequency, compute the total dollar amount per day, and rename this series `time_series`.

13. **Check for Missing Days**:
   - Ensure no missing days between each entry in `time_series`, using one way to verify this (e.g., `reset_index` followed by `.diff`).
   - Report if there are any missing days.

14. **Line Plot**:
   - Plot `time_series` as a line plot.

### Groupby vs. Pivot Explanation

15. **Explain Groupby vs. Pivot**:
   - Explain how `groupby` differs from `pivot`.

### Calculus Operations on Time Series

16. **Derivative and Integral**:
   - Compute the derivative and integral of the `time_series`.

### Regression and Prediction

17. **Fit Regression Models**:
   - Fit both linear and logistic regression model on univariate data without splitting data.
   - Forecast the next `15` days of total amounts. 
   - Set the predictions as new columns in `time_series`.

18. **Prediction Plot**:
   - Plot the true values and predictions in a single plot using:
     - Black for actual data
     - Red for linear regression
     - Blue for logistic regression
     - Label the axis, title, add legend etc.

19. **Error Calculations**:
   - Calculate **L1 Error** for each prediction and add it as a new column (`l1norm = truth - prediction`).
   - Calculate **L2 Error** for each prediction and add it as a new column (`l2norm = (truth - prediction)^2`).


20. **Scatter Plot of Predicted vs. L1 Error**:
   - Create a scatter plot with predicted values (x-axis) and L1 error (y-axis) for the linear model.
   - Discuss what this plot indicates about heteroskedasticity.

### Autocorrelation Analysis

21. **Autocorrelation for Lags**:
   - Compute autocorrelation values for lags from 1 to 8 for `time_series`. Be smart, use a loop or list comp.
   - Identify the lag with the strongest and weakest autocorrelation. Rationalize the results.

### Model Training on Entire Dataset

22. **Train on Entire Dataset**:
   - Explain if it's ok to ever train a model on the entire dataset. Why or why not?


### SQL:
run: `pip install -q duckdb-engine duckdb` 

Convert the original `taxis` dataframe from seaborn into a duckdb table. Use `duckdb.register`

23. Write a query to return the third largest total from the entire table using both `row_number` and common table expression together.
24. Do the same as above, but this time use `dense_rank` instead of `row_number` and explain the difference.
25. Tell me the sum total for each `pickup_borough` call it `pickup_borough_sum_total`. Filter for `pickup_borough_sum_total` > 10
26. Filter for `total` > 10 then do sum total for each `pickup_borough` call it `pickup_borough_sum_total`.
27. Explain the difference between the last 2 queries.
28. In a single query get, sum total, average total, min total, sum distance, max distance for each combination of pickup_borough and color. Hint: you'll need to group by 2 fields here.