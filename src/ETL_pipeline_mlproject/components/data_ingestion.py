import os
import urllib.request as request
from src.ETL_pipeline_mlproject import logger
import zipfile

from src.ETL_pipeline_mlproject.utils.common import read_yaml, create_directories
from src.ETL_pipeline_mlproject import logger

from src.ETL_pipeline_mlproject.entity.config_entity import (DataIngestionConfig)

## component Data ingestion
class DataIngestion:
    def __init__(self, config_path:DataIngestionConfig):
        
        self.config = read_yaml(config_path).data_ingestion
        create_directories([self.config.root_dir])