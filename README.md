# Website

## Install

1. `cp .sample_env .env` and fill out anything in `<>`
   1. DARKSKY_API_KEY is the DarkSky secret key from your DarkSky developer account
   2. VUE_APP_BACKEND_URL is the base URL that the frontend should use to communicate with the Flask server
      1. e.g. development `http://127.0.0.1:5000/api`
      1. e.g. production `https://camenpiho.com/api`
2. `set -o allexport && source .env && set +o allexport` to export environment variables
3. `npm install` to install frontend
4. Follow instructions at `backend/README.md` to install backend

## Run Servers

In separate processes:

1. development flow
   1. `scripts/run-frontend`
   2. `cd backend`
   3. `scripts/run-backend --dev`
2. production flow
   1. ngingx
   2. `cd backend`
   3. `scripts/run-backend`

## TODO

- thoughts
  - database
  - how to save file with formatting
  - script to upload file (while on local copy to server)
  - listing
  - searching
- treecounter
  - python cnn repository
- roguesky
  - show more not tell more
  - idea for table: title = day name, summary, star forecast; data underneath = everything
  else and try to think of a way to combine precip prob, type, and intensity
