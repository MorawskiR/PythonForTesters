import pandas as pd
pomiary = pd.read_csv("dane1.csv")
# C:\Users\Rafal_Morawski\Desktop\pythonProject
print("Tak Pandas zinterpretowało dane:\n", pomiary.info())
print("Cała tabela:\n", pomiary)