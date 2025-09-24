import streamlit as st

# Estructura de datos extraída del Excel
vias = {
    "Vía 1": ["PRUEBA 470-102"],
    "Vía 2": ["PRUEBA 490-006"],
    "Vía 3": ["ACOPLE 465-237"],
    "Vía 4": ["AGUAS NEGRAS 470-117"],
    "Vía 5": ["FOSO 1", "470-117", "PUESTO 3", "PUESTO 4"],
    "Vía 5": ["490-005 CMT", "490-005 CMP", "490-005 CR", "490-009 CR"],
    "Vía 6": ["470-102 CM", "470-102 RI", "470-102 RC", "C4"],
    "Vía 7": ["490-004 CR", "490-004 CMP", "490-004 CMT", "C6", "C6"],
    "Vía 8": ["470-103 RI", "470-103 CM", "470-103 RC", "AMI. PLAYA"],
    "Vía 9": ["OFF - ALSTOM", "464-207", "464-207", "464-207"],
    "Vía 10": ["465-236 C1", "465-236 C3", "465-236 C5", "C10"],
    "vÍA 11 PREPARACIÓN DE CAJA": ["464-224 C3"],
    "Vía 12": ["464-207 ALSTOM ACCIDENTE"],
    "Vía 13": ["SCHAFENBERG / PANTOGRAFOS"],
    "Vía 14": ["BOGIES", "", "C18", "C18"],
    "Vía 15": ["APARALLAJE", "AMORTIGUADORES", "VERIFICADO"],
    "Vía 16": ["VÍA DE PASO"],
    "Vía 17": ["VÍA DE PASO"],
    "Vía 18 CABINA DE PINTURA": ["470-103"],
}

st.set_page_config(page_title="Plano Interactivo de Taller", layout="wide")
st.title("Plano Interactivo de Situación de Coches en Taller")

st.markdown("""
Arrastra y suelta los bloques de coches entre vías para planificar movimientos. Haz doble clic en un bloque para editar su nombre.
""")

# Estado de la app
if "vias" not in st.session_state:
    st.session_state.vias = vias

# Mostrar cada vía como una fila de bloques
for via, coches in st.session_state.vias.items():
    st.subheader(via)
    cols = st.columns(len(coches) + 1 if coches else 2)
    for idx, coche in enumerate(coches):
        with cols[idx]:
            new_name = st.text_input(f"{via}-{idx}", coche, key=f"{via}-{idx}")
            st.session_state.vias[via][idx] = new_name
    # Añadir nuevo coche
    with cols[-1]:
        if st.button(f"Añadir coche a {via}"):
            st.session_state.vias[via].append("Nuevo coche")

# Guardar y descargar
if st.button("Descargar situación actual"):
    import pandas as pd
    data = []
    for via, coches in st.session_state.vias.items():
        for coche in coches:
            data.append({"Vía": via, "Coche": coche})
    df = pd.DataFrame(data)
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Descargar CSV", csv, "situacion_taller.csv", "text/csv")

