import os
from src.DataScience import logger
from src.DataScience.entity.config_entity import DataValidationConfig
import pandas as pd 

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self):
        try:
            validation_status = True

            data = pd.read_csv(self.config.unzip_data_dir)
            all_columns = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_columns:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"validation status: {validation_status}")
            return validation_status
        except Exception as e:
            raise e
                        

