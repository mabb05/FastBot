import pandas as pd
import os


def criar_pasta_num(arquivo, localfinal):
    
    df = pd.read_csv(arquivo, encoding="latin1")
    # print(df.iloc[:,0])

    for a in df.iloc[:,0]:
        path = os.path.join(localfinal,str(a))
        if not os.path.exists(path):
            os.makedirs(path)