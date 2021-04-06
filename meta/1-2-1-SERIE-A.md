---
# Info genérica
target_id: 1.2.1
reporting_status: complete
data_non_statistical: false
indicator_sort_order: 01-02-01-aa
national_geographical_coverage: Canarias

# Info de Subindicador
nombre: subindicator.1-2-1-SERIE-A-nombre
indicador_onu_global: global_indicators.1-2-1-title
meta_global: global_targets.1-2-title
objetivo_global: global_goals.1-title
definicion: subindicator.1-2-1-SERIE-A-definicion

# Fórmula teórica escrita en formato MathJax
# https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference
formula_teorica: '$$PPRPR_{NAC}^{t} = \frac{PRPR_{NAC}^{t}}{P^{t}} \cdot 100$$ <br>
donde: <br>
$PRPR_{NAC}^{t} =$ población en riesgo de pobreza relativa considerando el umbral nacional de pobreza (60% de la mediana nacional de los ingresos por unidad de consumo (escala OCDE modificada)) en el año $t$ <br>
$P^{t} =$ población total en el año  $t$'
unidad_medida: Porcentaje
fuentes_informacion: Encuesta de condiciones de vida, Instituto Nacional de Estadística (INE)
periodicidad: Anual
observaciones: "Los ingresos que se utilizan en el cálculo de este indicador corresponden al año anterior al de la encuesta. <br>
El número de unidades de consumo de un hogar se calcula utilizando la escala OCDE modificada, que asigna un peso de 1 a la primera persona de 14 o más años, un peso de 0,5 al resto de personas de 14 o más años y un peso de 0,3 a las personas de menos de 14 años."

# Info de Gráficas
graph_title: subindicator.1-2-1-SERIE-A-graph-title
graph_type: bar

# Info para las tabs
# Orden en que se mostrará esta tab...
sort_order: 1
# Nombre que tendrá la tab
tab_name: Serie A

#Coordinación con OCECAS
coordinado_con_ocecas: true
---