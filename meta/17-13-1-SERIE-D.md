---

# Info genérica
target_id: '17.13.1'
reporting_status: complete
data_non_statistical: false
indicator_sort_order: 17-13-01-dd
national_geographical_coverage: Canarias

# Info de Subindicador
nombre: subindicator.17-13-1-SERIE-D-nombre
indicador_onu_global: global_indicators.17-13-1-title
meta_global: global_targets.17-13-title
objetivo_global: global_goals.17-title
definicion: subindicator.17-13-1-SERIE-D-definicion

formula_teorica: '$$PPIBVR^{t} = \frac{VR^{t}}{PIB^{t}} \cdot 100$$ <br>
donde: <br>
$VR^{t} $ volumen de remesas enviadas al extranjero en el año $t$ <br>
$PIB^{t} $ producto interior bruto a precios corrientes en el año $t$ <br>
Si denotamos: <br>
$VR_{España,p}^{t} $ volumen de remesas enviadas desde España en el año $t$ <br>
$P_{16-64,España,p}^{t} $ población extranjera entre 16 y 64 años del país $p$ residente en España a 1 de enero del año $t$ <br>
$P_{16-64,p}^{t} $ población extranjera entre 16 y 64 años del país $p$ residente en la comunidad autónoma a 1 de enero del año $t$ <br>
entonces: <br>
$$VR^{t} = \sum_{p \in Países} VR_{España,p}^{t} \cdot \frac{\frac{P_{16-64,p}^{t}+P_{16-64,p}^{t+1}}{2}}{\frac{P_{16-64,España,p}^{t}+P_{16-64,España,p}^{t+1}}{2}}$$ <br>
siendo $Países = {Rumanía, Marruecos, Senegal, Bolivia, Colombia, Ecuador, Honduras,$
$Nicaragua, Paraguay, Perú, República Dominicana, Pakistán, Resto\, de\, países}$, debiéndose tener en cuenta que en $P_{16-64,España,Resto de países}^{t}$ y $P_{16-64,Resto de países}^{t}$ no se considera a los países pertenecientes a la Unión Europea.'
unidad_medida: "Porcentaje"
fuentes_informacion: "Balanza de pagos, Banco de España<br>
Estadística del Padrón continuo, Instituto Nacional de Estadística (INE)<br>
Contabilidad regional de España, Instituto Nacional de Estadística (INE)"
periodicidad: "Anual"
observaciones: ""


# Info de Gráficas
graph_title: subindicator.17-13-1-SERIE-D-graph-title
graph_type: bar

# Info de navegación
sort_order: 4
tab_name: Serie D

#Coordinación con OCECAS
coordinado_con_ocecas: true

---