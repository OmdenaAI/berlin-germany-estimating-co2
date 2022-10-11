# Source Folder Structure


    ├── src                <- Source code folder for this project
        │
        ├── data           <- Datasets used and collected for this project
        │   
        ├── docs           <- Folder for Task documentations, Meeting Presentations and task Workflow Documents and Diagrams.
        │
        ├── references     <- Data dictionaries, manuals, and all other explanatory references used 
        │
        ├── tasks          <- Master folder for all individual task folders
        │
        ├── visualizations <- Code and Visualization dashboards generated for the project
        │
        └── results        <- Folder to store Final analysis and modelling results and code.


## Guidelines

- Data              - Folder to Store all the data collected and used for this project 
- Docs              - Folder for Task documentations, Meeting Presentations and task Workflow Documents and Diagrams.
- References        - Folder to store any referneced code/research papers and other useful documents used for this project
- Tasks             - Master folder for all tasks
  - All Task Folder names should follow specific naming convention
  - All Task folder names should be in chronologial order (from 1 to n)
  - All Task folders should have a README.md file with task Details and task goals along with an info table containing all code/notebook files with their links and information
- Visualization     - Folder to store dashboards, analysis and visualization reports
- Results           - Folder to store final analysis modelling results for the project.


## Environment 

For installing the virtual environment use following commands: 

```Bash
pyenv local 3.9.8
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Data

1. [Data reference 1](data/00_data.csv) : [source](https://ig.ft.com/carbon-food-labelling/)
2. [Data reference 2](data/01_items_carbon-emission.csv) : [source](https://ig.ft.com/carbon-food-labelling/)
3. [Data reference 3](data/02_food-emissions-supply-chain.csv) : [source](https://ourworldindata.org/grapher/food-emissions-supply-chain?tab=table&country=Beef+%28beef+herd%29~Cheese~Poultry+Meat~Milk~Eggs~Rice~Pig+Meat~Peas~Bananas~Wheat+%26+Rye~Fish+%28farmed%29~Lamb+%26+Mutton~Beef+%28dairy+herd%29~Shrimps+%28farmed%29~Tofu~Maize~Coffee~Other+Pulses~Citrus+Fruit~Other+Fruit~Sunflower+Oil~Apples~Brassicas~Olive+Oil~Potatoes~Palm+Oil~Barley~Soybean+Oil~Wine~Root+Vegetables~Dark+Chocolate~Cane+Sugar~Nuts~Tomatoes~Rapeseed+Oil~Groundnuts)
4. [Data reference 4](data/01_items_carbon-emission.csv) : [source](https://www.nature.com/articles/s41597-021-00909-8#Sec15)
