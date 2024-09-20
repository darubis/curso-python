___
[pildoras informaticas](https://www.youtube.com/watch?v=TLVnoqXGWpY)

Que son?

Estructuras que extraen valores de una funcion y se almacenan en objetos iterables (que se pueden recorrer).

Estos valores se almacenan de uno en uno

Cada vez que un generador almacena un valor, esta permanece en un estado pausado hasta que se solicita al siguiente. 
Esta caracteristica es conocida como "suspencion de estado"

## Utilidad

Son mas eficientes que las funciones tradicionales

Muy eficientes con listas de valores infinitos

Bajo determinados escenarios, sera muy util que un genetador devuelva los valores de uno en uno.

## Sintaxis

```
def generarNumeros():
	yield numeros
```

