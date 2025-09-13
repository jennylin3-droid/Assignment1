import pandas as pd

hcpcs= pd.read_csv ('./Module1_MedicalCodexes/hcpcs/HCPC2023_JAN.txt')

colspecs = [(0, 11), (11, 90), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]
column_names = [
    "Code", "desription_small", "description_large", "status", "eff_date", "end_date", "rvu", "multiplier"
]
df = pd.read_fwf(file_path, colspecs=colspecs, names=column_names)


output_path = "Module1_MedicalCodexes/hcpcs/output/HCPC2023_JAN.csv"
df.to_csv(output_path, index=False)
