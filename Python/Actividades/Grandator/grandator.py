
# Main script
# @Owner: Adria Vidosa & Marc Moreno



# ######################## ADRIA VIDOSA #################################
import os
def titulo():
    #Adri
    print(r"""
      ________                         .___       __                
     /  _____/___________    ____    __| _/____ _/  |_  ___________ 
    /   \  __\_  __ \__  \  /    \  / __ |\__  \\   __\/  _ \_  __ \
    \    \_\  \  | \// __ \|   |  \/ /_/ | / __ \|  | (  <_> )  | \/
     \______  /__|  (____  /___|  /\____ |(____  /__|  \____/|__|   
            \/           \/     \/      \/     \/                   
                                                    by Marc, Adrià""")
    print("-----------------------------------------------------------------------------------")

def intro():
    #Adri
    titulo()    
    print("Aquest programa calcula la nota final d'un curs a partir de puntuacions ponderades.")
    print("Demana les qualificacions dels parcials, l'examen final i els treballs.")
    print("Finalment, determina la qualificació i mostra un missatge personalitzat.")
    print("-----------------------------------------------------------------------------------")   
    input("\nPrem Enter per continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')
    titulo()

def calculate_exam_score(score, weight): 
    #Adri: Calcula la nota del examen  :D
    if score > 100:
           score = 100
    weighted_score = (score / 100) * weight
    return weighted_score


def process_midterm(name, weight): 
    #Adri: Gestiona la puntuació d'un parcial
    score = int(input(f"Introdueix la puntuació del {name}: "))
    weighted_score = calculate_exam_score(score, weight)
    return weighted_score


def calculate_grade(midterm1, midterm2, final_exam, homework): 
    #Adri: Calcula el percentatge global de la nota del curs :P
    total_grade = midterm1 + midterm2 + final_exam + homework
    return total_grade




# ######################## MARC MORENO #################################

def calculate_homework_score(weight, num_assignments):
    """
    Funcio feta per: Marc Moreno

    Calcula la nota ponderada dels treballs d'acord amb el pes assignat i
    el nombre de treballs.
    
    Paràmetres:
    - weight (int): Pes dels treballs en la nota final.
    - num_assignments (int): Nombre de treballs assignats.
    
    Retorna:
    - float: Nota ponderada dels treballs.
    """
    total_obtained = 0
    total_possible = 0

    for i in range(1, num_assignments + 1):
        print(f"Treball {i}:")
        points_obtained = float(input("Introdueix els punts obtinguts: "))
        max_points = float(input("Introdueix els punts màxims possibles: "))
        
        if points_obtained > max_points:
            points_obtained = max_points
        
        total_obtained += points_obtained
        total_possible += max_points

    # Ajusta la nota total si supera el màxim possible
    if total_obtained > total_possible:
        total_obtained = total_possible

    weighted_score = (total_obtained / total_possible) * weight
    return round(weighted_score, 1)


def assign_letter_grade(percentage):
    """
    Funcio feta per: Marc Moreno
    Assigna una qualificació en forma de lletra basant-se en el percentatge obtingut.

    Paràmetres:
    - percentage (float): Percentatge global obtingut.

    Retorna:
    - str: Qualificació en forma de lletra.
    """
    if percentage >= 90:
        grade = "A"
        message = "Bakanisimo, cuanto chatGPT has usado?"
    elif 80 <= percentage < 90:
        grade = "B"
        message = "Fino ehhh, has estudiao o copiao?."
    elif 70 <= percentage < 80:
        grade = "C"
        message = "Aprobao, ara a echar unos fornais."
    elif 60 <= percentage < 70:
        grade = "D"
        message = "Pelao pelao... pero aprobao."
    else:
        grade = "F"
        message = "Cateto, a ver si estudiamo un poquito mas"

    print(f"La teva qualificació és: {grade}")
    print(message)
    return grade





def main():
    """
    Funcio feta per: Marc Moreno

    Punt de partida del software.
    """
    intro()

    # Pide el peso y las notas de los trabajos
    homework_weight = int(input("Peso de los trabajos (%): "))
    num_assignments = int(input("Numero de trabajos: "))
    homework_score = calculate_homework_score(homework_weight, num_assignments)
    print(f"Nota ponderada de los trabajos: {homework_score}")

    # Pide las notas de los parciales y el examen final
    midterm1_weight = int(input("Peso del parcial 1 (%): "))
    midterm1_score = process_midterm("parcial 1", midterm1_weight)
    print(f"Nota ponderada del parcial 1: {midterm1_score}")

    midterm2_weight = int(input("Peso del parcial 2 (%): "))
    midterm2_score = process_midterm("parcial 2", midterm2_weight)
    print(f"Nota ponderada del parcial 2: {midterm2_score}")

    final_exam_weight = int(input("Peso del examen final (%): "))
    final_exam_score = process_midterm("examen final", final_exam_weight)
    print(f"Nota ponderada del examen final: {final_exam_score}")

    # Calcula la nota total
    total_grade = calculate_grade(midterm1_score, midterm2_score, final_exam_score, homework_score)
    print(f"Nota total del curso (en porcentaje): {total_grade:.2f}%")

    # Asigna la calificación final
    assign_letter_grade(total_grade)

def ejercicio():
    #Adri: para tema errores
    try:
        main()
    except ValueError:
        print("Pon numeros (mira el teclado cuando escribes bobo)")
        print("Vuelve a intentarlo")
        ejercicio()
    except:
        print("Error, intentalo de nuevo noob")
        ejercicio()

ejercicio()