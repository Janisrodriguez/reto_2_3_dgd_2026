# 🎓 Reto de Ingeniería: Módulo 1

**Diplomado en Estrategias de Datos - USTA**

## 🎯 Objetivo General
Dejar de usar Python como una "calculadora gigante" y empezar a usarlo como una herramienta de Ingeniería de Datos. Optimizarás el consumo de memoria, vectorizarás operaciones lentas y crearás visualizaciones profesionales orientadas a la toma de decisiones.

## 🛠 Requisitos de Entrega
* **Formato:** Un único archivo Jupyter Notebook (`.ipynb`).
* **Nomenclatura:** `Reto_Modulo_Pandas_Nombre_Apellido.ipynb` o `Reto_Modulo_Visualización_Nombre_Apellido.ipynb`.
* **Fecha de Entrega:** 03-01-2026.
* **Estructura:** El código debe estar intercalado con celdas de **Markdown** explicando tus hallazgos (Storytelling).

## 🚀 Desafíos a Cubrir

### Parte A: Pandas Pro (Optimización)
Debes demostrar que puedes reducir el tamaño del dataset en memoria al menos un **50%** sin perder información.
1.  Diagnóstico de memoria real (`deep`).
2.  Downcasting de tipos numéricos (`int64` -> `int8/16`).
3.  Conversión de objetos a `Category`.
4.  Ingeniería de variables vectorizada (Fechas y Geoespacial).

### Parte B: Visualización Pro (Storytelling)
Debes generar gráficos que cuenten una historia, no solo que muestren datos.
1.  Manejo de *Overplotting* en mapas y scatters.
2.  Uso de escalas logarítmicas para distribuciones sesgadas.
3.  Limpieza de "Chartjunk" (tinta innecesaria).
4.  **Capstone:** Generación automática de un reporte PDF integrando tus hallazgos.

---
**Recursos:**
Asegúrate de haber leído `DATASET_INFO.md` para obtener los datos necesarios antes de comenzar.

---

### 📓 Estructura Sugerida del Jupyter Notebook

Para ayudar a los estudiantes a empezar con el pie derecho, puedes incluir esta **plantilla de estructura** en el repositorio o enviársela como guía. Esto asegura que todos sigan un orden lógico.

#### Estructura del Cuaderno (`Template_Reto.ipynb`)

**Celda 1 (Markdown) - Encabezado:**

```markdown
# 🚀 Reto de Ingeniería de Datos: Optimización y Visualización
**Diplomado en Estrategias de Datos - USTA**
* **Estudiante:** [Tu Nombre]
* **Fecha:** [Fecha]

**Descripción:** En este cuaderno aplico técnicas de *downcasting*, vectorización y visualización avanzada sobre el dataset de Taxis de NYC (1.4M registros).

```

**Celda 2 (Código) - Configuración Inicial:**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF

# Configuración para que los gráficos se vean bien en retina display
%config InlineBackend.figure_format = 'retina'
sns.set_theme(style="whitegrid")

# Ocultar advertencias molestas (opcional)
import warnings
warnings.filterwarnings('ignore')

```

**Celda 3 (Markdown/Código) - Carga y Diagnóstico (El "Antes"):**

* **Markdown:** "Cargamos el dataset sin optimizar y analizamos su peso en RAM."
* **Código:** `df = pd.read_csv('train.csv')` y `df.info(memory_usage='deep')`.

**Celda 4 (Markdown/Código) - Fase 1: Optimización (Pandas Pro):**

* *Aquí el estudiante desarrolla los puntos de conversión de tipos (int8, category) y muestra la reducción de memoria lograda (El "Después").*

**Celda 5 (Markdown/Código) - Fase 2: Ingeniería de Variables:**

* *Cálculos vectorizados de fechas (dt.hour) y distancias (Haversine).*
* *Uso de `.query()` y `.assign()`.*

**Celda 6 (Markdown/Código) - Fase 3: Visualización Avanzada:**

* *Subsección: Distribuciones.* (Histogramas logarítmicos).
* *Subsección: Análisis Geoespacial.* (Scatter plots con Alpha y Hexbins).
* *Subsección: Relaciones Temporales.* (Heatmaps de Día vs Hora).

**Celda 7 (Markdown/Código) - Fase 4: Reporte Automatizado (Capstone):**

* *Código para generar los assets (imágenes .png) temporales.*
* *Código de FPDF para compilar el PDF final.*

**Celda 8 (Markdown) - Conclusiones:**

```markdown
## 💡 Conclusiones y Hallazgos
1. **Memoria:** Se logró reducir el dataset de X GB a Y MB.
2. **Patrones:** Se detectó que el tráfico es más pesado en...
3. **Técnica:** La vectorización redujo el tiempo de procesamiento en un X%.

```
