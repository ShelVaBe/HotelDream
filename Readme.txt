crear un entorno virtual (virtual venv)
Activalo  venv\Scripts\activate    
instala 
pip install django
pip install mysqlclient 

modifica la ruta del settings en el apartado de Database a la ruta donde se encuentra ese certificado segun donde esta descargado el proyecto:
ssl': {
                'ca': 'D:\Documentos\9no y ultimo semestre\Topicos\Dream Hotel\CerHotel.pem',
            },
python manage.py runserver  

rutas
/admin
/hotel_app/reservacion

Usuario conraseña de admin
usuario: Hotel 
contraseña: Topicos2023
