#INICIO
print("\n---MESES-EN-QUE-UN-CAPITAL-SE-DUPLICA---\n")

#INPUT
c=int(input("\nDigite el capital: "))

#PROCESSING
m=2*c
i=int
mes=0

while (c < m):
    i = c * 0.05
    c= c + i
    mes= mes + 1


print("\nEl capital se duplicara en " + str(mes) + " meses.")

#FIN