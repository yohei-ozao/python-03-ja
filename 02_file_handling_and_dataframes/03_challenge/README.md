## **Challenge 3: Iris Dataset Exploration and Feature Engineering with Pandas**

**Objective:** Deepen your understanding of data manipulation, feature engineering, and analysis using Pandas by exploring and enhancing the Iris dataset.

**Overview:**
The Iris dataset is a classic dataset used in machine learning and statistics. It consists of 150 observations of iris flowers, including measurements of sepal length, sepal width, petal length, and petal width, along with the species classification. The species include Iris Setosa, Iris Versicolour, and Iris Virginica.

**Tasks:**

1. **Data Loading and Overview:**
    - Load the Iris dataset into a DataFrame (instructions below).
    - Display the first 5 rows for an overview.
2. **Data Cleaning and Validation:**
    - Ensure there are no missing or null values.
    - Check data types of each column (e.g., numeric types for measurements).
3. **Basic Analysis and Descriptive Statistics:**
    - Compute basic descriptive statistics (mean, median, standard deviation) for each numeric feature.
    - Create a new DataFrame where each row corresponds to a feature and columns contain the calculated statistics. Output this as a CSV.
4. **Feature Engineering:**
    - Add a new column **`sepal_area`** calculated as sepal length × sepal width.
    - Add another column **`petal_area`** calculated as petal length × petal width.
    - Calculate descriptive statistics for these new features and add them to the statistics DataFrame.
5. **Filtering Data:** 
    1. Write a function to filter the data based on given criteria (e.g., filter out rows where a certain column's value is below a threshold).
6. **Export your data:**
    1. Save your dataframe as a CSV. 
    2. Although the output of this challenge will not be autograded, we request that you include your own dataframe when you push to github. 

### Loading the Iris Dataset

**Data Loading:**

- Install **`scikit-learn`** if it's not already installed, using **`!pip install scikit-learn`**.
- Load the Iris dataset from **`sklearn.datasets`**.

```python
# Import necessary libraries
import pandas as pd
from sklearn import datasets

# Load Iris dataset and convert to dataframe
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add the species column, numbers 0-2 each represent a different species
iris_df['species'] = iris.target
```

- Learn more about the dataset here:
    - https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html