
print(" ------------------------------- ")
print(" | Classificação de triângulos | ")
print(" ------------------------------- ")
l1 = (int(input("\nInforme o valor do primeiro lado:")))
l2 = (int(input("Informe o valor do segundo lado:")))
l3 = (int(input("Informe o valor do terceiro lado:")))

if l1 == l2 and l1 == l3 and l2 == l3:
    print("\nTriângulo equilátero")
if l1 == l2 and l2 != l3 or l3 == l1 and l2 != l1 or l2 == l3 and l1 != l2:
    print("\nTriângulo Isósceles")
else:
    print("\nTriângulo escaleno")
