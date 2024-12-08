from app import mysql

# Vamos a crear un controlador para los usuarios
# Para obtener todos los usuarios
def get_users():
  # Vamos a establecer una conexion con la base de datos
  cursor = mysql.connection.cursor()
  
  # VAmos a ejecutar la consulta
  cursor.execute('SELECT * FROM users')
  
  # Vamos a recuperar los datos
  columns = [columna[0] for columna in cursor.description]
  
  users = [dict(zip(columns, fila)) for fila in cursor.fetchall()]
  #      id : 1
  #      name : "Ricardo"
  
  # Vamos a cerrar la conexion
  cursor.close()
  return users

# Para obtener un usuario
def get_user(id):
  #Vamos a establecer una conexion con la base de datos
  cursor = mysql.connection.cursor()
  
  # vamos a ejecutar la consulta
  cursor.execute('SELECT * FROM users WHERE id = %s', (id,))
  # Vamos a recuperar los datos
  columns = [columna[0] for columna in cursor.description]
  response = dict(zip(columns, cursor.fetchone()))
  cursor.close()
  
  if response:
    return response
  else:
    return {"Mensaje": "No se puede encontrar el usuario"}
  
# Para obtener un usuario a traves de query parameters
def get_user_query(id):
  if id:
    #Vamos a establecer una conexion con la base de datos
    cursor = mysql.connection.cursor()
    
    # vamos a ejecutar la consulta
    cursor.execute('SELECT * FROM users WHERE id = %s', (id,))
    # Vamos a recuperar los datos
    columns = [columna[0] for columna in cursor.description]
    response = dict(zip(columns, cursor.fetchone()))
    cursor.close()
    
    if response:
      return response
    else:
      return {"Mensaje": "No se puede encontrar el usuario"}
  else:
    return {"Mensaje":"Debe enviarse el id"}
  
# Para crear un usuario
def create_user(data):
  nombre = data.get('nombre')
  apellido = data.get('apellido')
  # Api pueden hacer validacion de expresiones regulares antes de realizar la consulta
  # Vamos a establecer una conexion con la base de datos
  cursor = mysql.connection.cursor()
  
  # Vamos a ejecutar la consulta
  cursor.execute('INSERT INTO users (nombre, apellido) VALUES (%s, %s)', (nombre, apellido))
  
  mysql.connection.commit()
  cursor.close()
  
  return {"Mensaaje": "Usuario creado con exito! :D"}

# Para actualizar un usuario
def update_user(id, data):
  if not data:
    return {"Mensaje":"Debe enviarse los datos"}
  
  cursor = mysql.connection.cursor()
  
  update_query = "UPDATE users SET "
  update_data = []
  
  for campo, valor in data.items():
    if campo in ['nombre','apellido']:
      update_query += f"{campo} = %s, " # UPDATE users SET nombre = %s, apellido = %s  
      update_data.append(valor) # ["elimelech"]
      
  if not update_data:
    return {"Mensaje": "Debe enviarse los datos"}
  
  # Vamos a eliminar la coma del final
  update_query = update_query.rstrip(", ")
  
  # Vamos a agregar la condicion
  update_query += " WHERE id = %s" # UPDATE users SET nombre = %s, apellido = %s WHERE id = %s
  update_data.append(id)
  
  # Vamos a ejecutar la consulta
  cursor.execute(update_query, tuple(update_data,))
  mysql.connection.commit()
  cursor.close()
  
  return {"Mensaje":"Usuario actualizado con exito!"}

# Para eliminar un usuario
def delete_user(id):
  cursor = mysql.connection.cursor()
  
  # Ejecutamos la consulta IMPORTANTE COLOCAR LA CONDICION
  cursor.execute('DELETE FROM users WHERE id = %s', (id,)) 
  mysql.connection.commit()
  cursor.close()
  
  return {"Mensaje":"Usuario eliminado con exito!"}