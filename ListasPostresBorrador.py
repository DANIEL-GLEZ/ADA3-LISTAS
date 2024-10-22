postres = {
    "Pastel de Chocolate": ["Harina", "Azúcar", "Cacao", "Huevos", "Leche", "Cacao"],
    "Helado de Vainilla": ["Leche", "Azúcar", "Vainilla", "Leche"],
    "Tarta de Manzana": ["Manzanas", "Harina", "Azúcar", "Mantequilla", "Manzanas"],
    "Brownies": ["Harina", "Azúcar", "Cacao", "Mantequilla", "Huevos", "Azúcar"],
    "Diples": ["Masa, Huevo, Jarabe de Azúcar, Miel, Canela, Nueces"]
}

def mostrar_ingredientes(postre):
    if postre in postres:
        print(f"Ingredientes de {postre}: {', '.join(postres[postre])}")
    else:
        print(f"{postre} no está en la lista de postres.")

def agregar_ingredientes(postre, nuevo_ingrediente):
    if postre in postres:
        postres[postre].append(nuevo_ingrediente)
        print(f"Ingrediente '{nuevo_ingrediente}' añadido a {postre}.")
    else:
        print(f"{postre} no está en la lista de postres.")

def eliminar_ingrediente(postre, ingrediente):
    if postre in postres:
        if ingrediente in postres[postre]:
            postres[postre].remove(ingrediente)
            print(f"Ingrediente '{ingrediente}' eliminado de {postre}.")
            mostrar_ingredientes(postre)
        else:
            print(f"Ingrediente '{ingrediente}' no está en {postre}.")
    else:
        print(f"{postre} no está en la lista de postres.")

def alta_postre(postre, ingredientes):
    if postre not in postres:
        postres[postre] = ingredientes
        print(f"Postre '{postre}' añadido con ingredientes: {', '.join(ingredientes)}.")
    else:
        print(f"El postre {postre} ya existe.")

def baja_postre(postre):
    if postre in postres:
        del postres[postre]
        print(f"Postre {postre} eliminado.")
    else:
        print(f"{postre} no está en la lista de postres.")

def eliminar_duplicados(postres):
    for postre, ingredientes in postres.items():
        ingredientes_unicos = list(set(ingredientes))
        postres[postre] = ingredientes_unicos

eliminar_duplicados(postres)

def menu():
    while True:
        print("\nOpciones: ")
        print("1. Mostrar ingredientes de un postre")
        print("2. Agregar ingredientes a un postre")
        print("3. Eliminar ingredientes de un postre")
        print("4. Dar de alta un postre")
        print("5. Dar de baja un postre")
        print("6. Mostrar todos los postres")
        print("7. Eliminar ingredientes duplicados")
        print("8. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            postre = input("Introduce el nombre del postre: ")
            mostrar_ingredientes(postre)
        elif opcion == '2':
            postre = input("Introduce el nombre del postre: ")
            ingrediente = input("Introduce el ingrediente a añadir: ")
            agregar_ingredientes(postre, ingrediente)
        elif opcion == '3':
            postre = input("Introduce el nombre del postre: ")
            ingrediente = input("Introduce el ingrediente a eliminar: ")
            eliminar_ingrediente(postre, ingrediente)
        elif opcion == '4':
            postre = input("Introduce el nombre del nuevo postre: ")
            ingredientes = input("Introduce los ingredientes separados por comas: ").split(", ")
            alta_postre(postre, ingredientes)
        elif opcion == '5':
            postre = input("Introduce el nombre del postre a eliminar: ")
            baja_postre(postre)
        elif opcion == '6':
            print("\nPostres actuales:")
            for p, ing in postres.items():
                print(f"{p}: {', '.join(ing)}")
        elif opcion == '7':
            eliminar_duplicados(postres)
            print("Ingredientes duplicados eliminados.")
        elif opcion == '8':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor elige nuevamente.")

menu()
