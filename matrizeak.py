# N×M matrize bat emanda, itzuli bere elementuak goiko ezkerreko izkinatik hasita espiralean zeharkatuta.

matrizea = [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16],
            [17,18,19,20],]


def espiral_zeharkatu(matrizea):
    if not matrizea:
        return []

    emaitza = []
    goia = 0
    behea = len(matrizea) - 1
    ezkerra = 0
    eskuina = len(matrizea[0]) - 1

    while goia <= behea and ezkerra <= eskuina:
        for i in range(ezkerra, eskuina + 1):
            emaitza.append(matrizea[goia][i])
        goia += 1

        for i in range(goia, behea + 1):
            emaitza.append(matrizea[i][eskuina])
        eskuina -= 1

        if goia <= behea:
            for i in range(eskuina, ezkerra - 1, -1):
                emaitza.append(matrizea[behea][i])
            behea -= 1

        if ezkerra <= eskuina:
            for i in range(behea, goia - 1, -1):
                emaitza.append(matrizea[i][ezkerra])
            ezkerra += 1

    return emaitza


print(espiral_zeharkatu(matrizea))
