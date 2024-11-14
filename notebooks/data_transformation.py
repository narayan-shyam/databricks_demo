# Databricks notebook source
from data_processor.processor import DataProcessor
from data_processor.utils import calculate_metrics


def main():
    processor = DataProcessor(spark)
    data = [{'id': 1, 'value': 100}, {'id': 2, 'value': 200}]

    df = processor.process_data(data)
    metrics = calculate_metrics(df)

    return metrics