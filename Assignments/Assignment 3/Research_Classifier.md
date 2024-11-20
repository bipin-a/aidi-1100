### Key Decision-Making Areas for Independent Research

1. **Choosing the Initial Models**:
   - Research and select which models to start with for the fraud detection problem.
   - Consider whether to begin with simpler models (e.g., Logistic Regression for interpretability) or more complex models (e.g., XGBoost, Random Forest, or CatBoost) that handle non-linear relationships.
   - Consider letting a simple model like Logistic Regression be a benchmark model. Explain why this is important.
   - Justify your model choices and establish a baseline for comparison.

2. **Handling Class Imbalance**:
   - Research the pros and cons of techniques like SMOTE, undersampling, and class weighting. What potential issues could it introduce?
   - Explain whether you decided to apply one or more of these techniques and justify your approach.

3. **Outlier Detection and Treatment**:
   - Discuss the impact of outlier treatment on fraud detection performance, especially on minority (fraud) cases.
   - Treat outliers that represent errors, technical issues, or non-predictive noise, while preserving those that may contain valuable information related to fraud patterns or risky behaviors

4. **Addressing Sampling Bias**:
   - Consider using statistical tests (e.g. PSI Test and correlation) to determine if there’s a significant difference in feature distributions between the training and test sets.

5. **Data Normalization**:
   - Decide if data normalization should be applied manually (e.g., with StandardScaler or MinMaxScaler) or if model-specific handling is sufficient.
   - Research how normalization affects different models and explain your approach based on the specific models you chose.

6. **Testing for Normality**:
   - Explain whether normality is important for the models and techniques you’re using. If so, how would you address features that deviate significantly from normality?

7. **Dimensionality Reduction (PCA)**:
   - Consider whether to apply **Principal Component Analysis (PCA)** or another dimensionality reduction method.
   - Research the pros and cons of PCA in fraud detection. Could it help with overfitting, or might it obscure meaningful patterns in the data?
   - Determine if PCA improves model performance or interpretability, and justify your choice to use or not use it.

8. **Feature Engineering Choices**:
   - Propose and create additional features that could improve fraud detection accuracy.
   - Could you possibly add more features to this dataset, such as prime interest rates for that month?
   - Consider features that might reveal transaction patterns, periodic behaviors, or statistical aggregations.

9. **Feature Selection Methods**:
   - Research feature selection methods, such as correlation filtering, or feature importance 'gain' in a model.
   - How many features are too many? How few are too few? What are the risks of each?
   - Select a feature selection approach, justifying why some features were retained or removed based on their relevance and impact on model performance.

10. **Testing and Addressing Multicollinearity**:
   - Research methods to detect multicollinearity, such as Variance Inflation Factor (VIF) and correlation matrices.
   - How might multicollinearity impact your model’s performance or interpretability?
   - Explain if and how you addressed multicollinearity (e.g., feature selection, dimensionality reduction) and justify your approach.

11. **Hyperparameter Tuning Methods**:
   - Explore methods for hyperparameter tuning, including grid search, random search, and more advanced techniques like Bayesian Optimization or Hyperopt.
   - Select an approach that best fits your model complexity and computational resources. (You must apply this for your project)

12. **Cross-Validation Strategy**:
   - Consider the most appropriate cross-validation strategy for the fraud detection problem, such as K-fold cross-validation or stratified K-fold.
   - Does the imbalanced nature of fraud detection require special considerations in cross-validation? Explain your approach and any special handling required.

13. **Evaluation Metrics Selection**:
   - Decide on the best evaluation metrics for this task, particularly with regard to balancing false negatives and false positives.
   - Consider metrics like F1 score, ROC-AUC, precision-recall AUC, and Brier Score.
   - Explain the trade-offs of each metric and why you chose specific ones for this fraud detection model.

14. **Evaluating Drift and Model Degradation**:
   - Research and apply methods to detect data drift and monitor model degradation over time.
   - Beyond using PSI, explore other drift measures, such as Jensen-Shannon divergence or KL divergence.
   - Explain why tracking data drift is essential in a dynamic fraud detection environment.


15. **Interpreting Model Results and Explainability**:
   - Consider methods for interpreting your model’s predictions, such as SHAP, LIME, or feature importance measures.
   - Select an interpretation method and explain how it helps to make the model’s predictions more understandable, especially in a regulatory context.

---

### Additional Submission Requirements

- **Research Justification Document**:
   - Summarize your research and decision-making for each key area (model selection, class imbalance handling, feature engineering, etc.).
   - Document the findings that informed your decisions and how they impacted the overall modeling approach.

- **Comparison of Approaches**:
   - For areas with multiple valid approaches (e.g., handling class imbalance, feature selection), compare at least two methods and discuss their impact on performance.
