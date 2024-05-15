# Automated Trading System

This repository contains the implementation of an Automated Trading System using TWS API with Python. The project includes data preprocessing, trading strategy implementation, trade execution, and evaluation.

## Features

- Integration with TWS API for real-time market data and order execution
- Implementation of various trading strategies
- Backtesting and live trading capabilities
- Evaluation and visualization of trading performance

## Technologies Used

- Python
- TWS API
- pandas
- numpy
- matplotlib

## Project Structure

- **README.md**: Overview of the project, installation instructions, and usage.
- **requirements.txt**: List of Python dependencies required for the project.
- **LICENSE**: License information for the project.
- **data/**: Directory to store datasets or any other data files.
- **src/**: Directory for the source code, including data preprocessing, trading strategy implementation, and trade execution scripts.
- **notebooks/**: Directory for Jupyter notebooks containing exploratory data analysis and trading experiments.
- **results/**: Directory to save results, such as trading logs, performance metrics, and plots.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Automated-Trading-System.git
    cd Automated-Trading-System
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Data Preprocessing

Run the data preprocessing script to prepare the dataset:
```bash
python src/data_preprocessing.py
