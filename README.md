# Lab Number 2

The point of this Lab is to get you working with Naive Bayesian Classifiers and to continue on the testing mindset.

# Environment

To get your environment running you will need Python 3.5.x (I've tested both). You will also have to install some packages:

```
pip install bs4 chardet
```

# To run the experiment

To run this experiment I want you to work with crossvalidate.py and naive_bayes/spam_trainer.rb

The goal of this Lab is to get you looking at the nuances of the naive bayesian classifier.

Note that probabilities tend to be somewhat useless on naive bayesian classifiers so we have left out ROC curves here.

## Suggestion

Shortening the fold1.label and fold2.label files will help increase the speed of crossvalidating.

# My results

```
Cross Validation
Parsing emails for ./tests/fixtures/fold2.label
Done parsing files for ./tests/fixtures/fold2.label

         Predicted
        SPAM  | HAM
  SPAM  290.0   | 333.0
  HAM   2.0   | 1400.0
  -----------------
  Precision: 0.9931506849315068
  Recall: 0.4654895666131621
  Accuracy: 0.8345679012345679 
  
Parsing emails for ./tests/fixtures/fold1.label
Done parsing files for ./tests/fixtures/fold1.label

         Predicted
        SPAM  | HAM
  SPAM  273.0   | 347.0
  HAM   3.0   | 1389.0
  -----------------
  Precision: 0.9891304347826086
  Recall: 0.4403225806451613
  Accuracy: 0.8260437375745527 
```
