# Plano Interactivo de Situación de Coches en Taller

Esta aplicación web desarrollada con **Streamlit** permite visualizar y gestionar de forma interactiva la situación de coches (vagones) en un taller ferroviario. Cada coche se representa como un bloque dentro de su vía correspondiente, permitiendo al jefe de producción planificar movimientos, editar información y descargar el estado actual.

## 🚆 Distribución del Taller

El plano se basa en un archivo Excel con la siguiente distribución de vías:

- **Vías 1 y 2**: Nave de Pruebas
- **Vías 3 y 4**: Nave de Paso
- **Vías 5 a 13**: Taller de Reparaciones
- **Vías 14 y 15**: Bogies
- **Vías 16 a 18**: Nave de Paso 2

### Zonas adicionales:
- **Lado Málaga**: Naves auxiliares
- **Lado Córdoba**: Vías de desguace, excepto:
  - Vía 15 y 16: Lavadero
  - Vía 17: Cabina de Pintura

## 🧩 Funcionalidades

- Visualización por bloques de cada coche en su vía.
- Edición de nombre de cada coche.
- Añadir nuevos coches a cualquier vía.
- Descargar el estado actual en formato CSV.
- Acceso desde cualquier navegador mediante enlace público.

## 🚀 Cómo desplegar en Streamlit Cloud

1. Crea una cuenta en [Streamlit Cloud](https://streamlit.ioApp**.
3. Selecciona este repositorio.
4. En el campo `Main file path`, escribe: `app.py`.
5. Haz clic en **Deploy**.

## 📁 Estructura del repositorio
plano-taller-streamlit ┣ 📄 app.py ┣ 📄 README.md

## ✍️ Autor

Miguel Soler – Jefe de Producción


