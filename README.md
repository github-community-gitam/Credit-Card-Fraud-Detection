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

Selected models: Logistic Regression,Decision Tree,Random Forest,Support Vector Machine (SVM).

**Performance of Selected Models:**

**1)Logistic Regression**
* Training Set: Accuracy: 0.8833, Precision: 0.9368, Recall: 0.7393, F1-Score: 0.8264
* Validation Set: Accuracy: 0.8835, Precision: 0.9350, Recall: 0.7451, F1-Score: 0.8293
* Test Set: Accuracy: 0.8782, Precision: 0.9159, Recall: 0.7375, F1-Score: 0.8171

**Conclusion:** The Logistic Regression model demonstrates stable performance across all datasets, with accuracy ranging from 87.82% to 88.35%. Precision remains consistently high (~91-94%), indicating the model effectively identifies positive cases. However, recall (~74%) is slightly lower, suggesting some positive cases are missed. 

**2)Decision Tree**
* Training Set: Accuracy: 1.0000, Precision: 1.0000, Recall: 1.0000, F1-Score: 1.0000
* Validation Set: Accuracy: 0.9594, Precision: 0.9444, Recall: 0.9490, F1-Score: 0.9467
* Test Set: Accuracy: 0.9541, Precision: 0.9337, Recall: 0.9424, F1-Score: 0.9381
* Confusion Matrix:
[[1942   79]
 [  68 1113]]

Classification Report: 
| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
|   0   |   0.97    |  0.96  |   0.96   |  2021   |
|   1   |   0.93    |  0.94  |   0.94   |  1181   |
|       |           |        |          |         |
| **Accuracy**     |           |        |   0.95   |  3202   |
| **Macro Avg**    |   0.95    |  0.95  |   0.95   |  3202   |
| **Weighted Avg** |   0.95    |  0.95  |   0.95   |  3202   |


**Conclusion:** The Decision Tree model performs exceptionally, achieving perfect accuracy on the training set and high accuracy (~95%) on the validation and test sets. Its precision (~93-97%), recall (~94-96%), and F1-scores (~94-96%) indicate strong classification performance with minimal misclassification. This balance between fitting the training data and generalizing well on unseen data makes it one of the best-performing models.

**3)Random Forest**
 * Training Set: Accuracy: 0.9783, Precision: 0.9746, Recall: 0.9676, F1-Score: 0.9711
 * Validation Set: Accuracy: 0.9535, Precision: 0.9464, Recall: 0.9301, F1-Score: 0.9382
 * Test Set: Accuracy: 0.9528, Precision: 0.9455, Recall: 0.9255, F1-Score: 0.9354

**Conclusion:** The Random Forest model shows strong performance, achieving 97.83% accuracy on the training set and approximately 95.3% on both the validation and test sets. Its precision ranges from 94% to 97%, while recall is between 93% and 96%, resulting in F1-scores around 93% to 97%.However,The Decision Tree outperforms the Random Forest in training accuracy, achieving a perfect 100%, indicating it can capture complex patterns in the training data more effectively.

**4)Support Vector Machine (SVM)**
* Training Set: Accuracy: 0.8694, Precision: 0.9605, Recall: 0.6805, F1-Score: 0.7966
* Validation Set: Accuracy: 0.8694, Precision: 0.9597, Recall: 0.6850, F1-Score: 0.7994
* Test Set: Accuracy: 0.8729, Precision: 0.9521, Recall: 0.6901, F1-Score: 0.8002

**Conclusion:** The tuned Support Vector Machine (SVM) model achieves consistent accuracy (~86.9% on training and validation sets, 87.29% on the test set). Precision is high (~95-96%), while recall is lower (~68-69%), resulting in F1-scores around 79-80%. Overall, the model demonstrates solid performance but could improve in capturing more positive cases.


### Final Model Selection:
After comparing four models—Logistic Regression, Decision Tree, Random Forest, and Tuned Support Vector Machine (SVM)—we found that ***Decision Tree*** model is the best performer. It achieved perfect accuracy on the training set while maintaining high accuracy, precision, recall, and F1-scores on both validation and test sets. Overall, the Decision Tree's effective balance between fitting the data and generalization makes it the most reliable model for this dataset.
