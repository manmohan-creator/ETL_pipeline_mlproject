from src.ETL_pipeline_mlproject import logger

from src.ETL_pipeline_mlproject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

logger.info("welcome to our custom logging data science")

STAGE_NAME = " Data Ingestion stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<")
        data_ingestion= DataIngestionTrainingPipeline()
        data_ingestion.initiate_data_ingestion()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e