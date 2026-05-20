import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================================
# FUNCIÓN CALCULAR EFICIENCIA
# =========================================

def calcular_eficiencia(df):

    df["eficiencia_remocion"] = (
        (df["DBO_entrada_mg_L"] - df["DBO_salida_mg_L"])
        / df["DBO_entrada_mg_L"]
    ) * 100

    return df

# =========================================
# FUNCIÓN RESUMEN POR PLANTA
# =========================================

def resumen_por_planta(df):

    resumen = df.groupby("planta").agg({
        "caudal_entrada_m3_d": "mean",
        "DBO_entrada_mg_L": "mean",
        "DBO_salida_mg_L": "mean",
        "eficiencia_remocion": "mean",
        "energia_aeracion_kWh": "mean"
    }).round(2)

    return resumen

# =========================================
# FUNCIÓN GENERAR DASHBOARD
# =========================================

def generar_dashboard(resumen):

    plt.figure(figsize=(14,6))

    plt.subplot(1,2,1)

    sns.barplot(
        x=resumen.index,
        y=resumen["eficiencia_remocion"]
    )

    plt.title("Eficiencia promedio por planta")

    plt.subplot(1,2,2)

    sns.barplot(
        x=resumen.index,
        y=resumen["DBO_salida_mg_L"]
    )

    plt.title("DBO salida promedio")

    plt.tight_layout()

    plt.savefig(
        "dashboard/dashboard_modular.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

# =========================================
# FUNCIÓN EXPORTAR REPORTES
# =========================================

def exportar_reportes(df):

    df.to_excel(
        "reportes/reporte_modular.xlsx",
        index=False
    )

    print("Reporte exportado correctamente")