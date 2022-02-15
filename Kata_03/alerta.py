tamaño = 25
velocidad = 46
if tamaño > 25 and tamaño < 1000 and velocidad >= 25:
    print("Alerta máxima, el asteroide golpeara la tierra")

elif tamaño < 25: 
    print("El asteroide probablemente se quemara a medida que entre en la atmósfera de la Tierra.")

elif velocidad >= 20:
    print("Asomate al cielo, el asteroide pudo a ver producido un rayito de luz")

elif velocidad == 19:
    print("¡Hay un asteroide que se dirige a la tierra a una velocidad de 19 km/s!")
else:
    print("Todo bien")