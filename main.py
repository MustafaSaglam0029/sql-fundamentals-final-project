from src.utils.database_connection import db_config
from src.mandate_data_script import load_mandate_data
from src.mandate_data_script import export_mandate_data
from src.meter_data_script import load_meter_data
from src.meter_data_script import export_meter_data
from src.meter_readings_data_script import load_meter_readings_data
from src.meter_readings_data_script import export_meter_readings_data



if __name__ == "__main__":

    execute_load = True

    if execute_load:
        load_mandate_data(r"data/mandate_data.json", db_config)

    export_mandate_data ("..data/output_mandate_data.json", db_config)

    if execute_load:
        load_meter_data(r"data/mandate_data.json", db_config)

    export_meter_data("../data/output_meter_data.json", db_config)

    if execute_load:
        load_meter_readings_data(r"/data/meter_readings.json", db_config)

    export_meter_readings_data("../data/output_meter_readings_data.json", db_config)





















