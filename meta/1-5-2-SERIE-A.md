---
target_id: 1.5.2
reporting_status: complete
data_non_statistical: false
indicator_sort_order: 01-05-02-aa
national_geographical_coverage: Canarias

nombre: subindicator.1-5-2-SERIE-A-nombre
indicador_onu_global: global_indicators.1-5-2-title
meta_global: global_targets.1-5-title
objetivo_global: global_goals.1-title
definicion: subindicator.1-5-2-SERIE-A-definicion

formula_teorica: '$$INDEMPIB^{t} = \frac{(IDP^{t}+IPP^{t}+IDB^{t})/IUIPC_{refT}^{t}}{PIB^{t}} \cdot 100 \quad \mathrm t=1,\dots,\mathrm T$$ <br>
$$IUIPC_{refT}^{T} = 1$$ <br>
$$IUIPC_{refT}^{t-1} = IUIPC_{refT}^{t} \cdot \frac{(100+TIPC_{dic}^{t})}{100} \quad \mathrm t=\mathrm T,\mathrm T-1,\dots,\mathrm 2$$ <br>
donde: <br>
$IDP^{t}$ indemnizaciones por daños personales pagadas y/o provisionadas en el año $t$ a precios del año $T$ <br>
$IPP^{t}$ indemnizaciones por pérdidas pecuniarias pagadas y/o provisionadas en el año $t$ a precios del año $T$ <br>
$IDB^{t}$ indemnizaciones por daños de bienes pagadas y/o provisionadas en el año $t$ a precios del año $T$ <br>
$IUIPC_{refT}^{t}$ índice unitario de la variación del IPC nacional en el año $t$ con referencia en el año $T$ <br>
$TIPC_{dic}^{t}$ tasa de variación anual del IPC nacional en el mes de diciembre del año $t$ <br>
$PIB^{t}$ producto interior bruto en términos corrientes en el año $t$'
unidad_medida: "Porcentaje"
fuentes_informacion: "Estadística de riesgos extraordinarios, Consorcio de Compensación de Seguros<br>
Contabilidad regional de España, Instituto Nacional de Estadística (INE)<br>
Índice de precios de consumo, Instituto Nacional de Estadística (INE)"
periodicidad: Anual
observaciones: "Las indemnizaciones se asignan al lugar y año de ocurrencia del siniestro, no incluyendo los siniestros ocurridos en el extranjero"

graph_title: subindicator.1-5-2-SERIE-A-graph-title
graph_type: bar

sort_order: 1
tab_name: 

coordinado_con_ocecas: true
---