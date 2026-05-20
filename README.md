# AquaLimpia

Proyecto de ciencia de datos para análisis operacional y ambiental de plantas de tratamiento de aguas residuales.

---

# Objetivo del proyecto

Analizar el desempeño de las plantas de tratamiento de AquaLimpia S.A. mediante técnicas de ciencia de datos, permitiendo evaluar eficiencia operacional, cumplimiento normativo y comportamiento de indicadores ambientales.

---

# Problemática abordada

La empresa AquaLimpia S.A. presenta incumplimientos intermitentes relacionados con parámetros ambientales asociados a la Demanda Biológica de Oxígeno (DBO), afectando el monitoreo operacional y el cumplimiento regulatorio.

---

# Herramientas utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Visual Studio Code
- GitHub

---

# Estructura del proyecto

AquaLimpia/
│
├── data/
├── dashboard/
├── evidencias/
├── reportes/
├── analisis.py
└── README.md

---

# Proceso analítico

## 1. Carga de datos

Se realizó la lectura del dataset en formato Excel utilizando Pandas.

## 2. Calidad de datos

Se revisaron:
- tipos de datos,
- registros,
- valores nulos,
- consistencia general.

## 3. Cálculo de métricas

Se calculó la eficiencia de remoción utilizando los valores de DBO de entrada y salida.

## 4. Análisis exploratorio

Se construyó un dashboard para comparar:
- eficiencia promedio,
- DBO salida,
- comportamiento por planta.

## 5. Exportación de reportes

Se generaron reportes diferenciados para:
- Operaciones,
- Gestión Ambiental.

---

# Resultados obtenidos

El análisis permitió:
- identificar diferencias de desempeño entre plantas,
- evaluar eficiencia promedio de remoción,
- detectar posibles incumplimientos,
- generar reportes automáticos,
- y visualizar indicadores mediante dashboards.

---

# Dashboard generado

El dashboard exploratorio fue almacenado en:

dashboard/dashboard_completo.png

---

# Reportes generados

- reporte_operaciones.xlsx
- reporte_gestion_ambiental.xlsx

---

# Repositorio GitHub

Repositorio del proyecto:

https://github.com/CristianIACC-1992/AquaLimpia

---

# Conclusión

La documentación técnica desarrollada facilita la comprensión, reutilización y mantenimiento del proyecto de ciencia de datos, permitiendo que futuras ejecuciones del análisis puedan realizarse de manera ordenada, reproducible y colaborativa.