# Credit-Card-Fraud-Detection

### Overview:
  The project aims to build an end-to-end system for detecting fraudulent credit card transactions. The solution will involve collecting and preprocessing transaction data, applying machine learning algorithms for fraud detection, and developing a web-based interface for users. The final product will be deployed using a Flask back-end and MongoDB for data storage.

## Data Preprocessing for Credit Card Fraud Detection

### Dataset Information
- **Source:** The dataset contains simulated credit card transaction data from 1,000 customers and 800 merchants, spanning the period from January 1, 2019, to December 31, 2020. This data was generated using the Sparkov Data Generation Tool and accessed from Kaggle.
- **Details:** The dataset consists of legitimate and fraudulent transactions, simulating real-world class imbalance in fraud detection.
- **Dataset Link:** [Fraud Detection Dataset on Kaggle](https://www.kaggle.com/datasets/kartik2112/fraud-detection)

### Data Collection
- Accessed the dataset from Kaggle.
- Loaded it into the workspace for further processing.

### Data Cleaning
- Removed duplicate records (if any).
- Handled missing values (if any).
- Identified and corrected data inconsistencies.

### Feature Engineering
- **Transaction Time Features:** Extracted new features such as the day of the week and hour of the day from the transaction timestamp to capture temporal patterns in fraudulent behavior.
- **Transaction Amount Scaling:** Scaled the Amount feature for consistency and better model performance.
- **Transaction Frequency Features:** Created features to measure the frequency of transactions for each customer and merchant.
- **Label Encoding:** Employed Label Encoding to convert categorical variables into a numerical format, making them suitable for machine learning algorithms.

### Data Normalization
- Applied Standard Scaler to ensure uniformity across numerical features, centering them around zero with a standard deviation of one, which is essential for model training.

The dataset has been cleaned, transformed, and enriched with engineered features. This comprehensive preprocessing lays the groundwork for further analysis, including Exploratory Data Analysis (EDA), which will provide insights into transaction behaviors and highlight patterns relevant to fraud detection.

## Data Visualization and analysis
Focuses on visualizing the dataset to uncover insights into transaction behaviors, identify patterns related to fraud, and understand the distribution of features.

### Visualization Techniques Used

- **Histograms:** To visualize the distribution of transaction amounts and identify outliers.
- **Box Plots:** To examine the spread and identify potential anomalies in transaction amounts across different classes (legitimate vs. fraudulent).
- **Heatmaps:** To visualize correlations between features, helping to identify which features are most relevant for fraud detection.
- **Scatter Plots:** To analyze relationships between features, such as transaction amount versus transaction time.

### Key Visualizations
- **Transaction Amount Distribution:**
A histogram showing the distribution of transaction amounts helps to identify skewness and outliers.
- **Box Plot of Transaction Amounts by Class:**
A box plot comparing legitimate and fraudulent transactions reveals differences in transaction amounts.
- **Correlation Heatmap:**
A heatmap illustrating feature correlations helps to identify which features are strongly correlated with fraud.
- **Scatter Plot of Amount vs. Time:**
A scatter plot to visualize how transaction amounts vary over time can help identify trends or patterns.
- **Transaction Amount vs Fraud:**
A bar chart comparing transaction amounts across fraudulent and non-fraudulent transactions.
- **Transaction Frequency by Time:**
A line plot showing transaction frequency at different times of the day to identify any patterns related to fraud.
- **Fraud by Region:**
A heatmap displaying the concentration of fraudulent transactions across different regions.
- **Age Group Distribution:**
A histogram showing the distribution of age groups and their association with fraud.
- **Gender and Fraud:**
A pie chart visualizing the proportion of fraudulent transactions across different genders.

### Insights Gained
- The visualizations revealed that fraudulent transactions tend to have lower amounts compared to legitimate ones.
- Certain features exhibited strong correlations with fraud detection, guiding feature selection for model training.
- Temporal patterns were identified, indicating specific times when fraudulent activities were more prevalent.

## Model Selection and Algorithm Testing

Selected models: Logistic Regression,Decision Tree,Random Forest,Support Vector Machine (SVM), 

**Performance of Selected Models:**

**Logistic Regression**
Accuracy: 0.9939
Precision: 0.0
Recall: 0.0
F1-Score: 0.0

**Conclusion:** Although the accuracy was fairly high (99.39%), the model failed to identify any positive cases correctly, as shown by the precision, recall, and F1-score all being 0. This makes it an unreliable choice.

**Decision Tree**
Accuracy: 0.9970
Precision: 0.7246
Recall: 0.7595
F1-Score: 0.7416

**Conclusion:** The Decision Tree had good accuracy (99.70%) and decent precision (72.46%) and recall (75.95%). However, it was not as precise as Random Forest, meaning it made more incorrect positive predictions, making it a slightly less accurate option.

**Random Forest**
Accuracy: 0.9982
Precision: 0.9318
Recall: 0.7290
F1-Score: 0.8181

**Conclusion:** The Random Forest model showed the best results, with the highest accuracy (99.82%) and strong precision (93.18%) and F1-score (81.81%). It made fewer mistakes and gave the most reliable predictions, making it the best choice.

**Support Vector Machine (SVM) (Tuned)**
Accuracy: 0.9936
Precision: 0.0
Recall: 0.0

**Conclusion:** Despite the high accuracy (99.36%), the SVM model performed poorly in precision, recall, and F1-score (all 0). Like Logistic Regression, it failed to correctly identify positive cases, which makes it unsuitable for this task.


### Final Model Selection
We **selected the Random Forest model as the best** because it had the highest accuracy (99.82%) and performed well across all evaluation metrics. Its precision (93.18%) and F1-score (81.81%) show that it makes more correct predictions and handles both positive and negative outcomes better than the other models.
