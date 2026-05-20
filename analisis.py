import matplotlib
matplotlib.use('TkAgg')

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Crear carpetas
os.makedirs("dashboard", exist_ok=True)
os.makedirs("reportes", exist_ok=True)
os.makedirs("evidencias", exist_ok=True)

# Función para guardar tablas como imagen
def guardar_tabla_imagen(dataframe, titulo, nombre_archivo):
    fig, ax = plt.subplots(figsize=(14, 4))
    ax.axis("off")

    tabla = ax.table(
        cellText=dataframe.values,
        colLabels=dataframe.columns,
        loc="center",
        cellLoc="center"
    )

    tabla.auto_set_font_size(False)
    tabla.set_fontsize(9)
    tabla.scale(1.2, 1.5)

    plt.title(titulo, fontsize=14, fontweight="bold")

    ruta = f"evidencias/{nombre_archivo}.png"

    plt.savefig(
        ruta,
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

# Cargar dataset
df = pd.read_excel("data/dataset_set_A_aguas_residuales.xlsx")

# Evidencia 1: carga del dataset
datos_iniciales = df.head()

guardar_tabla_imagen(
    datos_iniciales,
    "Evidencia 1 - Carga inicial del dataset",
    "evidencia_01_carga_dataset"
)

# Evidencia 2: información general
info_dataset = pd.DataFrame({
    "Columna": df.columns,
    "Tipo de dato": df.dtypes.astype(str).values,
    "Valores no nulos": df.notnull().sum().values,
    "Valores nulos": df.isnull().sum().values
})

guardar_tabla_imagen(
    info_dataset,
    "Evidencia 2 - Información general del dataset",
    "evidencia_02_info_dataset"
)

# Evidencia 3: valores nulos
valores_nulos = df.isnull().sum().reset_index()
valores_nulos.columns = ["Columna", "Cantidad de valores nulos"]

guardar_tabla_imagen(
    valores_nulos,
    "Evidencia 3 - Valores nulos por columna",
    "evidencia_03_valores_nulos"
)

# Cálculo de eficiencia
df["eficiencia_remocion"] = (
    (df["DBO_entrada_mg_L"] - df["DBO_salida_mg_L"])
    / df["DBO_entrada_mg_L"]
) * 100

# Resumen por planta
resumen = df.groupby("planta").agg({
    "caudal_entrada_m3_d": "mean",
    "DBO_entrada_mg_L": "mean",
    "DBO_salida_mg_L": "mean",
    "eficiencia_remocion": "mean",
    "energia_aeracion_kWh": "mean"
}).round(2)

resumen_tabla = resumen.reset_index()

guardar_tabla_imagen(
    resumen_tabla,
    "Evidencia 4 - Resumen promedio por planta",
    "evidencia_04_resumen_planta"
)

# Dashboard
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.barplot(
    x=resumen.index,
    y=resumen["eficiencia_remocion"]
)
plt.title("Eficiencia promedio por planta")
plt.ylabel("Eficiencia (%)")
plt.xlabel("Planta")

plt.subplot(1, 2, 2)
sns.barplot(
    x=resumen.index,
    y=resumen["DBO_salida_mg_L"]
)
plt.title("DBO salida promedio por planta")
plt.ylabel("DBO mg/L")
plt.xlabel("Planta")

plt.tight_layout()

plt.savefig(
    "dashboard/dashboard_completo.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    "evidencias/evidencia_05_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Exportar reportes Excel
df[[
    "fecha_registro",
    "planta",
    "caudal_entrada_m3_d",
    "DBO_entrada_mg_L",
    "DBO_salida_mg_L",
    "energia_aeracion_kWh",
    "lodos_generados_kg_d"
]].to_excel(
    "reportes/reporte_operaciones.xlsx",
    index=False
)

df[[
    "fecha_registro",
    "planta",
    "DBO_salida_mg_L",
    "cumplimiento_norma"
]].to_excel(
    "reportes/reporte_gestion_ambiental.xlsx",
    index=False
)

# Evidencia 6: archivos generados
archivos_generados = pd.DataFrame({
    "Archivo generado": [
        "dashboard/dashboard_completo.png",
        "reportes/reporte_operaciones.xlsx",
        "reportes/reporte_gestion_ambiental.xlsx",
        "evidencias/evidencia_01_carga_dataset.png",
        "evidencias/evidencia_02_info_dataset.png",
        "evidencias/evidencia_03_valores_nulos.png",
        "evidencias/evidencia_04_resumen_planta.png",
        "evidencias/evidencia_05_dashboard.png"
    ],
    "Descripción": [
        "Dashboard exploratorio del proyecto",
        "Reporte para el área de Operaciones",
        "Reporte para el área de Gestión Ambiental",
        "Primeras filas del dataset",
        "Tipos de datos, registros no nulos y nulos",
        "Revisión de valores nulos por columna",
        "Resumen promedio por planta de tratamiento",
        "Dashboard final guardado como imagen"
    ]
})

guardar_tabla_imagen(
    archivos_generados,
    "Evidencia 6 - Archivos generados por el análisis",
    "evidencia_06_archivos_generados"
)

print("PROCESO FINALIZADO CORRECTAMENTE")