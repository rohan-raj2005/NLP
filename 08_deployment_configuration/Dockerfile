FROM python:3.10-slim

WORKDIR /app

COPY 02_project_setup_and_architecture/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run training to make sure artifacts are fresh
RUN python 03_dataset_collection_and_exploration/download_datasets.py && \
    python 04_preprocessing_and_nlp_training/train.py

EXPOSE 8000

CMD ["python", "05_backend_api_and_inference/api_server.py"]
