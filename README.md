# Website

## Requirements

- Anaconda
- Darksky API credentials

## Installation

1. `scripts/install` to install development environment
1. `source activate website3.8` to activate virtual environment created at (1)
1. `cp .sample_env .env` and update any necessary environment variables
1. `set -o allexport; source .env; set +o allexport` to export environment variables
1. `scripts/test` to verify install
1. `scripts/start` to start server

## Backend

Flask

## Frontend

Vue

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
- fade in star image
- update global page layout
