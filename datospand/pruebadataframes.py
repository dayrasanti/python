import pandas as pd
lista= [1,2,3,4,5,6,7,8,9]
print(lista)
# crear un Dataframe
data = {"nombre":["Ana","luis","carlos"], "Edad":[23,34,29], "telefono":[123344,122323,24353454]}
df=pd.DataFrame(data)
print(df)