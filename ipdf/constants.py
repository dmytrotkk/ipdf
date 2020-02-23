import os
from pathlib import Path

PALETTE = {
    'success': '#00c841',
    'info': '#1976a3',
    'error': '#d40000'
}

LINE = '-' * 100

ELEMENTS = [1, 0]

DEFAULT_QUANTILE = 0.05


HOME_DIR = str(Path.home())
IPDF_DATADIR = os.getenv('IPDF_DATADIR')

if not IPDF_DATADIR:
    IPDF_DATADIR = os.path.join(HOME_DIR, 'ipdf_data')


TOURNAMENT_RESULTS_FILEPATH = os.path.join(IPDF_DATADIR, 'evolution_tournament_results.json')
