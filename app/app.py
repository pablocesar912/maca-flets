# from flask import Flask, render_template, request, redirect, url_for
# import pandas as pd
# import os

# app = Flask(__name__)

# # Configura la ruta de la carpeta estática
# app.config['STATIC_FOLDER'] = 'static'

# # Ruta del archivo CSV (carpeta/archivo.csv)
# csv_user_file_path = os.path.join('data', 'users.csv')
# csv_vehicle_file_path = os.path.join('data', 'vehicles.csv')

# # Cargar los dataframes desde los archivos CSV si existen, sino crear un dataframes vacíos
# if os.path.exists(csv_user_file_path):
#     users_df = pd.read_csv(csv_user_file_path)
# else:
#     users_df = pd.DataFrame(columns=['ID-Usuario', 'Nombre', 'Email', 'Teléfono', 'CUIT'])

# if os.path.exists(csv_vehicle_file_path):
#     vehicles_df = pd.read_csv(csv_vehicle_file_path)
# else:
#     vehicles_df = pd.DataFrame(columns=['ID-Vehículo', 'ID-Usuario', 'Modelo', 'Marca', 'Dominio', 'Seguro_RTO', 'Capacidad-kg', 'Año'])

# # Función para guardar los dataframes en archivos CSV
# def save_users_to_csv():
#     users_df.to_csv(csv_user_file_path, index=False)

# def save_vehicles_to_csv():
#     vehicles_df.to_csv(csv_vehicle_file_path, index=False)

# # Ruta de 'index.html'
# @app.route('/')
# def index():
#     return render_template('index.html')


# # Ruta de 'index.html'
# @app.route('/terms')
# def terms():
#     return render_template('terms.html')

# # Ruta de 'register_user'
# @app.route('/register_user', methods=['GET', 'POST'])
# def register_user():
#     global users_df
    
#     if request.method == 'POST':
#         user_id = len(users_df) + 1
#         nombre = request.form['nombre']
#         email = request.form['email']
#         telefono = request.form['telefono']
#         cuit = request.form['cuit']
#         terms_accepted = request.form.get('terms')

#         if terms_accepted:
#             # Crear un nuevo dataframe con la nueva fila
#             new_user = pd.DataFrame([{
#                 'ID-Usuario': user_id,
#                 'Nombre': nombre,
#                 'Email': email,
#                 'Teléfono': telefono,
#                 'CUIT': cuit
#             }])
#             # Concatenar el nuevo dataframe con el dataframe existente
#             users_df = pd.concat([users_df, new_user], ignore_index=True)
#             save_users_to_csv()
            
#             return redirect(url_for('register_vehicle', user_id=user_id))
#         else:
#             return "Debe aceptar los términos y condiciones."

#     return render_template('register_user.html')

# @app.route('/users')
# def users():
#     global users_df
#     # Convertir el dataframe a formato HTML
#     users_html = users_df.to_html(index=False)
#     return render_template('users.html', users_table=users_html)

# # Ruta de 'register_vehicle'
# @app.route('/register_vehicle/<int:user_id>', methods=['GET', 'POST'])
# def register_vehicle(user_id):
#     global vehicles_df
    
#     if request.method == 'POST':
#         vehicle_id = len(vehicles_df) + 1
#         modelo = request.form['modelo']
#         marca = request.form['marca']
#         dominio = request.form['dominio']
#         seguro_rto = request.form['seguro_rto']
#         capacidad = request.form['capacidad']
#         anio = request.form['anio']

#         new_vehicle = pd.DataFrame([{
#             'ID-Vehículo': vehicle_id,
#             'ID-Usuario': user_id,
#             'Modelo': modelo,
#             'Marca': marca,
#             'Dominio': dominio,
#             'Seguro_RTO': seguro_rto,
#             'Capacidad-kg': capacidad,
#             'Año': anio
#         }])
#         vehicles_df = pd.concat([vehicles_df, new_vehicle], ignore_index=True)
#         save_vehicles_to_csv()
        
#         return redirect(url_for('index'))
    
#     return render_template('register_vehicle.html', user_id=user_id)

# @app.route('/vehicles')
# def vehicles():
#     global vehicles_df, users_df
    
#     # Realizar la combinación de dataframes en base a 'ID-Usuario'
#     merged_df = vehicles_df.merge(users_df, on='ID-Usuario')
    
#     # Seleccionar y renombrar las columnas necesarias para la visualización
#     display_df = merged_df[['ID-Vehículo', 'Modelo', 'Marca', 'Dominio', 'Seguro_RTO', 'Capacidad-kg', 'Año', 'Nombre']]
#     display_df.rename(columns={'Nombre': 'Propietario'}, inplace=True)
    
#     # Convertir el dataframe a formato HTML
#     vehicles_html = display_df.to_html(index=False)
    
#     return render_template('vehicles.html', vehicles_table=vehicles_html)


# if __name__ == '__main__':
#     # Crear la carpeta data si no existe
#     if not os.path.exists('data'):
#         os.makedirs('data')
        
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

# Configura la ruta de la carpeta estática
app.config['STATIC_FOLDER'] = 'static'

# Ruta del archivo CSV (carpeta/archivo.csv)
csv_user_file_path = os.path.join('data', 'users.csv')
csv_vehicle_file_path = os.path.join('data', 'vehicles.csv')

# Cargar los dataframes desde los archivos CSV si existen, sino crear un dataframes vacíos
if os.path.exists(csv_user_file_path):
    users_df = pd.read_csv(csv_user_file_path)
else:
    users_df = pd.DataFrame(columns=['ID-Usuario', 'Nombre', 'Email', 'Teléfono', 'CUIT'])

if os.path.exists(csv_vehicle_file_path):
    vehicles_df = pd.read_csv(csv_vehicle_file_path)
else:
    vehicles_df = pd.DataFrame(columns=['ID-Vehículo', 'Modelo', 'Marca', 'Dominio', 'Seguro_RTO', 'Capacidad-kg', 'Año', 'ID-Usuario'])

# Función para guardar los dataframes en archivos CSV
def save_users_to_csv():
    users_df.to_csv(csv_user_file_path, index=False)

def save_vehicles_to_csv():
    vehicles_df.to_csv(csv_vehicle_file_path, index=False)

# Ruta de 'index.html'
@app.route('/')
def index():
    return render_template('index.html')


# Ruta de 'index.html'
@app.route('/terms')
def terms():
    return render_template('terms.html')

# Ruta de 'register_user'
@app.route('/register_user', methods=['GET', 'POST'])
def register_user():
    global users_df
    
    if request.method == 'POST':
        user_id = len(users_df) + 1
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        cuit = request.form['cuit']
        terms_accepted = request.form.get('terms')

        if terms_accepted:
            # Crear un nuevo dataframe con la nueva fila
            new_user = pd.DataFrame([{
                'ID-Usuario': user_id,
                'Nombre': nombre,
                'Email': email,
                'Teléfono': telefono,
                'CUIT': cuit
            }])
            # Concatenar el nuevo dataframe con el dataframe existente
            users_df = pd.concat([users_df, new_user], ignore_index=True)
            save_users_to_csv()
            
            return redirect(url_for('register_vehicle', user_id=user_id))
        else:
            return "Debe aceptar los términos y condiciones."

    return render_template('register_user.html')

@app.route('/users')
def users():
    global users_df
    # Convertir el dataframe a formato HTML
    users_html = users_df.to_html(index=False)
    return render_template('users.html', users_table=users_html)

# Ruta de 'register_vehicle'
@app.route('/register_vehicle/<int:user_id>', methods=['GET', 'POST'])
def register_vehicle(user_id):
    global vehicles_df
    
    if request.method == 'POST':
        vehicle_id = len(vehicles_df) + 1
        modelo = request.form['modelo']
        marca = request.form['marca']
        dominio = request.form['dominio']
        seguro_rto = request.form['seguro_rto']
        capacidad = request.form['capacidad']
        anio = request.form['anio']

        new_vehicle = pd.DataFrame([{
            'ID-Vehículo': vehicle_id,
            'Modelo': modelo,
            'Marca': marca,
            'Dominio': dominio,
            'Seguro_RTO': seguro_rto,
            'Capacidad-kg': capacidad,
            'Año': anio,
            'ID-Usuario': user_id
        }])
        vehicles_df = pd.concat([vehicles_df, new_vehicle], ignore_index=True)
        save_vehicles_to_csv()
        
        return redirect(url_for('index'))
    
    return render_template('register_vehicle.html', user_id=user_id)

@app.route('/vehicles')
def vehicles():
    global vehicles_df, users_df
    
    # Realizar la combinación de dataframes en base a 'ID-Usuario'
    merged_df = vehicles_df.merge(users_df, on='ID-Usuario')
    
    # Seleccionar y renombrar las columnas necesarias para la visualización
    display_df = merged_df[['ID-Vehículo', 'Modelo', 'Marca', 'Dominio', 'Seguro_RTO', 'Capacidad-kg', 'Año', 'Nombre']]
    display_df.rename(columns={'Nombre': 'Propietario'}, inplace=True)
    
    # Convertir el dataframe a formato HTML
    vehicles_html = display_df.to_html(index=False)
    
    return render_template('vehicles.html', vehicles_table=vehicles_html)


if __name__ == '__main__':
    # Crear la carpeta data si no existe
    if not os.path.exists('data'):
        os.makedirs('data')
        
    app.run(debug=True)
