# Building a Machine Learning Workflow with DVC and MLflow

This project presents a structured machine learning workflow using **DVC (Data Version Control)** to manage data and models, along with **MLflow** for experiment tracking. The pipeline implements a Random Forest Classifier trained on the Pima Indians Diabetes Dataset, with distinct steps for data preparation, model training, and evaluation.

## Highlights:

### Leveraging DVC for Workflow Management:
- Tracks datasets, model artifacts, and pipeline dependencies, ensuring reproducible results.
- Modular pipeline design allows automatic re-execution of affected steps when any input, code, or configuration changes.
- Supports remote storage options like S3 or DagsHub, enabling efficient handling of large datasets.

### Tracking Experiments with MLflow:
- Captures hyperparameters, metrics, and artifacts for each experiment run.
- Tracks model configurations such as `n_estimators` and `max_depth`, along with evaluation metrics like accuracy.
- Offers a clear comparison of multiple experiments to aid in model optimization.

## Workflow Steps:

### 1. Data Preparation:
- The `preprocess.py` script reads raw data (`data/raw/data.csv`), applies transformations (e.g., renaming columns), and outputs processed data to `data/processed/data.csv`.
- Ensures a consistent preprocessing routine for all runs.

### 2. Model Training:
- The `train.py` script trains a Random Forest Classifier on the prepared data.
- Saves the model as `models/random_forest.pkl`.
- Logs hyperparameters, metrics, and model artifacts to MLflow for easy tracking and visualization.

### 3. Model Evaluation:
- The `evaluate.py` script assesses the trained model's performance using metrics such as accuracy.
- Logs evaluation results to MLflow for comparison across experiments.

## Objectives:
- **Reproducibility:** Ensures consistent results by managing data, code, and dependencies across environments.
- **Experiment Tracking:** Simplifies comparison of different models and hyperparameter configurations.
- **Team Collaboration:** Facilitates smooth collaboration with shared tracking of datasets, models, and experiment results.

## Tools and Technologies:
- **Python:** Core language for implementing data processing and machine learning steps.
- **DVC:** Handles version control for datasets, models, and pipeline dependencies.
- **MLflow:** Manages experiment tracking and logs performance metrics and model artifacts.
- **Scikit-learn:** Provides the Random Forest implementation for training the model.

## How the Pipeline is Structured:

### Adding the Data Preparation Step:
```bash
dvc stage add -n preprocess \
    -p preprocess.input,preprocess.output \
    -d src/preprocess.py -d data/raw/data.csv \
    -o data/processed/data.csv \
    python src/preprocess.py
# ML-Workflow-with-DVC-and-MLflow
# ML-Workflow-with-DVC-and-MLflow
# ML-Workflow-with-DVC-and-MLflow
