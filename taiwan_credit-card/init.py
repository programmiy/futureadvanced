from datasets import load_dataset
import pandas as pd
import imodels
import numpy as np

dataset = load_dataset("imodels/credit-card")
df=pd.DataFrame(dataset['train'])
X= df.drop(columns=['default.payment.next.month'])
y= df['default.payment.next.month'].values

#test


# Fit a model:
m = imodels.FIGSClassifier(max_rules=5)
m.fit(X, y)
print(m)


# Evaluate the model:

df_test=pd.DataFrame(dataset['test'])
X_test= df_test.drop(columns=['default.payment.next.month'])
y_test= df_test['default.payment.next.month'].values
print('accuracy:', np.mean(m.predict(X_test) == y_test))