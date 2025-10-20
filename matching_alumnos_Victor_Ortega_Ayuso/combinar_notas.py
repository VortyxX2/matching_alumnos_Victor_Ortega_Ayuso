import csv

file_uf1 = 'Notas_Alumnos_UF1.csv'
file_uf2 = 'Notas_Alumnos_UF2.csv'
output_file = 'notas_alumnos.csv'

merged_data = {}

print(f"Iniciando la combinación de archivos...")

try:
    with open(file_uf1, mode='r', encoding='latin-1') as f:
        reader = csv.DictReader(f, delimiter=';')
        
        for row in reader:
            merged_data[row['Id']] = row

    print(f"Lectura de {file_uf1} completada. {len(merged_data)} alumnos encontrados.")

except FileNotFoundError:
    print(f"Error: El archivo {file_uf1} no se ha encontrado.")
    exit()
except Exception as e:
    print(f"Error inesperado al leer {file_uf1}: {e}")
    exit()

try:
    # --- CAMBIO AQUÍ ---
    with open(file_uf2, mode='r', encoding='latin-1') as f:
        reader = csv.DictReader(f, delimiter=';')
        
        for row in reader:
            if row['Id'] in merged_data:
                merged_data[row['Id']]['UF2'] = row['UF2']
            else:
                print(f"Advertencia: Alumno con Id {row['Id']} en {file_uf2} pero no en {file_uf1}.")

    print(f"Lectura y combinación de {file_uf2} completada.")

except FileNotFoundError:
    print(f"Error: El archivo {file_uf2} no se ha encontrado.")
    exit()
except Exception as e:
    print(f"Error inesperado al leer {file_uf2}: {e}")
    exit()

fieldnames = ['Id', 'Apellidos', 'Nombre', 'UF1', 'UF2']

try:
    with open(output_file, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
        
        writer.writeheader()
        
        writer.writerows(merged_data.values())

    print(f"¡Éxito! El archivo '{output_file}' ha sido creado correctamente.")

except PermissionError:
    print(f"Error: No tienes permisos para escribir en '{output_file}'.")
except Exception as e:
    print(f"Error inesperado al escribir {output_file}: {e}")