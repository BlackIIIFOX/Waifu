from gensim.models import Word2Vec
import lemmatization
import numpy
from sklearn.manifold import TSNE
import pandas as pd
import matplotlib.pyplot as plt


def plot():

   model = Word2Vec.load('all_vectors.model')
   model.init_sims(replace=True)
   vocab = list(model.wv.vocab)
   X = model[vocab]

   tsne = TSNE(n_components=2)
   X_tsne = tsne.fit_transform(X)

   df = pd.concat([pd.DataFrame(X_tsne),
                    pd.Series(vocab)],
                   axis=1)

   df.columns = ['x', 'y', 'word']
   print(df)

   fig = plt.figure()
   ax = fig.add_subplot(1, 1, 1)

   ax.scatter(df['x'], df['y'])


   for i, txt in enumerate(df['word']):
       ax.annotate(txt, (df['x'].iloc[i], df['y'].iloc[i]))

   plt.show()
