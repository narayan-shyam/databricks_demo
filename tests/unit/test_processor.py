# tests/unit/test_processor.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.data_processor.processor import DataProcessor

def test_process_data():
    processor = DataProcessor()
    test_data = [{'id': 1, 'value': 100}]
    
    result = processor.process_data(test_data)
    assert 'processed_date' in result.columns
    assert len(result) == 1
