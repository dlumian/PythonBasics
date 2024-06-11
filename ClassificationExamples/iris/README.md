# Iris Classification
Introduction to classification with iris dataset. This dataset is built into sklearn allowing for data to be loaded from package instead of a file.

Example can be run as a [script](./src/main.py) or [notebooks](./notebooks/). See [primary readme](./../../README.md) for details on how to run either option.

**NOTE:** Notebooks are short by design to highlight saving and loading data. Notebook version also includes more EDA and visuals.

## Goal

Showcase classification with sklearn, including visualizing results, comparing models, and storing data. 

## Directory Structure
### Initial setup:
- **notebooks:** 5 numbered notebooks to be run in order
- **README.md:** this file
- **src:** script version of example [main.py](./src/main.py)

### Generated content
- **clf_results:** for each model, stores confusion matrix and metrics
- **data:** csv files of raw data and data partitioned for train-test split
- **images:** holds copies of all model confusion matrices for quicker comparison
- **models:** pickle files of each model so training and evaluation can happen in different steps

#### NOTE: Content is not automatically removed and will be overwritten if running multiple times. To reset example, move or remove all of the directories listed under `Generated content`.

## Notebooks Overview

The notebooks for this example are numbered and must be run in order. 

**1_Generate_Data**

    * Imports data from sklearn
    * Converts datatype to pandas df
    * Creates a new directory
    * Saves data to csv files in 'data' dir

**2_Train_Test_Split**

    * Imports data using pandas from csv
    * Uses sklearn train-test split to create training and test datasets
    * Saves split data back into csvs for next step

**3_EDA**

    * Imports training data only to conduct exploratory data analysis (EDA)
    * Visualizes data with seaborn pairplot
    * Defines a function to explore column level data including number of unique values and value counts

**4_Train_Models**

    * Trains two models on training data
        * Random Forest Classifier
        * Logistic Regression
    * Saves models using joblib to pickle file

**5_Predict_and_Evaluate**

    * Loads trained models and test data
    * Runs predictions on test data
    * Evaluates performance by:
        * Visualizing confusion matrices
        * Calculating accuracy
        * Generating other metrics with a classification report

## Script Version

The script is a more streamlined version of the notebook workflow. It runs all at once, so there is less redundancy in saving and loading data and models. 

## Results

Classification metrics will be written out in the clf directory, as well as a confusion matrix. See [Model Evaluation](../../Markdowns/ModelEvaluation.md) for more information.

