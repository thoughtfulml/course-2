from naive_bayes import SpamTrainer
from naive_bayes import EmailObject
import io
import re

print("Cross Validation")

correct = 0
false_positives = 0.0
false_negatives = 0.0
confidence = 0.0
    
def label_to_training_data(fold_file):
  training_data = []
  
  for line in io.open(fold_file, 'r'):
    label_file = line.rstrip().split(' ')
    training_data.append(label_file)

  return SpamTrainer(training_data)

def parse_emails(keyfile):
  emails = []
  print("Parsing emails for " + keyfile)

  for line in io.open(keyfile, 'r'):
    label, file = line.rstrip().split(' ')

    try:
        emails.append(EmailObject(io.open(file, 'r'), category=label))
    except:
        "Ignoring file"

  print("Done parsing files for " + keyfile)
  return emails

def validate(trainer, set_of_emails):
  correct = 0
  false_positive = 0.0
  false_negative = 0.0
  true_positive = 0.0
  true_negative = 0.0
  confidence = 0.0

  total = 0

  for email in set_of_emails:
    classification = trainer.classify(email)
    confidence += classification.score
    total += 1

    if classification.guess == 'spam' and email.category == 'ham':
      false_positive += 1
    elif classification.guess == 'ham' and email.category == 'spam':
      false_negative += 1
    elif classification.guess == 'ham' and email.category == 'ham':
      true_negative += 1
    elif classification.guess == 'spam' and email.category == 'spam':
      true_positive += 1
    
  
  message = """
         Predicted
        SPAM  | HAM
  SPAM  {0}   | {1}
  HAM   {2}   | {3}
  -----------------
  Precision: {4}
  Recall: {5}
  Accuracy: {6} 
  """.format(true_positive, false_negative, false_positive, true_negative,
             true_positive / (true_positive + false_positive), true_positive / (true_positive + false_negative),
             (true_positive + true_negative) / total)
  print(message)

trainer = label_to_training_data('./tests/fixtures/fold1.label')
emails = parse_emails('./tests/fixtures/fold2.label') 
validate(trainer, emails)

trainer = label_to_training_data('./tests/fixtures/fold2.label') 
emails = parse_emails('./tests/fixtures/fold1.label') 
validate(trainer, emails)
