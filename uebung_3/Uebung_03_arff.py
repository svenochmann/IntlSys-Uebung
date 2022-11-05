from scipy.io import arff

import pandas as pd

pumpkin_seed_arff = arff.loadarff('C:\\Users\\Sven\\Datasets\\Pumpkin_Seeds_Dataset.arff')
df = pd.DataFrame(pumpkin_seed_arff[0])



pumpkin_seed_excel = pd.read_excel('C:\\Users\\Sven\\Datasets\\Pumpkin_Seeds_Dataset.xlsx',
    sheet_name='Pumpkin_Seeds_Dataset') 



print(df is pumpkin_seed_excel)