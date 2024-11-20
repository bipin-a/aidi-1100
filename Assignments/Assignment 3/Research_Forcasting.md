### Forecasting ML Problem: Sales Forecasting Assignment

#### Objective
This assignment mirrors the decision-making approach needed in a real-world time series forecasting problem. Students will predict daily sales for a retail company using historical sales data, focusing on data preparation, feature engineering, model selection, evaluation, and long-term monitoring.

---

### Part 1: Sales Forecasting Problem
#### Dataset: [Retail Sales Dataset (or any time series dataset with date, sales, and product features)]

1. **Forecasting Task**:
   - **Objective**: Forecast daily sales for the next 30 days based on historical sales data.
   - **Preprocessing**:
     - **Classify and handle time series features** like date, seasonality, trends, and potential outliers in sales data.
     - **Normalize and transform** features if needed, focusing on strategies to handle time series data effectively.
     - **Split the dataset** into training, validation, and test sets, considering seasonal patterns or specific time-based splits for realistic evaluation.

---

### Key Decision-Making Areas for Independent Research

1. **Choosing Initial Models**:
   - Research and select models to start with for the forecasting problem, considering both simpler models (e.g., ARIMA, Exponential Smoothing) and more complex models (e.g., Prophet, LSTM, XGBoost Regressor).
   - Consider using a simple statistical model (e.g., ARIMA) as a benchmark. Explain why having a benchmark model is useful in forecasting.
   - Justify your model choices and establish a baseline for comparison.

2. **Handling Seasonality and Trends**:
   - Research approaches for handling seasonality and trends in time series data. Should these be extracted and adjusted manually, or left for the model to capture?
   - Consider decomposing the time series into trend, seasonality, and residuals using techniques like STL decomposition. How might this influence your modeling approach?

3. **Outlier Detection and Treatment**:
   - Identify and analyze outliers in the sales data. Are there certain outliers (e.g., holiday sales peaks, one-off events) that should be preserved or treated differently?
   - Discuss the impact of outlier treatment on forecasting performance and justify your approach to handling these anomalies.

4. **Addressing Data Gaps or Missing Values**:
   - Explore techniques for handling missing values in time series, such as interpolation, forward/backward filling, or using model-based approaches.
   - Explain whether your chosen approach could affect forecast accuracy, especially around critical dates (e.g., holiday periods or weekends).

5. **Data Normalization and Transformation**:
   - Consider whether data normalization (e.g., MinMaxScaler, StandardScaler) or transformations (e.g., log, differencing) are appropriate for your chosen models.
   - Explain how these choices impact model performance and stability, particularly for time series data with seasonality and trends.

6. **Testing for Stationarity**:
   - Research stationarity testing methods like the Augmented Dickey-Fuller (ADF) test and KPSS test to assess if the series is stationary.
   - If the data is non-stationary, discuss techniques for differencing or transformation. Justify whether stationarity adjustments improve model performance.

7. **Feature Engineering for Time Series**:
   - Propose additional features, such as day of the week, month, holidays, or lagged sales data.
   - Consider aggregations or rolling features (e.g., moving averages, rolling sums) to capture recent trends. Justify how these features could help improve forecasting accuracy.

8. **Feature Selection Methods**:
   - Research feature selection methods like recursive feature elimination (RFE) or model-based selection (e.g., feature importance from XGBoost or Random Forest).
   - How many features are too many? How few are too few? Discuss the risks of overloading the model with features versus missing valuable predictors.
   - Select and justify a feature selection approach, highlighting its impact on forecast accuracy.

9. **Hyperparameter Tuning Methods**:
   - Explore hyperparameter tuning methods (e.g., grid search, random search, Bayesian Optimization) and select one that suits your model complexity and computational resources.
   - Apply this method to improve your forecasting model and document the results.

10. **Cross-Validation Strategy for Time Series**:
   - Research cross-validation techniques appropriate for time series (e.g., rolling-window, expanding-window validation).
   - Explain why traditional K-fold cross-validation isn’t suitable for time series and justify your chosen approach.

11. **Evaluation Metrics Selection**:
   - Choose evaluation metrics that reflect forecasting accuracy, such as Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), Mean Absolute Percentage Error (MAPE), and Symmetric Mean Absolute Percentage Error (SMAPE).
   - Discuss the trade-offs of each metric and why you selected specific ones for evaluating your forecasting model’s performance.

12. **Handling Seasonality and Long-term Trends in Drift Monitoring**:
   - Research methods to monitor and detect changes in seasonality or trends in the forecasted data over time.
   - Beyond using metrics like MAPE, explore using drift detection methods (e.g., PSI or rolling-window analysis) to assess if new data deviates from past patterns.

13. **Interpreting Forecasting Results and Explainability**:
   - Consider methods for interpreting your model’s predictions, such as SHAP for feature importance in tree-based models or coefficients in linear models.
   - Explain how feature importance and trend interpretation can support business decisions, especially in a sales context where seasonality and trends are critical.

---

### Additional Submission Requirements

- **Research Justification Document**:
   - Summarize your research and decision-making for each key area (model selection, handling seasonality, feature engineering, etc.).
   - Document the findings that informed your decisions and how they impacted your modeling approach.

- **Comparison of Approaches**:
   - For areas with multiple valid approaches (e.g., seasonality handling, feature selection), compare at least two methods and discuss their impact on performance.



                                                                             TODO:
                                                                              ADd regressor