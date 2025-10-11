import pandas as pd
from src.ingest_data import DataIngestorFactory
from zenml import step

"""
This file is required to seperately maintain zenml workflow
for each step like it instructs each step what to ddo at this step.
when we use @step ,it makes a seperate zenml step(sperate block or flow chunk).
"""
@step
def data_ingestion_step(file_path: str) -> pd.DataFrame:
    """Ingest data from a ZIP file using the appropriate DataIngestor."""
    # Determine the file extension
    file_extension = ".zip"  # Since we're dealing with ZIP files, this is hardcoded

    # Get the appropriate DataIngestor
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)

    # Ingest the data and load it into a DataFrame
    df = data_ingestor.ingest(file_path)
    return df
