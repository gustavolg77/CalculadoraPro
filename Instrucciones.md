------------------------------ INSTRUCCIONES ------------------------------------


Clonamos el repositorio para trabajar localmente

    git clone https://github.com/gustavolg77/CalculadoraPro.git
    cd CalculadoraPro  # una ves clonado con este comando ingresamos al repo

********************************************************
Creacion de sus ramas propias de cada integrante
!importante, deben estar en la rama 'develop'(rama que ya esta creada)
    git branch   #esto les mostrara todas las ramas y en que *rama se encuentran
    #si no estan en la rama 'develop' ejecutar el sgte comando
    git checkout develop

!ya estando en la rama 'develop' # crear su propia rama cada integrante

    git pull origin develop  #opcional para asegurarnos de tener la ultima version
    git checkout -b feature/suma #esto ya te crea tu rama
    # debe poner de nombre cada uno la funcion que lo toco ejm: feature/suma, feature/resta, etc.
    !importante, deben asegurarse que estan actualmente ubicados en su rama y no en otra

    git push origin feature/suma #subimos la rama al repositorio

**********************************************************

Implementacion de funciones en cada rama
    Cada integrante debe:

        *Escribir su función en el archivo Python del proyecto.
        *Probar su código localmente, y asegurarse que no tenga ningun conflicto.

    Hacer commits atomicos:
        !importante, deben asegurarse que estan actualmente ubicados en su rama y no en otra.

        git add .
        git commit -m "Agregada funcion de suma"
        git push origin feature/suma
************************************************************

!Una ves finalizada su parte
    Realizamos el Merge con 'develop'
    1.Cambiamos a develop:

        git checkout develop #nos cambiamos a la rama develop
        git pull origin develop #el pull para traer todos los ultimos cambios en esa rama

    2. Realizamos merge con su rama de feature:

        git merge feature/suma

    3. Subimos los cambios a Github:
        
        git push origin develop
        
!importante, una ves finalizado todas las funciones recien se hara push entre develop y main y solo lo realizara un estudiante.
!importante, estar siempre pendientes en que rama estan trabajando, no deben interferir por ahora en la rama principal 'main'.(en sus ramas 'feature', o maximo en 'develop').
