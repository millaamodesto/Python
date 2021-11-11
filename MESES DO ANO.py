
#dias = 28,30,31
#mes = jan,fev,mar,abr,mai,jun,jul,ago,set,out,nov,dez

print("----------------------------------------------------------------")
print("                   -  MESES COM 31 DIAS  -                      ")
print("| JANEIRO | MARÇO | MAIO | JULHO | AGOSTO | OUTUBRO | DEZEMBRO |")
print("----------------------------------------------------------------")
print("                   -  MESES COM 30 DIAS  -                      ")
print("            | ABRIL | JUNHO | SETEMBRO | NOVEMBRO |             ")
print("----------------------------------------------------------------")
print("                   -  MÊS COM 28 DIAS  -                        ")
print("                       | FEVEREIRO |                            ")
print("----------------------------------------------------------------")

num = (int(input("\nInforme um número de [1 a 12] correspondente ao mês:\n")))

if num < 1 or num > 12:
    print("Mês inválido!")
if num == 1:
    print(" Esse mês possui 31 dias.")
if num == 2:
    print(" Esse mês possui 28 dias.")
if num == 3:
    print(" Esse mês possui 31 dias.")
if num == 4:
    print(" Esse mês possui 30 dias.")
if num == 5:
    print(" Esse mês possui 31 dias.")
if num == 6:
    print(" Esse mês possui 30 dias.")
if num == 7:
    print(" Esse mês possui 31 dias.")
if num == 8:
    print(" Esse mês possui 31 dias.")
if num == 9:
    print(" Esse mês possui 30 dias.")
if num == 10:
    print(" Esse mês possui 31 dias.")
if num == 11:
    print(" Esse mês possui 30 dias.")
if num == 12:
    print(" Esse mês possui 31 dias.")
