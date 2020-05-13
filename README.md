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

- sidebar to always out on desktop, but collapsed
- make background image a forever scroll
- about
  - make it clear the recommendations are links
  - resume icon should go to resume
- home
  - home button background should go away after navigating
- navigation
  - little snappier on closing sidebar after clicking to external link

