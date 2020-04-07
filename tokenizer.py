from tensorflow.keras.preprocessing.text import Tokenizer
import pandas as pd

column_names = ['text', 'label']
train_data = pd.read_csv('dataset/imdb-dataset/Train.csv', names=column_names, encoding='utf-8')


train_text = train_data.text.tolist()
train_text.pop(0)

vocab_size = 10000
embedding_dimension = 16
max_lenght = 120
trunc_type = 'post'
oov_tok = '<OOV>'

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(train_text)
