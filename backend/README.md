# Website Backend

## Installation

(make sure your CWD is `backend/`)

1. `cp .sample_env .env` and fill out anything in `<>`
   1. DARKSKY_API_KEY DarkSky secret key from your DarkSky developer account
2. `set -o allexport && source .env && set +o allexport` to export environment variables
3. `pip install -r requirements-dev.in` to install testing/development requirements
4. `pip install -r requirements.txt` to install requirements
5. `python setup.py install` to install package
6. scripts/test to verify install
