#Dado el mensaje obtener todas las combinaciones posibles.
#Obtener cada frecuencia de todas las configuraciones
#calcular la ji cuadrada:
#Se calcula la menor ji cuadrada y esa es la frecuencia del mensaje correcto.
#Desencriptar el mensaje con esa frecuencia.

import encoder
import frecuencias
import identificarIndice

ABECEDARIO = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z"]

dicJI = {}

def computeJiSquared( ):

    encodedText = open("textoEncriptado.txt", 'r', encoding="utf8")
    sampleTextDictionary = frecuencias.frecuencias()

    aEncode = (encodedText.read())
    for i in range(1, 26):    #For cycle from the first letter to last
        encodedTextSwap = encoder.encode(aEncode, i)
        ji = 0
        encodedTextDictionary = frecuencias.frecuenciaTexto(encodedTextSwap)

        for n in range(len(ABECEDARIO)):
            charToProcess = ABECEDARIO[n]
            charEncodedText = encodedTextDictionary.get(charToProcess)
            charSampleText = sampleTextDictionary.get(charToProcess)
            if charSampleText == 0:
                charSampleText = 0.00000000001
            ji = ji + ((charEncodedText - charSampleText)*(charEncodedText - charSampleText))/charSampleText
            dicJI[i] = ji
    print(dicJI)
    swap = min(dicJI, key=dicJI.get)
    return swap
if __name__ == '__main__':
    decodedText = computeJiSquared()
    print("Swap: ")
    swap = 26 - decodedText
    print(swap)
    print("texto decodificado: ")
    encodedText = open("textoEncriptado.txt", 'r', encoding="utf8")
    print(encoder.encode(encodedText.read(),-swap))
