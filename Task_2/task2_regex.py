# import modules
import pandas as pd
dim_df = pd.read_csv('../candidateEvalData/dim_df_correct.csv')
print(dim_df.head())

#0: 19×52cm
r0 = r'(\d+)×(\d+)cm'

#1: 50 x 66,4 cm
r1 = r'(\d+(?:,\d+)?)\s*x\s*(\d+(?:,\d+)?)\s*cm'

#2: 168.9 x 274.3 x 3.8 cm (66 1/2 x 108 x 1 1/2 in.)
r2 = r'(\d+(?:.\d+)?)\s*x\s*(\d+(?:.\d+)?)\s*x\s*(\d+(?:.\d+)?)\s*cm'

#3: Sheet: 16 1/4 × 12 1/4 in. (41.3 × 31.1 cm) Image: 14 × 9 7/8 in. (35.6 × 25.1 cm)
r3 = r'Image.*\((\d+(?:.\d+)?)\s*×\s*(\d+(?:.\d+)?)\s*cm'

#4: 5 by 5in
r4 = r'(\d+)\s*by\s*(\d+)\s*in'