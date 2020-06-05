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

## Nginx

- https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04#step-5-setting-up-server-blocks-(recommended)
- https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04

## TODO

- next steps
  - clean up nginx config
  - write my own cron job
  - add top margin to 404
  - add caching logic
  - use local storage 
  - recommendations
    - add
    - mechanism to show tags/endorsement
  - nature identification page

- new pages
  - tree count
  - documentation
  - measurements

## Nature Identification

- https://www.planning.org/pas/reports/report236.htm
