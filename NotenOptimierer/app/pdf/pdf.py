import pandas as pd
import tabula

'''
Put your grades into a file noten.pdf and save the file into the same folder of this pdf.py
'''

class Modul():
    def __init__(self, name, cp, grade) -> None:
        self.name = name
        self.cp = cp
        self.grade = grade

    def __str__(self) -> str:
        return f'{self.name}-{self.grade}-{self.cp}'

    def __repr__(self) -> str:
        return self.__str__()


file = "./noten.pdf"
df = tabula.read_pdf(file, pages='2', multiple_tables=True)
table = df[0]

modules = []

for module  in table.values:
    if module[2] == "BE" : 
        modules.append(Modul(module[0], module[1], module[4]))

print(modules)
