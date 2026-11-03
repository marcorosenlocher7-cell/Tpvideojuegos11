
import sqlite3

conexion = sqlite3.connect(r"C:\Users\Estudiante\Downloads\tpvideojuegos\arigato.db")
cursor = conexion.cursor()
print("conexion establecida")
conexion.commit()

def consultar_todos():

    cursor.execute("SELECT * FROM games")

    videojuegos = cursor.fetchall()

    if len(videojuegos) == 0:

        print("No hay videojuegos registrados.")

    else:

        for juego in videojuegos:

            print(juego)

def buscar_por_id():


    id_buscar = input("Ingrese el ID del videojuego: ")

    cursor.execute(
        "SELECT * FROM games WHERE id = ?",
        (id_buscar,)
    )

    videojuego = cursor.fetchone()

    if videojuego is not None:


        print("Videojuego encontrado:", videojuego)

    else:

        print("No se encontro ningun videojuego con ese ID.")

def agregar_videojuego():

    titulo = input("Ingrese el titulo: ")
    plataforma = input("Ingrese la plataforma: ")
    genero = input("Ingrese el genero: ")
    anio = input("Ingrese el año de lanzamiento: ")

    cursor.execute(
        """INSERT INTO games
        (titulo, plataforma, genero, anio)
        VALUES (?, ?, ?, ?)""",

        (titulo, plataforma, genero, anio)
    )

    conexion.commit()

    print("Videojuego agregado correctamente.")


def actualizar_videojuego():

    id_actualizar = input("Ingrese el ID que desea actualizar: ")

    cursor.execute(
        "SELECT * FROM games WHERE id = ?",
        (id_actualizar,)
    )

    videojuego = cursor.fetchone()


    if videojuego is not None:

  
        titulo = input("Nuevo titulo: ")
        plataforma = input("Nueva plataforma: ")
        genero = input("Nuevo genero: ")
        anio = input("Nuevo año: ")

        cursor.execute(
            """UPDATE games
            SET titulo = ?, plataforma = ?, genero = ?, anio = ?
            WHERE id = ?""",

            (titulo, plataforma, genero, anio, id_actualizar)
        )

        conexion.commit()

        print("Videojuego actualizado correctamente.")

    else:

        print("No existe un videojuego con ese ID.")


def eliminar_videojuego():

    id_eliminar = input("Ingrese el ID que desea eliminar: ")

    cursor.execute(
        "SELECT * FROM games WHERE id = ?",
        (id_eliminar,)
    )

    videojuego = cursor.fetchone()

    if videojuego is not None:

        cursor.execute(
            "DELETE FROM games WHERE id = ?",
            (id_eliminar,)
        )

        conexion.commit()

        print("Videojuego eliminado correctamente.")

    else:

        print("No existe un videojuego con ese ID.")


try:

    while True:

        # Mostramos las opciones disponibles.
        print("\n===== MENU DE VIDEOJUEGOS =====")
        print("1. Consultar todos los registros")
        print("2. Buscar un registro por ID")
        print("3. Agregar un registro")
        print("4. Actualizar un registro")
        print("5. Eliminar un registro")
        print("6. Salir")


        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            consultar_todos()

        elif opcion == "2":
            buscar_por_id()

        elif opcion == "3":
            agregar_videojuego()
            
        elif opcion == "4":
            actualizar_videojuego()

        elif opcion == "5":
            eliminar_videojuego()

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion incorrecta. Intente nuevamente.")

finally:

    cursor.close()

    conexion.close()

    print("Conexion con la base de datos cerrada.")

