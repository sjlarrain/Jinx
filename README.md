# Database Project

This project involves loading data from text files, processing it, and visualizing it using different tools.

## Files

- `main.py`: Script to load data from text files, process it, and save it to a SQLite database.
- `visualization.py`: Dash application to visualize the database with filters for each column.
- `visualization_streamlit.py`: Streamlit application to visualize the database with filters for each column.
- `work_station.ipynb`: Jupyter notebook to load and process data.
- `BBDD_Schema/BBDD_J&S.drawio`: Diagram of the database schema in draw.io format.
- `BBDD_Schema/BBDD_J&S.pdf`: Diagram of the database schema in PDF format.
- `install_requirements.sh`: Shell script to install the required libraries.
- `install_requirements_windows.py`: Python script to install the required libraries on Windows.

## Data

The data is stored in the `BBDD` folder and includes the following files:
- `PUB_NOM_SUCURSAL.txt`
- `CODIGO_TIPO_SUBTIPO.txt`
- `PUB_EMPRESAS_PJ_2020_A_2024.txt`
- `PUB_NOMBRES_PJ.txt`
- `PUB_NOM_DOMICILIO.txt`
- `PUB_NOM_ACTECOS.txt`

For more information, visit [this link](https://www.sii.cl/sobre_el_sii/nominapersonasjuridicas.html).

## Database Schema

The database schema is represented in the `BBDD_Schema/BBDD_J&S.drawio` and `BBDD_Schema/BBDD_J&S.pdf` files. These files provide a visual representation of the relationships between the tables and the structure of the data.

## Usage

1. Run `install_requirements.sh` to install the required libraries on Linux.
2. Run `install_requirements_windows.py` to install the required libraries on Windows.
3. Run `main.py` to load and process the data, and save it to a SQLite database.
4. Use `visualization.py` to visualize the data using Dash.
5. Use `visualization_streamlit.py` to visualize the data using Streamlit.
6. Use `work_station.ipynb` to interactively load and process the data in a Jupyter notebook.

## Requirements

- pandas
- sqlite3
- dash
- streamlit
- jupyter
