---

# Info genérica
target_id: '4.5.1'
reporting_status: complete
data_non_statistical: false
indicator_sort_order: 04-05-01-bb
national_geographical_coverage: Canarias

# Info de Subindicador
nombre: subindicator.4-5-1-SERIE-B-nombre
indicador_onu_global: global_indicators.4-5-1-title
meta_global: global_targets.4-5-title
objetivo_global: global_goals.4-title
definicion: subindicator.4-5-1-SERIE-B-definicion

formula_teorica: '$$IP_{\lt 900/\ge 2.500}^{t} = \frac{PPE_{18-64,\lt 900}^{t}}{PPE_{18-64,\ge 2.500}^{t}}$$ <br>
siendo: <br> 
$$PPE_{18-64,\lt 900}^{t} = \frac{PE_{18-64,\lt 900}^{t}}{P_{18-64,\lt 900}^{t}}  \cdot 100$$ <br>
$$PPE_{18-64,\ge 2.500}^{t} = \frac{PE_{18-64,\ge 2.500}^{t}}{P_{18-64,\ge 2.500}^{t}}  \cdot 100$$ <br>
donde: <br>
$PE_{18-64,\lt 900}^{t} =$ población entre 18 y 64 años perteneciente a hogares con ingresos mensuales netos de menos de 900 euros que ha realizado actividades educativas (formales o no formales) en los últimos 12 meses en el año $t$ <br>
$P_{18-64,\lt 900}^{t} =$ población entre 18 y 64 años perteneciente a hogares con ingresos mensuales netos de menos de 900 euros en el año $t$<br>
$PE_{18-64,\ge 2.500}^{t} =$ población entre 18 y 64 años perteneciente a hogares con ingresos mensuales netos de 2.500 o más euros que ha realizado actividades educativas (formales o no formales) en los últimos 12 meses en el año $t$ <br>
$P_{18-64,\ge 2.500}^{t} =$ población entre 18 y 64 años perteneciente a hogares con ingresos mensuales netos de 2.500 o más euros en el año $t$<br>'
unidad_medida: "Índice"
fuentes_informacion: "Encuesta sobre la participación de la población adulta en las actividades de aprendizaje, Instituto Nacional de Estadística (INE)"
periodicidad: "Quinquenal"
observaciones: "El valor de referencia de este indicador es 1, que se tiene cuando la paridad es absoluta. El grado de disparidad es mayor cuanto más se aleja de 1 el valor del indicador, reflejando una situación desfavorable o favorable del grupo poblacional del numerador respecto al grupo poblacional del denominador según tome un valor inferior o superior a 1 respectivamente. A la hora de interpretar este indicador se debe tener en cuenta que no es simétrico en torno a 1."

# Info de Gráficas
graph_title: subindicator.4-5-1-SERIE-B-graph-title
graph_type: bar

# Info de navegación
sort_order: 2
tab_name: Serie B

#Coordinación con OCECAS
coordinado_con_ocecas: true

---