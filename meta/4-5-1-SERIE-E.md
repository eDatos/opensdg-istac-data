---

# Info genérica
target_id: '4.5.1'
reporting_status: complete
data_non_statistical: false
indicator_sort_order: 04-05-01-ee
national_geographical_coverage: Canarias

# Info de Subindicador
nombre: subindicator.4-5-1-SERIE-E-nombre
indicador_onu_global: global_indicators.4-5-1-title
meta_global: global_targets.4-5-title
objetivo_global: global_goals.4-title
definicion: subindicator.4-5-1-SERIE-E-definicion

formula_teorica: '$$IP_{\le 10.000/\gt 10.000}^{t} = \frac{PPE_{15-64,\le 10.000}^{t}}{PPE_{15-64,\gt 10.000}^{t}} \cdot 100$$ <br>
siendo: <br> 
$$PPE_{15-64,\le 10.000}^{t} = \frac{PE_{15-64,\le 10.000}^{t}}{P_{15-64,\le 10.000}^{t}} $$ <br>
$$PPE_{15-64,\gt 10.000}^{t} = \frac{PE_{15-64,\gt 10.000}^{t}}{P_{15-64,\gt 10.000}^{t}} $$ <br>
donde: <br>
$PE_{15-64,\le 10.000}^{t} =$ población entre 15 y 64 años residente en municipios de 10.000 o menos habitantes que ha realizado estudios o formación (reglada o no reglada) en las últimas cuatro semanas en el año $t$ <br>
$P_{15-64,\le 10.000}^{t} =$ población entre 15 y 64 años residente en municipios de 10.000 o menos habitantes en el año $t$<br>
$PE_{15-64,\gt 10.000}^{t} =$ población entre 15 y 64 años residente en municipios de más de 10.000 habitantes que ha realizado estudios o formación (reglada o no reglada) en las últimas cuatro semanas en el año $t$ <br>
$P_{15-64,\gt 10.000}^{t} =$ población entre 15 y 64 años residente en municipios de más de 10.000 habitantes en el año $t$<br>
teniendo en cuenta que cada una de estas poblaciones se calcula como la media aritmética de los cuatro trimestres del año'
unidad_medida: "Índice"
fuentes_informacion: "Encuesta de población activa, Instituto Nacional de Estadística (INE)"
periodicidad: "Anual"
observaciones: "El valor de referencia de este indicador es 100, que se tiene cuando la paridad es absoluta. El grado de disparidad es mayor cuanto más se aleja de 100 el valor del indicador, reflejando una situación desfavorable o favorable del grupo poblacional del numerador respecto al grupo poblacional del denominador según tome un valor inferior o superior a 100 respectivamente. A la hora de interpretar este indicador se debe tener en cuenta que no es simétrico en torno a 100."

# Info de Gráficas
graph_title: subindicator.4-5-1-SERIE-E-graph-title
graph_type: bar

# Info de navegación
sort_order: 5
tab_name: Serie E

#Coordinación con OCECAS
coordinado_con_ocecas: true

---