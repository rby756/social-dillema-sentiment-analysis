from sklearn import preprocessing
from sklearn.pipeline import TransformerMixin
from sklearn.pipeline import Pipeline

from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# nltk.download('stopwords')
# nltk.download('wordnet')
def clean_text(text):
  text=str(text)
  text=text.lower()
  text=text.strip()
  text = [re.sub('[^a-zA-Z.]',"", Word) for Word in text.split()]
  english_words=set(stopwords.words('english'))
  word_stemmer=SnowballStemmer('english')
  lemetizer=WordNetLemmatizer()

  word=[Word for Word in text if Word not in english_words]
  word=[word_stemmer.stem(Word) for Word in word]
  word=[lemetizer.lemmatize(Word) for Word in word]

  new_text=" ".join(word)

  return new_text

import re

text = u'This is a smiley face \U0001f602'
print(text) # with emoji

def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)

print(deEmojify(text))



class CleanEmojiTransformer(TransformerMixin):
   def transform(self, X, **transform_params):
      if type(X) == str :
        return [deEmojify(X)]
      else:
        result= [deEmojify(text) for text in X]
        return result
   def fit(self, X, y=None, **fit_params):
        return self


class CleanTextTransformer(TransformerMixin):
   def transform(self, X, **transform_params):
      if type(X) == str :
        return [clean_text(X)]
      else:
        result= [clean_text(text) for text in X]
        return result
   def fit(self, X, y=None, **fit_params):
        return self


preprocessing=Pipeline([
  ("emoji", CleanEmojiTransformer),
  ('cleanText', CleanTextTransformer)
])


import pickle
filename='preprocessing.pkl'
pickle.dump(preprocessing,open(filename,'wb'))