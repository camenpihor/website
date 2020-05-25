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

- next steps
  - link checker test
  - add all actual text
  - add dao for recommendations
  - add dao for nature items
  - add api endpoints for recommendations and nature items
  - use api endpoints for recommendations and nature items search

- pages
  - tree count
  - measurements
  - nature identification

- pair programming
  - recommendations search
  - blog post search
