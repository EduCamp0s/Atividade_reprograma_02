def idade_dos_meus_pets(pet1, pet2, pet3):
    return pet1 + pet2 + pet3

idade1 = int(input("Qual a primeira idade?"))
idade2 = int(input("Qual a segunda idade?"))
idade3 = int(input("Qual a terceira idade?"))

resultado = idade_dos_meus_pets(idade1,idade2,idade3)
print(resultado)
