# 📊 Product Sales Prediction System using Machine Learning

An **end-to-end Machine Learning project** that predicts the **profit percentage of a product** in a given area and classifies whether the product will yield **Profit or Loss**.  
This system helps clients evaluate the feasibility of setting up a business in a specific region with chosen products.  

---

## 🚀 Project Overview  

- **Inspiration Point**:  
  Clients often lack knowledge of expected profit margins in specific regions before starting a business.  
- **Existing System**:  
  Businesses choose areas and products with little predictive insight, leading to possible loss.  
- **Proposed System**:  
  A prediction model capable of forecasting **profit percentage** and classifying products as **Profit/Loss**, guiding clients to make informed business decisions.  

---

## 🛠️ Business Use Case  

The system:  
- Predicts the **profit rate** for a product in a particular area.  
- Helps clients avoid **time loss and financial risk**.  
- Assists in choosing the **right product-location combination** for better success.  

---

## 📂 Dataset  

**Features Used:**  
- Area  
- Usage product  
- Number of people having product requirement  
- Number of competitors in that area  
- Purchase rate  
- Market margin rate  
- Self margin rate  
- Service  

**Target Variables:**  
- **Profit Percentage (Continuous)** → Forecasted using **Multiple Linear Regression**  
- **Profit/Loss (Categorical)** → Classified using **Naive Bayes**  

**Observations:**  
- Profit rate increases as client’s margin rate rises.  
- When margin rate is in the range of **20–30**, profit rate exceeds **200**.  

---

## 🧠 Models & Approach  

- **Multiple Linear Regression** → For predicting the **profit percentage**  
- **Naive Bayes** → For classifying **Profit/Loss**  

**Evaluation:**  
- Models were tested and validated for accuracy.  
- Results showed **good predictive power** for both regression and classification tasks.  

---

## 📈 Results  

- **Multiple Linear Regression**: Effectively predicts profit percentage.  
- **Naive Bayes**: Accurately classifies products into Profit/Loss categories.  
- Achieved reliable accuracy with tested algorithms.  

---

## 🖥️ Tech Stack  

- **Python**  
- **Scikit-learn** (ML Algorithms)  
- **Pandas, NumPy** (Data Processing)  
- **Matplotlib, Seaborn** (Visualization)  
- **Jupyter Notebook** (Experiments & Analysis)  

---

## 📊 Workflow  

1. Load dataset  
2. Perform **data preprocessing** (handle missing values, encoding, scaling)  
3. Train models:  
   - Multiple Linear Regression  
   - Naive Bayes  
4. Evaluate performance (accuracy, error metrics)  
5. Generate predictions:  
   - Profit percentage (numeric)  
   - Profit/Loss (categorical)  

---

## 📷 Screenshots  
**Observations**  
![Observations](https://github.com/devathisrija/Product-sales-prediction-using-machine-learning/blob/main/screenshots/Screenshot%20(695).png)

**Results**
![Results](https://github.com/devathisrija/Product-sales-prediction-using-machine-learning/blob/main/screenshots/Screenshot%20(696).png)

**Results**
![Results](https://github.com/devathisrija/Product-sales-prediction-using-machine-learning/blob/main/screenshots/Screenshot%20(697).png)

---

## 🔮 Future Improvements  

- Try more advanced ML models (Random Forest, XGBoost, Neural Networks).  
- Deploy as a **Flask Web App** for real-time predictions.  
- Add a **dashboard** to visualize predictions interactively.  

---

## 👤 Author  

**Devathi Srija**  
- 🎓 CSE C  
- 📧 Email: srijadevathi@gmail.com 


---
