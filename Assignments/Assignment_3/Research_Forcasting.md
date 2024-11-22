## Task:

Time Series Forecasting

- You must select more than 2+ models to experiment with, and 1 basic model which will serve as a benchmark. 

## Dataset:

Note: In real world scenarios you usually query the data from a database using SQL. However for this assignment you won't be asked to write queries.

https://huggingface.co/datasets/autogluon/chronos_datasets

### Additional Submission Requirements

- Summarize the decision for each key area (model selection, class imbalance handling, feature engineering, etc.).
- Explain your rationale under each decision. (No longer than 4 jot notes)
- Use Jot Notes! If you use paragraphs, I will not read it, and you **will get a 0.**
- Be concise, if you are making me read useless or redundant sentences, you will **lose** marks!
- Submit either a markdown file or a PDF file.
- If you'd like to do an EDA on the data, you can include screenshots.
- You must submit a 10 minute video to walk me through the rationale. 
- If you read word by word, you will lose marks!


### Key Decision-Making Areas for Independent Research

1. **Choosing Initial Models**:
   - Research and select models to start with for the forecasting problem, considering both simpler models (e.g., ARIMA, Exponential Smoothing) and more complex models (e.g., Prophet, LSTM, XGBoost Regressor).
   - Consider using a simple statistical model (e.g., ARIMA) as a benchmark. Explain why having a benchmark model is useful in forecasting.
   - Justify your model choices and establish a baseline for comparison.

2. **Data Pre-processing**:
   - Based on models you've selected, should the data be processed differently?
   - Think of any normalization/standardization or encodding techniques you may have to apply.
   - Do you need to handling seasonality and trends? (i.e  LSTM performs better when you detrend the input) )
   - Explain the rationale.

3. **Outlier Detection and Treatment**:
   - Identify and analyze outliers in the sales data. Are there certain outliers (e.g., holiday sales peaks, one-off events) that should be preserved or treated differently?
   - Discuss the impact of outlier treatment on forecasting performance and justify your approach to handling these anomalies.

4. **Addressing Data Gaps or Missing Values**:
   - Explore techniques for handling missing values in time series, such as interpolation, forward/backward filling, or using model-based approaches.
   - Explain whether your chosen approach could affect forecast accuracy, especially around critical dates (e.g., holiday periods or weekends).

5. **Testing for Stationarity**:
   - Research stationarity testing methods like the Augmented Dickey-Fuller (ADF) test and KPSS test to assess if the series is stationary.
   - If the data is non-stationary, discuss techniques for differencing or transformation. Justify whether stationarity adjustments improve model performance.

6. **Feature Engineering for Time Series**:
   - Propose additional features, such as day of the week, month, holidays, or lagged sales data.
   - Consider aggregations or rolling features (e.g., moving averages, rolling sums) to capture recent trends. Justify how these features could help improve forecasting accuracy.
   - Should you use auto-correlation features here?

7. **Feature Selection Methods**:
   - Research feature selection methods like recursive feature elimination (RFE) or model-based selection (e.g., feature importance from XGBoost or Random Forest).
   - How many features are too many? How few are too few? Discuss the risks of overloading the model with features versus missing valuable predictors.
   - Select and justify a feature selection approach, highlighting its impact on forecast accuracy.

8. **Hyperparameter Tuning Methods**:
   - Explore hyperparameter tuning methods (e.g., grid search, random search, Bayesian Optimization) and select one that suits your model complexity and computational resources.
   - Apply this method to improve your forecasting model and document the results.

9. **Cross-Validation Strategy for Time Series**:
   - Research cross-validation techniques appropriate for time series (e.g., rolling-window, expanding-window validation).
   - Explain why traditional K-fold cross-validation isn’t suitable for time series and justify your chosen approach.

10. **Evaluation Metrics Selection**:
   - Choose evaluation metrics that reflect forecasting accuracy, such as Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), Mean Absolute Percentage Error (MAPE), and Symmetric Mean Absolute Percentage Error (SMAPE).
   - Discuss the trade-offs of each metric and why you selected specific ones for evaluating your forecasting model’s performance.

11. **Handling Seasonality and Long-term Trends in Drift Monitoring**:
   - Research methods to monitor and detect changes in seasonality or trends in the forecasted data over time.
   - Beyond using metrics like MAPE, explore using drift detection methods (e.g., PSI or rolling-window analysis) to assess if new data deviates from past patterns.

12. **Interpreting Forecasting Results and Explainability**:
   - Consider methods for interpreting your model’s predictions, such as SHAP for feature importance in tree-based models or coefficients in linear models.
   - Explain how feature importance and trend interpretation can support business decisions, especially in a sales context where seasonality and trends are critical.

