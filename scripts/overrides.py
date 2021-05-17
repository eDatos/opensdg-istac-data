"""
Este script sobreescribe algunas de las funcionaldiades de sdg_build para adaptarse a los requisitos del cliente.
https://github.com/open-sdg/sdg-build
"""
import json
from zipfile import ZipFile
import humanize
import re
import os
import sdg
from sdg import open_sdg
from sdg import IndicatorExportService
from sdg.outputs import OutputOpenSdg
from sdg.data import write_csv
from sdg.json import write_json, df_to_list_dict

INDEX_NAME = "indice.csv"


"""
Sobreescritura de IndicatorExportService
https://github.com/open-sdg/sdg-build/blob/1.0.0/sdg/IndicatorExportService.py
"""
class OVRIndicatorExportService(IndicatorExportService):
    def __init__(self, site_directory, indicators):
        """Constructor for IndicatorExportService.

        Parameters
        ----------
        site_directory : string
            Path to an already-performed build. The files to be zipped are
            assumed to be in a "data" subfolder.
        indicators : dict
            A dict of Indicator objects, keyed by indicator id.
        """
        self.__site_directory = site_directory
        self.__zip_directory = "%s/zip" % site_directory
        self.__data_directory = "%s/data" % site_directory
        self.__indicators = indicators

    def export_all_indicator_data_as_zip_archive(self):
        self.__create_zip_folder_at_site_directory()
        csv_files = self.__get_all_indicator_csv_files()
        self.__create_zip_file("all_indicators.zip", csv_files)

    def __create_zip_folder_at_site_directory(self):
        directory = "%s/zip" % self.__site_directory
        if not os.path.exists(directory):
            os.mkdir(directory)

    # Modificado
    def __get_all_indicator_csv_files(self):
        all_data_file_names = os.listdir(self.__data_directory)
        all_data_file_names = filter(lambda l: re.search(r".*SERIE.*\.csv", l) or l == INDEX_NAME, all_data_file_names)
        csv_data_file_names = []
        for file_name in all_data_file_names:
            if self.__file_is_suitable_for_export(file_name):
                csv_data_file_names.append(file_name)

        csv_data_files = []
        for each_file_name in csv_data_file_names:
            csv_data_files.append({
                "file_name": each_file_name,
                "path": "%s/%s" % (self.__data_directory, each_file_name)
            })
        
        csv_data_files.append({
            "file_name": INDEX_NAME,
            "path": "%s/%s" % ('data', INDEX_NAME)
        })

        return csv_data_files

    def __file_is_suitable_for_export(self, file_name):
        indicator_id = file_name.split('.')[0]
        if indicator_id not in self.__indicators:
            raise KeyError("Could not check whether %s is suitable for export." % indicator_id)
        suitable = True
        suitable = suitable & self.__file_is_csv(file_name)
        suitable = suitable & self.__indicators[indicator_id].is_complete()
        suitable = suitable & self.__indicators[indicator_id].is_statistical()
        return suitable

    def __file_is_csv(self, file_name):
        return file_name.endswith(".csv")

    def __create_zip_file(self, zip_file_name, files_to_include):
        zip_file = ZipFile("%s/%s" % (self.__zip_directory, zip_file_name), "w")

        for each_file in files_to_include:
            zip_file.write(each_file["path"], each_file["file_name"])

        zip_file.close()

        self.__save_zip_file_info(zip_file_name)

    def __save_zip_file_info(self, zip_file_name):
        info = self.__get_zip_file_info(zip_file_name)
        json_file_name = zip_file_name.replace('.zip', '.json')
        with open(os.path.join(self.__zip_directory, json_file_name), 'w') as f:
            json.dump(info, f)

    def __get_zip_file_info(self, zip_file_name):
        size = self.__get_zip_file_size(zip_file_name)
        info = {
            'size_bytes': size,
            'size_human': humanize.naturalsize(size),
            #'timestamp': str(datetime.datetime.now())
        }
        return info

    def __get_zip_file_size(self, zip_file_name):
        st = os.stat(os.path.join(self.__zip_directory, zip_file_name))
        return st.st_size


"""
Sobreescritura de OutputOpenSdg
https://github.com/open-sdg/sdg-build/blob/1.0.0/sdg/outputs/OutputOpenSdg.py
"""
class OVROutputOpenSdg(OutputOpenSdg):
    def build(self, language=None):
        """Write the JSON output expected by Open SDG. Overrides parent."""
        status = True
        all_meta = dict()
        all_headline = dict()
        site_dir = self.output_folder

        # Write the schema.
        schema_output = sdg.schemas.SchemaOutputOpenSdg(schema=self.schema)
        schema_output_folder = os.path.join(site_dir, 'meta')
        schema_output.write_schema(output_folder=schema_output_folder, filename='schema.json')

        # Write the translations.
        translation_output = sdg.translations.TranslationOutputJson(self.translations)
        translation_folder = os.path.join(site_dir, 'translations')
        translation_output.write_translations(
            language=language,
            output_folder=translation_folder,
            filename='translations.json'
        )

        for indicator_id in self.get_indicator_ids():
            indicator = self.get_indicator_by_id(indicator_id).language(language)
            # Output all the csvs
            status = status & write_csv(indicator_id, indicator.data, ftype='data', site_dir=site_dir)
            status = status & write_csv(indicator_id, indicator.edges, ftype='edges', site_dir=site_dir)
            status = status & write_csv(indicator_id, indicator.headline, ftype='headline', site_dir=site_dir)
            # And JSON
            data_dict = df_to_list_dict(indicator.data, orient='list')
            edges_dict = df_to_list_dict(indicator.edges, orient='list')
            headline_dict = df_to_list_dict(indicator.headline, orient='records')

            status = status & write_json(indicator_id, data_dict, ftype='data', gz=False, site_dir=site_dir)
            status = status & write_json(indicator_id, edges_dict, ftype='edges', gz=False, site_dir=site_dir)
            status = status & write_json(indicator_id, headline_dict, ftype='headline', gz=False, site_dir=site_dir)

            # combined
            comb = {'data': data_dict, 'edges': edges_dict}
            status = status & write_json(indicator_id, comb, ftype='comb', gz=False, site_dir=site_dir)

            # Metadata
            status = status & sdg.json.write_json(indicator_id, indicator.meta, ftype='meta', site_dir=site_dir)

            # Append to the build-time "all" output
            all_meta[indicator_id] = indicator.meta
            all_headline[indicator_id] = headline_dict

        status = status & sdg.json.write_json('all', all_meta, ftype='meta', site_dir=site_dir)
        status = status & sdg.json.write_json('all', all_headline, ftype='headline', site_dir=site_dir)

        stats_reporting = sdg.stats.reporting_status(self.schema, all_meta, self.reporting_status_grouping_fields)
        status = status & sdg.json.write_json('reporting', stats_reporting, ftype='stats', site_dir=site_dir)

        indicator_export_service = OVRIndicatorExportService(site_dir, self.indicators)
        indicator_export_service.export_all_indicator_data_as_zip_archive()

        return(status)


"""
Sobreescritura de open_sdg_prep
https://github.com/open-sdg/sdg-build/blob/1.0.0/sdg/open_sdg.py#L156
"""
def ovr_open_sdg_prep(options):
    """Prepare Open SDG output for validation and builds.

    Args:
        options: Dict of options.

    Returns:
        List of the prepared OutputBase objects.
    """
    # Set defaults for the mutable parameters.
    if 'languages' in options and options['languages'] is None:
        options['languages'] = []

    # Combine the inputs into one list.
    inputs = [open_sdg.open_sdg_input_from_dict(input_dict, options) for input_dict in options['inputs']]

    # Do any data/metadata alterations.
    if callable(options['alter_data']):
        for input in inputs:
            input.add_data_alteration(options['alter_data'])
    if callable(options['alter_meta']):
        for input in inputs:
            input.add_meta_alteration(options['alter_meta'])

    # Use a Prose.io file for the metadata schema.
    schema_path = os.path.join(options['src_dir'], options['schema_file'])
    schema = sdg.schemas.SchemaInputOpenSdg(schema_path=schema_path)

    # Indicate any extra fields for the reporting stats, if needed.
    reporting_status_extra_fields = []
    if 'reporting_status_extra_fields' in options:
        reporting_status_extra_fields = options['reporting_status_extra_fields']

    # Create an "output" from these inputs/schema/translations, for Open SDG output.
    opensdg_output = OVROutputOpenSdg(
        inputs=inputs,
        schema=schema,
        output_folder=options['site_dir'],
        translations=options['translations'],
        reporting_status_extra_fields=reporting_status_extra_fields,
        indicator_options=options['indicator_options'])

    outputs = [opensdg_output]

    # If there are any map layers, create some OutputGeoJson objects.
    for map_layer in options['map_layers']:
        geojson_kwargs = {
            'inputs': inputs,
            'schema': schema,
            'output_folder': options['site_dir'],
            'translations': options['translations'],
            'indicator_options': options['indicator_options'],
            'id_column': options['geo_code_column'],
        }
        for key in map_layer:
            geojson_kwargs[key] = map_layer[key]
        # If the geojson_file parameter is not remote, make sure it uses src_dir.
        if not geojson_kwargs['geojson_file'].startswith('http'):
            geojson_file = os.path.join(options['src_dir'], geojson_kwargs['geojson_file'])
            geojson_kwargs['geojson_file'] = geojson_file
        # Create the output.
        outputs.append(sdg.outputs.OutputGeoJson(**geojson_kwargs))

    return outputs


open_sdg.open_sdg_prep = ovr_open_sdg_prep