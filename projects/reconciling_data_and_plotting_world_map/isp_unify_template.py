"""
Project for Week 3 of "Python Data Visualization".
Unify data via common country name.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal

def reconcile_countries_by_name(plot_countries, gdp_countries):
    """
    Inputs:
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country names used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country names from
      gdp_countries The set contains the country codes from
      plot_countries that were not found in gdp_countries.
    """
    countries_dict = {}
    not_found_countries = set()
    for plot_country in plot_countries.items():
        if plot_country[1] in gdp_countries:
            countries_dict[plot_country[0]] = plot_country[1]
        else:
            not_found_countries.add(plot_country[0])

    return countries_dict, not_found_countries

# def test_reconcile_countries_by_name():
#     plot_countries = { 'ad': 'Andorra', 'ae': 'United Arab Emirates', 'af': 'Afghanistan' }
#     gdp_countries = { 'Andorra': None, 'Afghanistan': None }

#     print(reconcile_countries_by_name(plot_countries, gdp_countries))
#     return

#test_reconcile_countries_by_name()


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in reader:
            table[row[keyfield]] = row

    return table

def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    gdp_by_country_code = {}
    no_data_countries = set()
    gdpfile = gdpinfo['gdpfile']
    separator = gdpinfo['separator']
    quote = gdpinfo['quote']
    country_name_column = gdpinfo['country_name']

    gdp_data = read_csv_as_nested_dict(gdpfile, country_name_column, separator, quote)
    countries_dict, nofound_countries = reconcile_countries_by_name(plot_countries, gdp_data.keys())
    for country_code, country_name in countries_dict.items():
        gdp = gdp_data[country_name][year]
        if gdp is None or gdp == "":
            no_data_countries.add(country_code)
        else:
            gdp_by_country_code[country_code] = math.log10(float(gdp))

    return gdp_by_country_code, nofound_countries, no_data_countries

# def test_build_map_dict_by_name():
#     gdpinfo = {
#         "gdpfile": "isp_gdp.csv",
#         "separator": ",",
#         "quote": '"',
#         "min_year": 1960,
#         "max_year": 2015,
#         "country_name": "Country Name",
#         "country_code": "Country Code"
#     }
#     plot_countries = { 'br': 'Brazil' }
#     plot_countries = pygal.maps.world.COUNTRIES
#     year = '2000'

#     gdp_by_country_code = build_map_dict_by_name(gdpinfo, plot_countries, year)
#     print(gdp_by_country_code)

#test_build_map_dict_by_name()

def render_world_map(gdpinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for
      map_file       - Name of output file to create

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data for the given year and
      writes it to a file named by map_file.
    """

    plot_data, not_found, no_data = build_map_dict_by_name(gdpinfo, plot_countries, year)

    worldmap = pygal.maps.world.World()
    worldmap.title = 'GDP by country for year {}'.format(year)
    worldmap.add('GDP info', plot_data)
    worldmap.add('No GDP info', not_found)
    worldmap.add('No GDP in year', no_data)
    
    worldmap.render_to_file(map_file) 
    # worldmap.render_in_browser()


def test_render_world_map():
    """
    Test the project code for several years.
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, pygal_countries, "1960", "isp_gdp_world_name_1960.svg")

    # 1980
    render_world_map(gdpinfo, pygal_countries, "1980", "isp_gdp_world_name_1980.svg")

    # 2000
    render_world_map(gdpinfo, pygal_countries, "2000", "isp_gdp_world_name_2000.svg")

    # 2010
    render_world_map(gdpinfo, pygal_countries, "2010", "isp_gdp_world_name_2010.svg")


# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

# test_render_world_map()
