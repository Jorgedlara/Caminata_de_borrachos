from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)
    
    for _ in range (pasos):
        campo.mover_borracho(borracho)
    
    return inicio.distancia(campo.obtener_coordenada(borracho))

def simular_caminata(pasos, num_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(name='Jorge')
    origen = Coordenada(0,0)
    distancias = []
    for _ in range (num_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))
    
    return distancias

def graficar(x, y):
    grafica = figure(title = "Camino borracho", x_axis_label = 'pasos', y_axis_label='distancia')
    grafica.line(x, y, legend ='distancia media')

    show(grafica)

def main(distancias_de_caminata, num_intentos, tipo_de_borracho):
    distancias_media_por_caminata = []
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, num_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias)/len(distancias), 4)
        distnacia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distnacia_maxima}')
        print(f'Min = {distancia_minima}')
    graficar(distancias_de_caminata, distancias_media_por_caminata)

if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    num_intentos = 100

    main(distancias_de_caminata, num_intentos, BorrachoTradicional)