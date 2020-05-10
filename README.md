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

- larger font on desktop
- sidebar to always out on desktop, but collapsed
- broken life icon width on mobile
- broken margin on mobile
- slow down speed of sidebar opening/closing on mobile
- lock background page when sidebar is open
- add links to everything
- add on-hover to links
