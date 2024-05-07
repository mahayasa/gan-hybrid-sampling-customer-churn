# CTGAN-ENN: A tabular GAN-based Hybrid Sampling Method for Imbalanced and Overlapped Data in Customer Churn Prediction

Our research project in PhD program at AIDA (Applied Intelligence and Data Analytics) lab, College of Computing, Khon Kaen University, Thailand

## Overview

CTGAN is a tabular GAN-based oversampling to address class imbalance but has a class overlap problem. We Combined CTGAN with the ENN under-sampling technique to overcome the class overlap. CTGAN-ENN reduced the number of class overlaps by each feature in all datasets. 


## The Result

- Best F1-Score (0.994) in Mobile dataset with Random Forest Algorithm
- Best AUC (1.000) in Mobile dataset with XGBoost Algorithm
- Best G-Mean (0.984) in Telco 2 dataset with Random Forest and Gradient Boosting Algorithm

## CTGAN-ENN visualization in Bank Dataset 
<img src="https://github.com/mahayasa/gan-hybrid-sampling-customer-churn/blob/main/experiment%20image/bank%3Dctganenn.png" alt="Sample Image" width="70%">

We can see on the picture above, CTGAN-ENN clearly separated the customer churn class blue (not churn) and red (churn) and made machine learning algorithm easily to learn.

## Publication

### Preprint

Read the preprint version of paper here : https://www.researchsquare.com/article/rs-3644024/latest

it's my pleasure if any of you have some feedback or question about this research.

## Installation
[![PyPI version](https://badge.fury.io/py/ctganenn.svg)](https://badge.fury.io/py/ctganenn)
[![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9-blue)](https://badge.fury.io/py/ctganenn)

Install CTGAN-ENN using pip:

```bash
pip install ctganenn
```

## Usage

### Variables

- minClass: the minority class in the dataset (dataframe).
- majClass: the majority class in the dataset (dataframe).
- genData: how much data that you want to generate from minorty class (int).
- targetLabel: what is your target label name in dataset (string).

### Example Usage
```bash
from ctganenn import CTGANENN
```

### use the CTGANENN function with 4 variables
```bash
X, y=CTGANENN(minClass,majClass,genData,targetLabel)
```
### Output
the output of method are X and y :
- X : all features of your dataset
- y : target label of your dataset

### Classification process
you can process the X and y variable to the next step for classification stage. For example using Decision Tree Classifier:

```bash
model = tree.DecisionTreeClassifier()
classification = model.fit(X, y)
```

## Limitation
CTGAN-ENN on this version only works for binary classification

  
## Acknowledgments
This work was supported by <a href='https://m.kku.ac.th/'>Khon Kaen University</a> ASEAN GMS grant and part of AIDA (Applied Intelligence and Data Analytics) lab in College of Computing, Khon Kaen University, Thailand.

