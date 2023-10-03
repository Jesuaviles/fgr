# Importar las librerías necesarias
import streamlit as st
from PIL import Image

# Configurar el título de la aplicación
st.title("Planetometro")

# Crear una barra de navegación para seleccionar las páginas
page = st.sidebar.selectbox("Selecciona una página:", ["Página de Inicio", "Mercurio", "Venus", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno", "Contacto"])

# Definir el contenido de cada página
if page == "Página de Inicio":
    
    # Página de Inicio
    st.header("Bienvenido a nuestra calculadora de edad y peso según el planeta elegido")
    st.write("Esta app web te dice la edad y peso que tendrías en los planetas si hubieras nacido en ellos y estuvieras vivo para contarlo.")
    sistema_solar = Image.open("Sistema solar.png")
    st.image(sistema_solar)

elif page == "Mercurio":
    # Página de Mercurio
    st.header("Mercurio")
    st.write("Mercurio es el planeta del sistema solar más cercano al Sol y el más pequeño. Forma parte de los denominados planetas interiores y carece de satélites naturales al igual que Venus.")
    mercurio = Image.open("mercurio.png")
    st.image(mercurio)
    
    age_on_earth = st.number_input("Ingresa tu edad en años terrestres:", min_value=0)
    weight_on_earth = st.number_input("Ingresa tu peso en kilogramos:", min_value=0)
    
    age_on_mercury = age_on_earth / 0.24  # Años terrestres a años en Mercurio
    weight_on_mercury = weight_on_earth * 0.38  # Peso en kilogramos a peso en Mercurio
    
    st.write(f"Tu edad en Mercurio es aproximadamente {age_on_mercury:.2f} años.")
    st.write(f"Tu peso en Mercurio es aproximadamente {weight_on_mercury:.2f} kilogramos.")

elif page == "Venus":
    # Página de Venus
    st.header("Venus")
    st.write("Venus es el segundo planeta del sistema solar en orden de proximidad al Sol y el tercero más pequeño después de Mercurio y Marte. Al igual que Mercurio, carece de satélites naturales.")
    venus = Image.open("venus.png")
    st.image(venus)
    
    age_on_earth = st.number_input("Ingresa tu edad en años terrestres:", min_value=0)
    weight_on_earth = st.number_input("Ingresa tu peso en kilogramos:", min_value=0)
    
    age_on_venus = age_on_earth / 0.62  # Años terrestres a años en Venus
    weight_on_venus = weight_on_earth * 0.91  # Peso en kilogramos a peso en Venus
    
    st.write(f"Tu edad en Venus es aproximadamente {age_on_venus:.2f} años.")
    st.write(f"Tu peso en Venus es aproximadamente {weight_on_venus:.2f} kilogramos.")

elif page == "Marte":
    # Página de Marte
    st.header("Marte")
    st.write("Marte es el cuarto planeta en orden de distancia al Sol y el segundo más pequeño del sistema solar, después de Mercurio.")
    marte = Image.open("marte.png")
    st.image(marte)
    
    age_on_earth = st.number_input("Ingresa tu edad en años terrestres:", min_value=0)
    weight_on_earth = st.number_input("Ingresa tu peso en kilogramos:", min_value=0)
    
    age_on_mars = age_on_earth / 1.88  # Años terrestres a años en Marte
    weight_on_mars = weight_on_earth * 0.38  # Peso en kilogramos a peso en Marte
    
    st.write(f"Tu edad en Marte es aproximadamente {age_on_mars:.2f} años.")
    st.write(f"Tu peso en Marte es aproximadamente {weight_on_mars:.2f} kilogramos.")

    

elif page == "Júpiter":
    # Página de Júpiter
    st.header("Júpiter")
    st.write("Júpiter es el planeta más grande del sistema solar y el quinto en orden de lejanía al Sol. Es un gigante gaseoso que forma parte de los denominados planetas exteriores.")
    jupiter = Image.open("jupiter.png")
    st.image(jupiter)
    
    age_on_earth = st.number_input("Ingresa tu edad en años terrestres:", min_value=0)
    weight_on_earth = st.number_input("Ingresa tu peso en kilogramos:", min_value=0)
    
    age_on_jupiter = age_on_earth / 11.86  # Años terrestres a años en Júpiter
    weight_on_jupiter = weight_on_earth * 2.36  # Peso en kilogramos a peso en Júpiter
    
    st.write(f"Tu edad en Júpiter es aproximadamente {age_on_jupiter:.2f} años.")
    st.write(f"Tu peso en Júpiter es aproximadamente {weight_on_jupiter:.2f} kilogramos.")
    
elif page == "Saturno":
    # Página de Saturno
    st.header("Saturno")
    st.write("Saturno es el sexto planeta del sistema solar contando desde el Sol, el segundo en tamaño y masa después de Júpiter y el único con un sistema de anillos visible desde la Tierra.")
    saturno = Image.open("saturno.png")
    st.image(saturno)
    
    age_on_earth = st.number_input("Ingresa tu edad en años terrestres:", min_value=0)
    weight_on_earth = st.number_input("Ingresa tu peso en kilogramos:", min_value=0)
    
    age_on_saturn = age_on_earth / 29.46  # Años terrestres a años en Saturno
    weight_on_saturn = weight_on_earth * 0.92  # Peso en kilogramos a peso en Saturno
    
    st.write(f"Tu edad en Saturno es aproximadamente {age_on_saturn:.2f} años.")
    st.write(f"Tu peso en Saturno es aproximadamente {weight_on_saturn:.2f} kilogramos.")

elif page == "Urano":
    # Página de Urano
    st.header("Urano")
    st.write("Urano es el séptimo planeta del sistema solar, el tercero de mayor tamaño, y el cuarto más masivo.")
    urano = Image.open("urano.png")
    st.image(urano)
    
    age_on_earth = st.number_input("Ingresa tu edad en años terrestres:", min_value=0)
    weight_on_earth = st.number_input("Ingresa tu peso en kilogramos:", min_value=0)
    
    age_on_uranus = age_on_earth / 84.07  # Años terrestres a años en Urano
    weight_on_uranus = weight_on_earth * 0.89  # Peso en kilogramos a peso en Urano
    
    st.write(f"Tu edad en Urano es aproximadamente {age_on_uranus:.2f} años.")
    st.write(f"Tu peso en Urano es aproximadamente {weight_on_uranus:.2f} kilogramos.")

    

elif page == "Neptuno":
    # Página de Neptuno
    st.header("Neptuno")
    st.write("Neptuno es el octavo planeta en distancia respecto al Sol y el más lejano del sistema solar. Forma parte de los denominados planetas exteriores, y dentro de estos, es uno de los gigantes helados.")
    neptuno = Image.open("neptuno.png")
    st.image(neptuno)
    
    age_on_earth = st.number_input("Ingresa tu edad en años terrestres:", min_value=0)
    weight_on_earth = st.number_input("Ingresa tu peso en kilogramos:", min_value=0)
    
    age_on_neptune = age_on_earth / 164.81  # Años terrestres a años en Neptuno
    weight_on_neptune = weight_on_earth * 1.19  # Peso en kilogramos a peso en Neptuno
    
    st.write(f"Tu edad en Neptuno es aproximadamente {age_on_neptune:.2f} años.")
    st.write(f"Tu peso en Neptuno es aproximadamente {weight_on_neptune:.2f} kilogramos.")

    # Puedes agregar contenido adicional sobre Neptuno aquí

elif page == "Contacto":
    # Contacto
    st.header("Contacto:+56996434486")
    st.write("Equipo de desarrollo: Los Planetoides ")
    st.write("-Jesus Aviles")
    st.write("-Tomas Romero")
    st.write("-Said Romero")
    st.write("Curso: Cuatro azul medio")



# Footer con información adicional
st.sidebar.markdown("Hecho con ❤️ por Los Planetoides")

# Fin del código