def tarjetas(x,y):
    plumones = (x*12)
    papel = (y*35)
    if plumones<papel:
        return(plumones)
    elif papel<plumones:
        return(papel)

def main():
    #escribe tu código abajo de esta línea
    plumones=int(input('Dame la cantidad de pliegos de papel albanene: '))
    papel=int(input('Dame la cantidad de plumones: '))
    r=tarjetas(plumones,papel)
    print('El número máximo de tarjetas que se pueden hacer es: '+str(r))


if __name__=='__main__':
    main()
