import os
import pandas as pd 
import matplotlib.pyplot as plt 

from joblib import dump
from os.path import join

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    ConfusionMatrixDisplay,
    accuracy_score
)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

class IrisClassification():
    """
    Class to generate data, train, and evluate classifiers on Iris dataset
    """
    def __init__(self):
        self.data_dir = join('..', 'data')
        self.img_dir = join('..', 'imgs')
        self.output_dir = join('..', 'clf_results')
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.img_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)
        self.clf_dict = {
            'DecisionTree': DecisionTreeClassifier(),
            'LogisticRegression': LogisticRegression(max_iter=1000),
            'RandomForest': RandomForestClassifier()
        }
        self.results = pd.DataFrame()
        # Create dictionary mapping target values to actual species names
        self.target_mapping = {
            0: 'setosa',
            1: 'versicolor',
            2: 'virginica'
        }

    def load_data(self):
        """Loads iris data from sklearn
        """
        self.data = load_iris()
        self.df = pd.DataFrame(data=self.data.data, columns=self.data.feature_names)
        self.df["target"] = self.data.target

    def split_data(self):
        """Populates X and y with train and test data
        """
        df_to_split = self.df.copy(deep=True)
        self.y = df_to_split['target']
        self.X = df_to_split.drop(columns=['target'])
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, 
            self.y, 
            test_size=0.33, 
            random_state=42, 
            stratify=self.y
        )

    def train_models(self):
        """Trains classifiers in clf dict
        """
        for label, clf in self.clf_dict.items():
            clf_output_dir = join(self.output_dir, label)
            os.makedirs(clf_output_dir, exist_ok=True)
            clf.fit(self.X_train, self.y_train)
            dump(clf, join(clf_output_dir, 'model.pkl'))
            self.get_metrics(clf, clf_output_dir, train_or_test='Train')
            self.get_metrics(clf, clf_output_dir, train_or_test='Test')

    def get_metrics(self, clf, clf_output_dir, train_or_test='Train'):
        if train_or_test.lower() == 'train':
            X = self.X_train
            y = self.y_train
        else:
            X = self.X_test
            y = self.y_test
        preds = clf.predict(X)        
        cm_plt = ConfusionMatrixDisplay.from_predictions(y_true=y, y_pred=preds, cmap='Blues')
        cm_plt_path = join(clf_output_dir, f'{train_or_test}_confusion_matrix.png')
        print(f'Saving image to path: {cm_plt_path}.')
        cm_plt.figure_.savefig(cm_plt_path)
        report = classification_report(y, preds, output_dict=True)
        df_report = pd.DataFrame(report).transpose()
        report_path = join(clf_output_dir, f'{train_or_test}_metrics.csv')
        print(f'Saving image to path: {report_path}.')
        df_report.to_csv(report_path, index=False)

if __name__=='__main__':
    ic = IrisClassification()
    ic.load_data()
    ic.split_data()
    ic.train_models()