# CTGAN-ENN: A tabular GAN-based Hybrid Sampling Method for Imbalanced and Overlapped Data in Customer Churn Prediction

Our research project in PhD program at AIDA (Applied Intelligence and Data Analytics) lab, College of Computing Khon Kaen University, Thailand

## Overview

CTGAN is a tabular GAN-based oversampling to address class imbalance but has a class overlap problem. We Combined CTGAN with the ENN under-sampling technique to overcome the class overlap. CTGAN-ENN reduced the number of class overlaps by each feature in all datasets. 


## The Result

- Best F1-Score (0.994) in Mobile dataset with Random Forest Algorithm
- Best AUC (1.000) in Mobile dataset with XGBoost Algorithm
- Best G-Mean in Telco 2 dataset with Random Forest and Gradient Boosting Algorithm

## CTGAN-ENN Result in Bank Dataset 
<img src="https://github.com/mahayasa/gan-hybrid-sampling-customer-churn/blob/main/experiment%20image/bank%3Dctganenn.png" alt="Sample Image" width="70%">

We can see on the picture above, CTGAN-ENN cleary separated the customer churn class blue (not churn) and red (churn) and made machine learning algorithm easily to learn.

## Publication

### Preprint

Read the preprint version of paper here : https://www.researchsquare.com/article/rs-3644024/latest

it's my pleasure if any of you have some feedback or question about this research.
  
## Acknowledgments
Thanks to <a href='https://m.kku.ac.th/'>Khon Kaen University</a> for Funding this research work.
