import pandas as pd
import numpy as np

data = {
    "area" : [2600,3000,3200,3600,4000],
    "price" : [550000,565000,610000,680000,725000]
}

a= pd.DataFrame(data)
a.to_excel("a.xlsx",index=False)