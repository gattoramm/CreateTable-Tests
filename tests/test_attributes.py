import pytest
import app.sqlscripts_generator as sql_generator
import app.sqlscripts_constructor as sql_constructor


@pytest.mark.parametrize()
def test_directory_command():
    scripts_list = sql_generator.get_sql_scripts_list()
    map_ttc = sql_constructor.map_type__table_column
    pass