import pandas as pd
df = pd.DataFrame({'age': 18,
                   'name': ["Alice","Bob", "Carl"],
                   'cardio': [60,70,80]})
df['friend'] = 'Alice'
print(df)