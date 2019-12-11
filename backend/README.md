# Website Backend

## Installation

(make sure your CWD is `backend/`)

1. `cp .sample_env .env` and fill out anything in `<>`
   1. DARKSKY_API_KEY DarkSky secret key from your DarkSky developer account
   2. DATABASE_URL postgres database url to be created and used for development
   3. TEST_DATABASE_URL postgres database url to be created and used for tests
2. `set -o allexport && source .env && set +o allexport` to export environment variables
3. `pip install -r requirements-dev.in` to install testing/development requirements
4. `pip install -r requirements.txt` to install requirements
5. `python setup.py install` to install package
6. scripts/setup-db to set up production and test databases
7. scripts/test to verify install
