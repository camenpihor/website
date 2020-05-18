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
  - verify all links
  - link checker test
  - add geographical star visibility to map
  - add long-term forecast of star visibility to calendar
  - life icons to just paragraph summaries/remove all together?

- pages
  - documentation
  - tree count
  - measurements
  - nature identification

- pair programming
  - recommendations search
  - blog post search
