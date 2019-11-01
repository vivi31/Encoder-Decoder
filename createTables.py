#encoding: UTF-8
import terminaltables
import frecuencias
import jiCuadrada


def createSampleTable():
    dictTable = frecuencias.frecuencias()
    dictTableKeys = list(dictTable.keys())
    dictTableValues = list(dictTable.values())
    data = []
    data.append(['Processed Char:', 'Average count:'])
    for n in range(26):
        data.append([str(dictTableKeys[n]), str(dictTableValues[n])])
    table = terminaltables.DoubleTable(data)
    table.title = "Tabla de Frecuencias"
    table.inner_row_border = True
    table.inner_column_border = False
    table.justify_columns[0] = 'center'
    return table.table

def createCustomTable(text):
    dictTable = frecuencias.frecuenciaLetras(text)
    dictTableKeys = list(dictTable.keys())
    dictTableValues = list(dictTable.values())
    data = []
    data.append(['Processed Char', 'Average count'])
    for n in range(len(dictTable)):
        data.append([str(dictTableKeys[n]), str(dictTableValues[n])])
    table = terminaltables.AsciiTable(data)
    table.inner_row_border = True
    table.inner_column_border = False
    table.title = "Tabla de frecuencias"
    return table.table

def createJiTable(dictionary):
    dictTable = dictionary
    dictTableKeys = list(dictTable.keys())
    dictTableValues = list(dictTable.values())
    data = []
    data.append(["Swap index", "JI"])
    for n in range(len(dictTable)):
        data.append([str(dictTableKeys[n]), str(dictTableValues[n])])
    table = terminaltables.DoubleTable(data)
    table.title = "JI Cuadrada"
    table.inner_row_border = True
    table.inner_column_border = False
    table.justify_columns[0] = 'center'
    return table.table

if __name__ == "__main__":
    output = createSampleTable()
    print(output)


