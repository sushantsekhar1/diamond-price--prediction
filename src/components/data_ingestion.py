import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


## Initilized the Data Ingestion Configruation

@dataclass
class DataIngestionConfig:
    