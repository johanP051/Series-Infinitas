class Series():
    def serie(self, n):
        s_n = 0
        for i in range(0, n + 1):
            s_n += 1 / (2**i)
        return s_n
    
    def serie_p(self, n, p):
    #1 / n^p converge para p >1
        s_n = 0
        for i in range(1, n + 1):
            s_n += 1/ i**p
        return s_n

def main():
#Escriba un código en Python para calcular la suma de la serie geométrica 1/2^i para n ∈ {10, 50, 100}
    print("\n\nPrimer Ejercicio")
    mi_serieGeometrica = Series()
    N = [10, 50, 100]
    for n in N:
        print(f"Para n = {n}, La serie converge a S_n = {mi_serieGeometrica.serie(n)}")


    print("\n\nSegundo Ejercicio")
    # Compara la convergencia de las series 1/i² y 1/i^5 mediante la comparación de sus sumas parciales en n ∈ {10, 50, 100}

    mi_serie_p = Series()

    P = [2, 5]
    N = [10, 50, 100]


    for n in N:
        print("\n")
        for p in P:
            print(f"Para n = {n}, La serie_p 1/i^{p} converge a S_n= {mi_serie_p.serie_p(n, p)}")
    
    print("\n\nTercer Ejercicio")
    #Programe la n-esima suma parcial de la serie armónica 1/i . Dé el N lo suficientemente grande para que S_n sobre pase el valor de 10.
    mi_serie_armonica = Series()

    #Para que s_n sea mayor a 10, n tiene que ser >= a 100001
    n_1 = 500000000
    p_1 = 1

    print(f"{mi_serie_armonica.serie_p(n_1, p_1)}\n\n")


if __name__ == "__main__":
    main()