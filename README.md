# Database Project

This project involves loading data from text files, processing it, and visualizing it using different tools.

## Files

- `main.py`: Script to load data from text files, process it, and save it to a SQLite database.
- `visualization.py`: Dash application to visualize the database with filters for each column.
- `visualization_streamlit.py`: Streamlit application to visualize the database with filters for each column.
- `work_station.ipynb`: Jupyter notebook to load and process data.

## Data

The data is stored in the `BBDD` folder and includes the following files:
- `PUB_NOM_SUCURSAL.txt`
- `CODIGO_TIPO_SUBTIPO.txt`
- `PUB_EMPRESAS_PJ_2020_A_2024.txt`
- `PUB_NOMBRES_PJ.txt`
- `PUB_NOM_DOMICILIO.txt`
- `PUB_NOM_ACTECOS.txt`

## Usage

1. Run `main.py` to load and process the data, and save it to a SQLite database.
2. Use `visualization.py` to visualize the data using Dash.
3. Use `visualization_streamlit.py` to visualize the data using Streamlit.
4. Use `work_station.ipynb` to interactively load and process the data in a Jupyter notebook.

## Requirements

- pandas
- sqlite3
- dash
- streamlit
- jupyter
