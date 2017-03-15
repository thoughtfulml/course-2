import re
import sys

if sys.version_info[0] < 3:
    import sets

class Tokenizer:
  NULL = u'\u0000'

  @staticmethod
  def tokenize(string):
    return re.findall("\w+", string.lower())

  @staticmethod
  def unique_tokenizer(string):
    if sys.version_info[0] < 3:
        return sets.Set(Tokenizer.tokenize(string))
    else:
        return set(Tokenizer.tokenize(string))

  @staticmethod
  def ngram(string, ngram):
    tokens = Tokenizer.tokenize(string)

    ngrams = []

    for i in range(len(tokens)):
      shift = i-ngram+1
      padding = max(-shift,0)
      first_idx = max(shift, 0)
      last_idx = first_idx + ngram - padding

      ngrams.append(Tokenizer.pad(tokens[first_idx:last_idx], padding))

    return ngrams

  @staticmethod
  def pad(tokens, padding):
    padded_tokens = []

    for i in range(padding):
      padded_tokens.append(Tokenizer.NULL)

    return padded_tokens + tokens
