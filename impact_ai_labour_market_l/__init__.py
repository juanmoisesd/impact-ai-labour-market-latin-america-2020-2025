"""Impact of Artificial Intelligence on the Labour Market in Latin America (2020-2025)
DOI: 10.5281/zenodo.19211739 | GitHub: https://github.com/juanmoisesd/impact-ai-labour-market-latin-america-2020-2025"""
__version__="1.0.0"
__author__="de la Serna, Juan Moisés"
import pandas as pd,io
try:
    import requests
except ImportError:
    raise ImportError("pip install requests")

def load_data(filename=None):
    """Load dataset from Zenodo. Returns pandas DataFrame."""
    rid="10.5281/zenodo.19211739".split(".")[-1]
    meta=requests.get(f"https://zenodo.org/api/records/{rid}",timeout=30).json()
    csvs=[f for f in meta.get("files",[]) if f["key"].endswith(".csv")]
    if not csvs:raise ValueError("No CSV found")
    f=next((x for x in csvs if filename and x["key"]==filename),csvs[0])
    return pd.read_csv(io.StringIO(requests.get(f["links"]["self"],timeout=60).text))

def cite():return f'de la Serna, Juan Moisés (2025). Impact of Artificial Intelligence on the Labour Market in Latin America (2020-20. Zenodo. https://doi.org/10.5281/zenodo.19211739'
def info():print(f"Dataset: Impact of Artificial Intelligence on the Labour Market in Latin America (2020-20\nDOI: 10.5281/zenodo.19211739\nGitHub: https://github.com/juanmoisesd/impact-ai-labour-market-latin-america-2020-2025")