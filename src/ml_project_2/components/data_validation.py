import os
from ml_project_2 import logger
from ml_project_2.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            columns = list(data.columns)
            schema_col = self.config.all_schema.keys()

            validation_status = None

            for col in columns:
                if col not in schema_col:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation Status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation Status: {validation_status}")

            return validation_status
            
        except Exception as e:
            raise e