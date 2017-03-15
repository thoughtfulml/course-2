import sys
if sys.version_info[0] < 3:
    from sets import Set
import io

from . import EmailObject
from . import Tokenizer
from collections import defaultdict

class SpamTrainer:
  class Classification:
    def __init__(self, guess, score):
      self.guess = guess
      self.score = score
    def __eq__(self, other):
      return self.guess == other.guess and self.score == other.score

  def __init__(self, training_files):
    if sys.version_info[0] < 3:
        self.categories = Set()
    else:
        self.categories = set()

    for category, file in training_files:
      self.categories.add(category)

    self.totals = defaultdict(float)

    self.training = {c: defaultdict(float) for c in self.categories}

    self.to_train = training_files
  
  def normalized_score(self, email):
    score = self.score(email)
    scoresum = sum(score.values())

    if sys.version_info[0] < 3:
        normalized = {cat: (aggregate/scoresum) for cat, aggregate in score.iteritems()} 
    else:
        normalized = {cat: (aggregate/scoresum) for cat, aggregate in score.items() }
    return normalized

  def total_for(self, category):
    return self.totals[category]

  def train(self):
    for category, file in self.to_train:
      email = EmailObject(io.open(file, 'r', errors='ignore'))

      self.categories.add(category)
      
      for token in Tokenizer.unique_tokenizer(email.body()):
        self.training[category][token] += 1
        self.totals['_all'] += 1
        self.totals[category] += 1

    self.to_train = {}

  def score(self, email):
    self.train()

    # TODO: The goal of this is to create the actual naive bayesian score
    # There are a few options here
    # You can toy with different tokenization schemes
    # I have used Tokenizer.unique_tokenizer(email.body())

    cat_totals = self.totals

    # This will give you a starting probability
    # for instance P(Spam) = ?
    # P(Ham) = ?
    # ==> {Ham: ?, Spam: ?}
    # HINT use this to multiply on to create the naive bayesian score

    aggregates = {cat: cat_totals[cat]/cat_totals['_all'] for cat in self.categories}

    for token in ?? # TODO: look at Tokenizer and see if you can determine a simple model
      for cat in self.categories:
        # TODO create joint probability by multiplying on the correct aggregates above
        # to get the number of tokens used look at self.training
        # to get the category totals look at cat_totals or self.totals
        # From there create a probability out of the two.
        # HINT: use a psuedo count. Everything gets a 1 added to it. This avoids cases like 
        # Divison by zero

    return aggregates

  def preference(self):
    return sorted(self.categories, key=lambda cat: self.total_for(cat))

  def classify(self, email):
    score = self.score(email)

    max_score = 0.0
    preference = self.preference()
    max_key = preference[-1]

    for k,v in score.items():
      if v > max_score:
        max_key = k
        max_score = v
      elif v == max_score and preference.index(k) > preference.index(max_key):
        max_key = k
        max_score = v
    return self.Classification(max_key, max_score)

