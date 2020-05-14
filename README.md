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
- recommendations
  - search functionality
- blog
  - position wave at bottom on every screen
  - search functionality
  - more spacing after search
- blog post
  - position bowling at bottom on every screen
  - more spacing after search
  - search functionality
- screen size should be min 100vh on every screen
- maybe backup icons/text in case loading failure
- rogueSky page
- math implementations link (or maybe just host what the file is on github?? possible???)
- verify all links
- link checker test
- tree count
  - mock
  - create
- measurements for humans
  - mock
  - create
- nature identification
  - mock
  - create
- recommendations
  - fix spacing due tp person readin image
- search bar
  - more rounded edges
- max width on router-view
- see what css I can generalize
- whenever 404 page sometimes home icon doesn't load