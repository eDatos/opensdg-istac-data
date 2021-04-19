# Open SDG - Datos

Módulo que implementa el formato de datos de OpenSDG basado en el proyecto [open-sdg-data-starter](https://github.com/open-sdg/open-sdg-data-starter)


## Carga de datos y metadatos

El proceso de carga de ficheros en la plataforma OpenSDG se realiza mediante la creación de un fichero de datos y otro de metadatos por cada indicador que deseemos incluir.
Para cada indicador se definirá al menos un archivo CSV con los datos requeridos para poder representarlo en una gráfica y un archivo MD con los metadatos requeridos para poder representar dicho indicador.


### Nombre de los Archivos de Datos

Los datos se definen en un archivo CSV cuyo nombre ha de ser de la siguiente forma: **indicator_\$indicador.csv** siendo **\$indicador** el número de un indicador con la forma **\$M-\$O-\$I** tal que:
* **\$M** = Número de la meta.
* **\$O** = Código alfanumérico del objetivo.
* **\$I** = Código alfanumérico del indicador.

Además habrá que diferenciar las series que pertenecen a un indicador que tendrán un nombre con el siguiente formato: indicator_\$indicador-SERIE-\$serie siendo \$indicador  un número de indicador con el formato \$M-\$O-\$I y $serie siendo una letra mayúscula de la A a la Z.

### Contenido De los Archivos de Datos

Este archivo CSV ha de tener la siguiente estructura:

|year|units|[...]|value|
|:---:|:---:|:---:|:---:|
Año de los datos recogidos.<br>Esta columna es obligatoria.|Unidad en que se miden los datos presentados.<br>Esta columna es opcional.|Podremos añadir cuantas columnas queramos en medio de las obligatorias.|Valor del dato recogido.<br>Esta columna es obligatoria.

Además de estas columnas existen otras dos con un comportamiento especial dentro del software:

* **Serie**:  Define a que serie pertenece la fila en cuestión 	
* **Territorio**: Se puede desagregar la información por “Territorio” utilizando para esto los códigos NUTS2.

## Definiendo los Metadatos

### Nombre de los Metadatos

Los metadatos se definen en un archivo Markdown cuyo nombre ha de ser de la siguiente forma:
**\$indicador.md** siendo **\$indicador** el número de un indicador con la forma **\$M-\$O-\$I** siendo:

* **\$M** = Número de la meta.
* **\$O** = Código alfanumérico del objetivo.
* **\$I** = Código alfanumérico del indicador.

Además habrá que diferenciar las series que pertenecen a un indicador que tendrán un nombre con el siguiente formato: **\$indicador-SERIE-\$serie** siendo **\$indicador**  un número de indicador con el formato **\$M-\$O-\$I** y **\$serie** siendo una letra mayúscula de la A a la Z.

### Contenido de los Archivos de Metadatos
En esta sección hay que diferenciar entre los dos tipos de metadatos que vamos a encontrar.

#### Metadatos de Indicador
Los metadatos de indicador son aquellos que definen los indicadores de tres niveles (P.Ej.: 1-2-1, 4-a-2, etc.).
Estos indicadores tendrán los siguientes metadatos:

|Nombre|Definición|Tipo de dato|
|:---:|:---:|:---:|
data_non_statistical|Define si los datos de este indicador son estadísticos, y por tanto podemos mostrar una gráfica relacionada a ellos, o si no lo son|Valores booleanos (true, false)
goal_meta_link|Define un enlace a un documento asociado al indicador|Texto  entre comillas simples cuyo contenido sea un enlace al documento deseado
goal_meta_link_text|Define el texto que aparecerá en el enlace al documento definido en goal_meta_link|Texto
graph_title|Título del gráfico del indicador|Texto
graph_type|Tipo de gráfico que se podrá elegir entre *line* y *bar*. Por defecto para este tipo de indicadores se recomienda *line*|Texto
indicator_number|Número del indicador|Número de indicador en formato [**\$M.\$O.\$I**](#nombre-de-los-metadatos).<br>**Ojo**: Se utilizan puntos en lugar de guiones.
indicator_definition|Definición del indicador|Texto
indicator_name|Nombre del indicador|Texto
indicator_sort_order|Orden del indicador|Esto tendrá el siguiente formato:<br>\$MM-\$OO-\$II siguiendo el mismo formato de [**\$M-\$O-\$I**](#nombre-de-los-metadatos) pero asegurando que los números y caracteres alfanuméricos tengan un formato de doble dígito.<br>P.Ej.:<br>01-02-01 = 1-2-1<br>01-aa-02 = 1-a-2*<br>01-02-1a = 1-2-1a<br>*\* Cuidado de no representar las letras sueltas como 0a por ejemplo*
published|Define si el indicador está publicado o no|Valores booleanos (true, false)
reporting_status|Indica el estado del indicador, si sus datos están completos o no|Texto que tendrá uno de dos valores: **complete** o  **notstarted**
sdg_goal|Define el la Meta de Naciones Unidas al que se relaciona este indicador|Número natural entre comillas simples
target_name|Define el nombre del Objetivo de Naciones unidas al que se relaciona este indicador|Texto
target_id|Define el número del Objetivo de Naciones unidas al que se relaciona este indicador|Número con el formato [**\$M.\$O**](#nombre-de-los-metadatos) entre comillas simples. Ojo: Se utilizan puntos en lugar de guiones.
un_custodian_agency|Agencia de custodia del indicador|Texto
un_designated_tier|Importancia designada por Naciones Unidas|Número natural entre comillas simples
national_geographic_coverage|Que región cubre los datos mostrados en el indicador|Texto
source_active_N|Activa la fuente número N, siendo N un número natural entre el 1 y el 12|Valores booleanos (true, false)
source_organisation_N|Organización que provee los datos de la fuente N|Texto
source_url_N|Enlace a la web de la organización de la fuente N|Texto
source_url_text_N|Texto que aparecerá como enlace para la web de la fuente N|Texto
computation_units|Unidad de medida del indicador|Texto entre comillas
prev_indicator|Indicador previo. Utilizado para la navegación entre indicadores|Número de indicador con el formato [**\$M-\$O-\$I**](#nombre-de-los-metadatos)
next_indicator|Indicador siguiente. Utilizado para la navegación entre indicadores|Número de indicador con el formato [**\$M-\$O-\$I**](#nombre-de-los-metadatos)

#### Metadatos de Serie

|Nombre|Definición|Tipo de dato|
|:---:|:---:|:---:|
target_id|Número del indicador con el que está relacionada esta serie|Número con el formato [**\$M.\$O**](#nombre-de-los-metadatos) entre comillas simples. Ojo: Se utilizan puntos en lugar de guiones.
reporting_status|Similar a reporting_status en los indicadores|Texto que tendrá uno de dos valores: **complete** o  **notstarted**
data_non_statistical|Similar a data_non_statistical  en los indicadores|Valores booleanos (true, false)
indicator_sort_order|Similar a indicator_sort_order en los indicadores|Esto tendrá el siguiente formato:<br>\$MM-\$OO-\$II siguiendo el mismo formato de [**\$M-\$O-\$I**](#nombre-de-los-metadatos) pero asegurando que los números y caracteres alfanuméricos tengan un formato de doble dígito.<br>P.Ej.:<br>01-02-01 = 1-2-1<br>01-aa-02 = 1-a-2*<br>01-02-1a = 1-2-1a<br>*\* Cuidado de no representar las letras sueltas como 0a por ejemplo*
national_geographic_coverage|Similar a national_geographic_coverage en los indicadores|Texto
nombre|Nombre de la serie|Texto entre comillas simples
indicador_onu_global|Nombre del indicador de Naciones Unidas al que va relacionada esta serie|Texto
objetivo_global|Nombre del objetivo de Naciones Unidas al que va relacionada esta serie|Texto
meta_global|Nombre de la meta de Naciones Unidas a la que va relacionada esta serie|Texto
definicion|Definción de la serie|Texto entre comillas simples
formula_teorica|Fórmula teórica de la serie|Fórmula representada en formato [MathJax](https://www.mathjax.org/). P.Ej.: x^2 + y^2 = 3
unidad_medida|Unidad de medida en que se han recogido los datos de la serie|Texto
fuentes_información|Fuentes de información de las que se recogen los datos de esta serie|Texto
periodicidad|Periodicidad con la que se recogen datos para esta serie|Texto
observaciones|Observaciones a destacar para esta serie|Texto
graph_title|Similar a graph_title para el indicador|Texto
graph_type|Similar a graph_type para el indicador.<br>Para las series se recomienda utilizar *bar*|Texto
sort_order|Orden en que se mostrará la pestaña de este indicador en la agrupación de pestañas|Número natural mayor que 0
tab_name|Nombre que se le dará a la pestaña que representa esta serie|Texto
show_map|Metadato que se utiliza para mostrar o no el mapa|Valores booleanos (true, fals
### Mostrar la información en mapas

Para poder mostrar la información de un subindicador en un mapa será necesario realizar una serie de pasos:

1) En los archivos de datos se debe incluir una columna de nombre `GeoCode`. Bajo esta columna irán los códigos de regiones (`geocodes`) que mapearán los datos a las regiones del mapa.
2) En los metadatos del subindicador se deberá añadir un nuevo metadato: [**`show_map`**](#metadatos-de-serie) y establecerlo a `true` si se desea mostrar el mapa. Se puede establecer a `false` para ocultarlo.
3) Añadir configuraciones de mapa al archivo `config_data.yml`. Existen ejemplos de esto en el propio archivo. Para más información consultar la [documentación de OpenSDG](https://open-sdg.readthedocs.io/en/latest/maps/)
4) Esta configuración de los mapas se deberá añadir tal cual está en `config_data.yml` en la configuración de la web [`opensdg-web/src/_config.yml`](https://git.arte-consultores.com/istac/edatos-opensdg-web/blob/develop/opensdg-web/src/_config.yml).