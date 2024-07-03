import os

def create_project_structure(base_path):
    # Define the folder structure with numbered prefixes for ordering
    folders = [
        "data/raw",
        "data/processed",
        "data/external",
        "notebooks/001-overview",       # Overview of data files present
        "notebooks/002-preprocessing",  # Data preprocessing and cleaning notebooks
        "notebooks/003-exploratory",    # Exploratory Data Analysis (EDA) notebooks
        "notebooks/004-modeling",       # Notebooks for different models and experiments
        "notebooks/005-evaluation",     # Notebooks for evaluating models
        "notebooks/006-final",          # Final notebooks for presentation and reporting
        "scripts/data",
        "scripts/features",
        "scripts/models",
        "scripts/evaluation",
        "results/figures",
        "results/tables",
        "results/logs",
        "docs/reports",
        "docs/references",
        "src"
    ]

    # Create the folders
    for folder in folders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)

    # Create the README file
    readme_content = """

# Data Science Project Template

This is a template for organizing data science projects. Below is a description of the folder structure:

## Folder Structure


    my-project/
    │
    ├── data/
    │   ├── raw/              # Raw data, unchanged and original datasets
    │   ├── processed/        # Cleaned and preprocessed data
    │   └── external/         # External data from third-party sources
    │
    ├── notebooks/
    │   ├── 001-overview/      # Overview of data files present
    │   ├── 002-preprocessing/ # Data preprocessing and cleaning notebooks
    │   ├── 003-exploratory/   # Exploratory Data Analysis (EDA) notebooks
    │   ├── 004-modeling/      # Notebooks for different models and experiments
    │   ├── 005-evaluation/    # Notebooks for evaluating models
    │   └── 006-final/         # Final notebooks for presentation and reporting
    │
    ├── scripts/
    │   ├── data/             # Scripts for data processing and cleaning
    │   ├── features/         # Scripts for feature engineering
    │   ├── models/           # Scripts for model training
    │   └── evaluation/       # Scripts for model evaluation
    │
    ├── results/
    │   ├── figures/          # Figures and plots
    │   ├── tables/           # Tables and summaries
    │   └── logs/             # Logs of model training and evaluation
    │
    ├── docs/                 # Documentation
    │   ├── reports/          # Generated analysis as HTML, PDF, LaTeX, etc.
    │   ├── references/       # Data dictionaries, manuals, and all other explanatory materials
    │   └── README.md         # Project overview and setup instructions
    │
    ├── src/                  # Source code for project
    │   ├── __init__.py
    │   ├── data_processing.py
    │   ├── feature_engineering.py
    │   ├── model_training.py
    │   └── evaluation.py
    │
    ├── environment.yml       # Conda environment file (or requirements.txt for pip)
    └── .gitignore            # Git ignore file


## Description of Each Folder

- **data/**:
      
    - `raw/`: Contains the raw, untouched data files.
      
    - `processed/`: Contains cleaned and processed data files ready for analysis.
      
    - `external/`: Contains data from third-party sources.

- **notebooks/**:

    - `001-overview/`: Overview of data files present.
      
    - `002-preprocessing/`: Notebooks for data cleaning and preprocessing.
      
    - `003-exploratory/`: Notebooks for exploratory data analysis.
      
    - `004-modeling/`: Notebooks for model development and experimentation.
      
    - `005-evaluation/`: Notebooks for model evaluation.
      
    - `006-final/`: Notebooks that are ready for presentation or sharing.

- **scripts/**:
      
    - `data/`: Scripts for data loading, cleaning, and transformation.
      
    - `features/`: Scripts for feature engineering and selection.
      
    - `models/`: Scripts for training different models.
      
    - `evaluation/`: Scripts for evaluating model performance.

- **results/**:
      
    - `figures/`: Stores figures and plots generated during the analysis.
      
    - `tables/`: Stores tables and summaries.
      
    - `logs/`: Logs generated during model training and evaluation.

- **docs/**:
      
    - `reports/`: Generated analysis reports.
      
    - `references/`: Contains reference materials such as data dictionaries.
      
    - `README.md`: Provides an overview of the project, including setup instructions and key findings.

- **src/**:
      
    - Source code for the project, including modules for data processing, feature engineering, model training, and evaluation.

- **environment.yml** or **requirements.txt**:
      
    - Contains the list of dependencies required to run the project.

- **.gitignore**:
      
    - Specifies files and directories to be ignored by version control (Git).

## Detailed Explanation of Best Practices

1. **Modularize Code**: Keep code modular and reusable by separating it into different scripts and notebooks. This helps in maintaining code quality and makes it easier to debug and update specific parts of the project.

2. **Document Thoroughly**: Include README files and documentation for clarity. Thorough documentation helps new team members or collaborators understand the project quickly.

3. **Use Version Control**: Use Git to track changes and collaborate effectively. Version control ensures that changes can be traced, reviewed, and reverted if necessary.

4. **Environment Management**: Use environment files (e.g., `environment.yml` or `requirements.txt`) to manage dependencies. This ensures that the project can be replicated easily on different machines or environments.

5. **Data Handling**: Keep raw data unchanged and separate from processed data. This ensures data integrity and makes it possible to reprocess data if needed.

## Happy Hacking !!!
    
    """

    with open(os.path.join(base_path, "README.md"), "w", encoding="utf-8") as readme_file:
        readme_file.write(readme_content.strip())

    # Create LICENSE file (MIT License)
    license_content = """
    MIT License

    Copyright (c) <year> <author>

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """

    with open(os.path.join(base_path, "LICENSE"), "w", encoding="utf-8") as license_file:
        license_file.write(license_content.strip())

# Usage
if __name__ == "__main__":
    base_path = os.getcwd()  # Get the current working directory
    create_project_structure(base_path)
    
    # Delete the script itself after running
    script_path = os.path.abspath(__file__)
    os.remove(script_path)
