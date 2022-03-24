import pandas as pd
import tabula

'''
Put your grades into a file noten.pdf and save the file into the same folder of this pdf.py
'''


class Module():
    def __init__(self, name, grade, cp) -> None:
        self.name = name
        self.cp = float(cp.replace(",", "."))
        try:
            self.grade = float(grade.replace(",", "."))
            self.graded = True
        except:
            self.graded = False

    def __str__(self) -> str:
        return f'{self.name}-{self.grade if self.graded  else "Bestanden"}-{self.cp}'

    def __repr__(self) -> str:
        return self.__str__()


def getModules(filename):
    df = tabula.read_pdf(filename, pages='2', multiple_tables=True)
    table = df[0]

    modules = []

    for module in table.values:
        if module[2] == "BE":
            modules.append(Module(module[0], module[1], module[4]))

    return modules


modules = getModules("./noten.pdf")
gradedModules = [module for module in modules if module.graded == True]


def calcThroughCutNoten(modules) -> float:
    cp = 0
    grade = 0
    for module in modules:
        cp += module.cp
        grade += module.grade * module.cp
    return grade / cp


throughCut = calcThroughCutNoten(gradedModules)
print(throughCut)
