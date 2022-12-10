import pandas as pd

db=pd.read_csv("MOCK_DATA.csv")
pd.set_option('display.max_columns', 500)
print(db)