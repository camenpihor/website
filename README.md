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

## Caching

- Cache ttl
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag

## TODO

- add caching logic
- use local storage
- recommendations
  - mechanism to show tags/endorsement
- rogue sky
  - add light pollution layer
    - https://blog.mapbox.com/mapping-the-lights-of-the-night-bd32d5a1bdf8
  - add weather to calendar
  - report the max cloud cover from like 6pm to midnight each day
- add report a bug feature

- new pages
  - nature identification
  - tree count
  - documentation
  - measurements

## Nature Identification

- https://www.planning.org/pas/reports/report236.htm
