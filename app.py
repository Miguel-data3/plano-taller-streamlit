import streamlit as st

# Estructura de datos extraída del Excel
vias = {
    "Vía 1": ["PRUEBA 470-102"],
    "Vía 2": ["PRUEBA 490-006"],
    "Vía 3": ["ACOPLE 465-237"],
    "Vía 4": ["AGUAS NEGRAS 470-117"],
    "Vía 5": ["FOSO 1", "470-117", "PUESTO 3", "PUESTO 4", "DESGUACE:" "C2", "7-446-078 RI", "ARCO 2.209", "C2", "7-446-078 RI", "ARCO 2.209"],
    "Vía 4": ["4"],
    "Vía 5": ["490-005 CMT", "490-005 CMP", "490-005 CR", "490-009 CR", "C2", "7-446-078 RI", "ARCO 2.209", "C2", "7-446-078 RI", "ARCO 2.209"],
    "Vía 6": ["470-102 CM", "470-102 RI", "470-102 RC", "C4", "^^ 9-446-078 CM1", "9-446-078 CM2 ^^", "C4", "^^ 9-446-078 CM1", "9-446-078 CM2 ^^"],
    "Vía 7": ["490-004 CR", "490-004 CMP", "490-004 CMT", "C6", "C6"],
    "Vía 8": ["470-103 RI", "470-103 CM", "470-103 RC", "AMI. PLAYA", "C8", "AMI. PLAYA", "C8"],
    "Vía 9": ["OFF - ALSTOM", "464-207", "464-207", "464-207", "AMI. MONTE", "C9", "AMI. MONTE", "C9"],
    "Vía 10": ["465-236 C1", "465-236 C3", "465-236 C5", "C10", "ARCO 2.201", "C10", "ARCO 2.201"],
    "Vía 11": ["C12", "ARCO 2.204", "C12", "ARCO 2.204"],
    "Vía 12": ["465-228 C3", "465-228 C5", "465-228 C4", "465-228 C2", "465-228 C1", "C15", "C15"],
    "Vía 13": ["SCHAFENBERG / PANTOGRAFOS", "C17", "C17"],
    "Vía 14": ["BOGIES", "", "C18", "C18"],
    "Vía 15": ["APARALLAJE", "AMORTIGUADORES", "VERIFICADO"],
    "Vía 16": [],
    "Vía 17": [],
    "Vía 18": [],
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

