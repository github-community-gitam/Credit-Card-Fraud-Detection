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
