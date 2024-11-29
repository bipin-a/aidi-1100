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
1. **Training Pipeline**:
    This can either be an `.ipynb` file which produces your trained model or an `.py` file. It can include the following components (depending on your proposal in the assignment 3):
     - Data Preparation.
          - Filter out a small portion of raw data **not used in your train/test split** for endpoint testing. This is your **Out Of Sample** data that will be used for inference.
          - Produce a dataset that has all the processing required. 
     - Feature generation (if any)
     - Feature Selection (if any)
     - Modeling:
         - Hyperparameter Tuning
         - Evaluating Performance (As defined in your assignment 3)
     - Save the trained model as a file (e.g., using `joblib` or `pickle` or `json`). Read more here: 
    https://scikit-learn.org/stable/model_persistence.html#model-persistence


2. **Functioning Model Serving in FastAPI**:
    This must be a FastAPI application that's working end to use. It must contain:
     - A clear endpoint for predictions (`/predict`).
     - Your app will load the persisted model from the training pipeline.
     - This endpoint will trigger a series of function and finally return the prediction the model

3. **Documentation**:
   - Include:
     - **Rationale** for each step (e.g., why you chose a specific feature, split ratio, model, etc.).
     - Explanation for skipped steps (if any) and their potential impact.
     - Instructions for running your code and testing the API locally.

4. **Demo**:
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
