# flourish-server

<!-- badges -->
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://www.mit.edu/~amini/LICENSE.md)
[![GitHub latest commit](https://img.shields.io/github/last-commit/team-flourish/flourish-server.svg)](https://github.com/team-flourish/flourish-server/commit/)
[![GitHub forks](https://img.shields.io/github/forks/team-flourish/flourish-server.svg)](https://github.com/team-flourish/flourish-server)

Server-side repo for the Flourish group project. Main project repo can be found [here](https://github.com/team-flourish/flourish).

## Installation & Usage

### Prerequisites

* You must have Python 3.9.1 installed.

### Installation

1. Clone the repo using `git clone git@github.com:team-flourish/flourish-server.git`
2. Enter the repo directory `cd flourish-server`
3. Create the virtual environment `pipenv --python 3.9.1`
4. Enter the virtual environment `pipenv shell`
5. Install dependencies `pipenv install --dev`

### Usage

* While inside the virtual environment:
  * `pipenv run dev` to start the server in development mode.
    * Available at `localhost:5000`.
  * `pipenv run test` to run tests.
  * `pipenv run coverage` to check test coverage.
* To remove the virtual environment from your system use `pipenv --rm`.

## Design & Implementation

### Technologies

* Flask
* pytest
* PostgreSQL

### API Routes

<!-- API routes here -->

## Changelog



## Fixed Bugs



## Pitfalls & Discoveries



## Remaining Bugs



## Improvements & Future Features



## License

* [MIT License](https://www.mit.edu/~amini/LICENSE.md)
