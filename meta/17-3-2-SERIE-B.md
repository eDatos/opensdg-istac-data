---

# Info genérica
target_id: '17.3.2'
reporting_status: complete
data_non_statistical: false
indicator_sort_order: 17-03-02-bb
national_geographical_coverage: Canarias

# Info de Subindicador
nombre: subindicator.17-3-2-SERIE-B-nombre
indicador_onu_global: global_indicators.17-3-2-title
meta_global: global_targets.17-3-title
objetivo_global: global_goals.17-title
definicion: subindicator.17-3-2-SERIE-B-definicion

formula_teorica: '$$VR^{t}$$ <br>
donde: <br>
$VR^{t} =$ volumen de remesas enviadas al extranjero en el año $t$<br>
Si denotamos:<br>
$VR_{España,p}^{t} =$ volumen de remesas enviadas desde España al país $p$<br>
$P_{16-64,España,p}^{t} =$ población extranjera entre 16 y 64 años del país p residente en España a 1 de enero del año $p$<br>
$P_{16-64,p}^{t} =$ población extranjera entre 16 y 64 años del país p residente en la comunidad autónoma a 1 de enero del año $p$<br>
Entonces: <br>
$$ VR^{t} = \displaystyle \sum_{p \epsilon Países} VR_{España,p}^{t} = \frac{\frac{P_{16-64,p}^{t}+P_{16-64,p}^{t+1}}{2}}{\frac{P_{16-64,España,p}^{t}+P_{16-64,España,p}^{t+1}}{2}} $$
siendo $Países = \{Colombia, Marruecos, Ecuador, República\;Dominicana, Honduras, Bolivia, Senegal, Paraguay,Pakistán, Rumanía, Resto\;de\;países\}$, debiéndose tener en cuenta que en $P_{16-64,España,Resto\;de\;países}$ y $P_{16-64,Resto\;de\;países}$ no se considera a los países pertenecientes a la Unión Europea.'
unidad_medida: "Millones de euros"
fuentes_informacion: "Balanza de pagos, Banco de España<br>
Estadística del Padrón continuo, Instituto Nacional de Estadística (INE)"
periodicidad: "Anual"
observaciones:

# Info de Gráficas
graph_title: subindicator.17-3-2-SERIE-B-graph-title
graph_type: bar

# Info de navegación
sort_order: 2
tab_name: Serie B

#Coordinación con OCECAS
coordinado_con_ocecas: true

---