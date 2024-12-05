### **Project Instructions: Build and Serve an End-to-End Machine Learning Pipeline**

---

#### **Goal**
The objective of this project is to implement an end-to-end machine learning workflow and serve a trained model through an API endpoint. You will be evaluated on the **rationale behind your decisions**, not on the model’s performance. Follow the steps outlined below and document your reasoning throughout.

---

### **Requirements**
1. **Dataset**:
   - Clearly explain how you obtained, cleaned, and split it.

---

### **Deliverables**

1. **EDA**:
   Visualize patterns/characteristics that our model is trying to learn.

   Objective: Advise on which models you should employ. 

   - Histograms
      - Variance
      - Average
      - Raw Values
   - Null counts
   - Correlation between features and target?
         - This is a good sign. This means you don't need complex non-linear models.
   - Correlations between features?
        - PCA
        - Multicollinearity:
             - VIF
             - Thresholds of correlation

2. **Training Pipeline**:
    This can either be an `.ipynb` file which produces your trained model or an `.py` file. It can include the following components (depending on your proposal in the assignment 3):
     - Data Preparation.
          - Filter out a small portion of raw data **not used in your train/test split** for endpoint testing. This is your **Out Of Sample** data that will be used for inference.
          - Produce a dataset that has all the processing required.
          - Null Imputation (If any)
          - Feature generation (if any) - Only applies to the training data
              - Arithmetic Operation
              - Non-Linear Operation
              - Sin/Cos etc. (_encoding_)
              - Binning and Clustering of values to define categories qcut()
              - Encoding (If any)

          - Train/Test/Split and Cross-validation, stratify.
     - Feature Selection (if any) - Only applied to the training data 
         - Feature importance on XGB using default hyperparams -> FI_X 
         - Feature importance on CatBoost using default hyperparams -> FI_C
         - Scaling both minmax(FI_X), minmax(FI_C). So now both features importances are scaled between 0 and 1.
         - You can take the average importance for each feature.
         - Top (50, 25, 10)
     - Select the right features from the dataset.
     - Modeling:
         - Hyperparameter Tuning / Cross 
            - Random Grid Search
         - Try new models. Benchmark.
         - Ensemble modeling.
         - Evaluating Performance (As defined in your assignment 3)
     - Save the trained model as a file (e.g., using `joblib` or `pickle` or `json`). Read more here: 
    https://scikit-learn.org/stable/model_persistence.html#model-persistence


3. **Functioning Model Serving in FastAPI**:
    This must be a FastAPI application that's working end to use. It must contain:
     - A clear endpoint for predictions (`/predict`).
     - Your app will load the persisted model from the training pipeline.
     - This endpoint will trigger a series of function and finally return the prediction the model

4. **Documentation**:
   - Include:
     - **Rationale** for each step (e.g., why you chose a specific feature, split ratio, model, etc.).
     - Explanation for skipped steps (if any) and their potential impact.
     - Instructions for running your code and testing the API locally.

5. **Demo**:
   - Record or perform a live demo.
   - Use your Out of Sample raw data as an input into the API.

5. **Explanation**:
   - Tell me why your model is good or bad.

---


### **Tips**
- Focus on simplicity. **Don’t overcomplicate the model or steps**.
- Ensure each step logically follows from the previous one.
- If you encounter challenges (e.g., missing data or unclear model results), document how you addressed or decided to skip them.
- Use FastAPI tutorials/documentation if you’re new to it. The focus is on showing how an end-to-end pipeline works, not on API optimization.



How should projects be managed in a team?

**AGILE:**
- Iteration. 
- Delivering modular components at a time.

