@echo off

echo Creating ML Project Structure...

:: Root folders
mkdir ml-project
cd ml-project

mkdir .github
mkdir .github\workflows

mkdir data
mkdir data\raw
mkdir data\processed
mkdir data\external

mkdir notebooks

mkdir src
mkdir src\ingestion
mkdir src\preprocessing
mkdir src\training
mkdir src\evaluation
mkdir src\inference
mkdir src\pipelines
mkdir src\utils
mkdir src\config

mkdir models
mkdir models\model_versioning

mkdir reports
mkdir reports\figures

mkdir api

mkdir deployment
mkdir deployment\kubernetes

mkdir tests

:: Create empty files

:: GitHub CI/CD
type nul > .github\workflows\ci-cd.yml

:: Notebooks
type nul > notebooks\eda.ipynb
type nul > notebooks\experiments.ipynb

:: Src files
type nul > src\__init__.py

type nul > src\ingestion\ingest.py
type nul > src\ingestion\data_loader.py

type nul > src\preprocessing\preprocess.py
type nul > src\preprocessing\feature_engineering.py
type nul > src\preprocessing\data_validation.py

type nul > src\training\train.py
type nul > src\training\model.py
type nul > src\training\hyperparameter_tuning.py

type nul > src\evaluation\evaluate.py
type nul > src\evaluation\metrics.py

type nul > src\inference\predict.py
type nul > src\inference\batch_inference.py

type nul > src\pipelines\training_pipeline.py
type nul > src\pipelines\inference_pipeline.py

type nul > src\utils\logger.py
type nul > src\utils\helpers.py
type nul > src\utils\config_loader.py

type nul > src\config\config.yaml
type nul > src\config\params.yaml

:: Models
type nul > models\trained_model.pkl

:: Reports
type nul > reports\metrics.json

:: API
type nul > api\app.py
type nul > api\routes.py

:: Deployment
type nul > deployment\Dockerfile
type nul > deployment\docker-compose.yml

:: Tests
type nul > tests\test_data.py
type nul > tests\test_model.py
type nul > tests\test_api.py

:: Root files
type nul > requirements.txt
type nul > setup.py
type nul > .env
type nul > .gitignore
type nul > README.md

