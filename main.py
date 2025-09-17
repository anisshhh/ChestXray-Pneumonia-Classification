import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from src.chestXrayClassification.pipeline import stage_01_data_ingestion

if __name__ == "__main__":
    # Stage 1: Data Ingestion
    path = stage_01_data_ingestion.data_ingestion()
    print("Stage 1 completed, dataset available at:", path)
