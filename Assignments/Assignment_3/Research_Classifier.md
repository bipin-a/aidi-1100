## Task:

Binary Classification.

- You must select more than 2+ models to experiment with, and 1 basic model which will serve as a benchmark. 

## Dataset:

Note: In real world scenarios you usually query the data from a database using SQL. However for this assignment you won't be asked to write queries.

https://www.kaggle.com/datasets/fedesoriano/company-bankruptcy-prediction


### Additional Submission Requirements

- Summarize the decision for each key area.
- Explain your rationale under each decision. (No longer than 4 jot notes)
- Use Jot Notes! If you use paragraphs, I will not read it, and you **will get a 0.**
- Be concise, if you are making me read useless or redundant sentences, you will **lose** marks!
- Submit either a markdown file or a PDF file.
- If you'd like to do an EDA on the data, you can include screenshots.
- You must submit a 10 minute video to walk me through the rationale. 
- If you read word by word, you will lose marks!


### Key Decision-Making Areas for Independent Research

1. **Choosing the Initial Models**:
   - Research and select which models to the problem. 
   - Consider whether to begin with simpler models (e.g., Logistic Regression for interpretability) or more complex models (e.g., XGBoost, Random Forest, or CatBoost) that handle non-linear relationships.
   - Or do you want to do a supervised clustering approach, where high-hisk companies are grouped into clusters based on features? Why or why not?
   - Consider letting a simple model like Logistic Regression be a benchmark model. Explain why this is important.

2. **Data Pre-processing**:
   - Based on models you've selected, should the data be processed differently?
   - Think of any normalization/standardization or encodding techniques you may have to apply.
   - Explain the rationale.

3. **Handling Class Imbalance**:
   - Is there a class imbalance problem in this dataset?
   - Research the pros and cons of techniques like SMOTE, undersampling, and class weighting. What potential issues could it introduce?
   - Thoughts on adding more weights to certain samples during training time?
   - Explain whether you decided to apply one or more of these techniques and justify your approach.

4. **Outlier Detection and Treatment**:
   - Discuss the impact of outlier treatment on fraud detection performance, especially on minority (fraud) cases.
   - Treat outliers that represent errors, technical issues, or non-predictive noise, while preserving those that may contain valuable information related to fraud patterns or risky behaviors

5. **Addressing Sampling Bias**:
   - Consider using statistical tests (e.g. PSI Test and correlation) to determine if there’s a significant difference in feature distributions between the training and test sets.
   - Explain to me why we might want to do this.

6. **Data Normalization**:
   - Decide if data normalization should be applied manually (e.g., with StandardScaler or MinMaxScaler).
   - Does the model already handle it inherently? 
   - Research how normalization affects different models and explain your approach based on the specific models you chose.

7. **Testing for Normality**:
   - Explain whether normality is important for the models and techniques you’re using. If so, how would you address features that deviate significantly from normality?

8. **Dimensionality Reduction (PCA)**:
   - Consider whether to apply **Principal Component Analysis (PCA)** or another dimensionality reduction method.
   - Research the pros and cons of PCA. Could it help with overfitting, or might it obscure meaningful patterns in the data?
   - What is the threshold of improvement that you hope to achieve by applying PCA?

9. **Feature Engineering Choices**:
   - Could you possibly add more features to this dataset?
   - Or do you think this dataset has enough features and you don't need to make additional feature?

10. **Testing and Addressing Multicollinearity**:
   - Research methods to detect multicollinearity, such as Variance Inflation Factor (VIF) and correlation matrices.
   - How might multicollinearity impact your model’s performance or interpretability?
   - Explain if and how you addressed multicollinearity (e.g., feature selection, dimensionality reduction) and justify your approach.

12. **Feature Selection Methods**:
   - Research feature selection methods, such as:
        - correlation filtering
        - feature importance or the 'gain' in a model
        - the regularization terms of lasso and ridge regression
   - How many features are too many? How few are too few? What are the risks of each?
   - Select a feature selection approach, justifying why some features were retained or removed based on their relevance and impact on model performance.

13. **Hyperparameter Tuning Methods**:
   - Explore methods for hyperparameter tuning, including grid search, random search, and more advanced techniques like Bayesian Optimization or Hyperopt.
   - Select an approach that best fits your model complexity and computational resources. (You must apply this for your project)

14. **Cross-Validation Strategy**:
   - Consider the most appropriate cross-validation strategy for the problem, such as K-fold cross-validation or stratified K-fold.

15. **Evaluation Metrics Selection**:
   - Decide on the best evaluation metrics for this task.
   - Are you going the evaluate the results of a `predict(X)` or `predict_proba(X)` ?
   - Consider metrics like F1 score, ROC-AUC, precision-recall AUC, and Brier Score.
   - Explain the trade-offs of each metric and why you chose specific ones for this model.

16. **Evaluating Drift and Model Degradation**:
   - Research and apply methods to detect data drift and monitor model degradation over time. (hint: PSI)
   - Explain why tracking data drift is essential.


17. **Interpreting Model Results and Explainability**:
   - Consider methods for interpreting your model’s predictions, such as SHAP, LIME, or feature importance measures.
   - Select an interpretation method and explain how it helps to make the model’s predictions more understandable, especially in a regulatory context.

