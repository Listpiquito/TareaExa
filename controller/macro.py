import xlwings as xw
import numpy as np
from numpy.ma.core import transpose

from model.Grafica import grafica
from model.Formulas import calcula_Qo



def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]

    Pwf = np.array(sheet['A6:A11'].value)                          #np.array([2400,2000,1500,1000,500,0])
    Pr = sheet['B2'].value
    Qmax = sheet['B3'].value
    sheet["A5"].value= 'Pwf (psi)'
    sheet["A6"].options(transpose = True).value = Pwf
    sheet["A2"].value = 'Pr'
    sheet["B2"].value = Pr
    sheet["A3"].value = 'Qmax'
    sheet["B3"].value = Qmax
    sheet["B5"].value = 'Q (bbl/d)'
    Qo = calcula_Qo(Pr, Qmax, Pwf)
    Qo = np.round(Qo, 3)
    sheet["B6"].options(transpose=True).value = Qo
    grafica1 = grafica(Pwf, Qo)
    sheet.pictures.add(grafica1, name = 'Grafica IPR', update = True, left = sheet.range('G3').left, top = sheet.range('G3').top)
#ok



@xw.func
def hello(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    xw.Book("macro.xlsm").set_mock_caller()
    main()