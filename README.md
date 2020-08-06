# Intelli Trip Planner

Repository: [https://github.com/BadwaterBay/intelli-trip-planner](https://github.com/BadwaterBay/intelli-trip-planner)

![Python application](https://github.com/BadwaterBay/intelli-trip-planner/workflows/Python%20application/badge.svg)
![Node.js CI](https://github.com/BadwaterBay/intelli-trip-planner/workflows/Node.js%20CI/badge.svg)
[![codecov](https://codecov.io/gh/BadwaterBay/intelli-trip-planner/branch/master/graph/badge.svg)](https://codecov.io/gh/BadwaterBay/intelli-trip-planner)
[![CodeFactor](https://www.codefactor.io/repository/github/badwaterbay/intelli-trip-planner/badge)](https://www.codefactor.io/repository/github/badwaterbay/intelli-trip-planner)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![GitHub issues](https://img.shields.io/github/issues/BadwaterBay/intelli-trip-planner.svg)](https://GitHub.com/BadwaterBay/intelli-trip-planner/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/BadwaterBay/intelli-trip-planner.svg)](https://GitHub.com/BadwaterBay/intelli-trip-planner/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/BadwaterBay/intelli-trip-planner.svg)](https://GitHub.com/BadwaterBay/intelli-trip-planner/pulls/)
[![GitHub pull-requests closed](https://img.shields.io/github/issues-pr-closed/BadwaterBay/intelli-trip-planner.svg)](https://GitHub.com/BadwaterBay/intelli-trip-planner/pulls/)

---

## Table of contents

- [Thank you, contributors](#thank-you-contributors)
- [Description](#description)
- [Tasks](#tasks)
- [Contributing to this project](#contributing-to-this-project)
- [Essential file structure](#essential-file-structure)

---

## Thank you, contributors

We'd like to thank all of our contributors.

[Click here to see a list of our contributors.](https://github.com/BadwaterBay/intelli-trip-planner/graphs/contributors)

---

## Description

The goal of this project is to build an API that can intelligently recommend road trip routes, given a number of criteria, including trip duration, budget, region of interest, must-visit destinations, lodging places and time spent at a given location.

---

## Tasks

The grand goal is glorious but difficult to implement, requiring front-end website (HTML, CSS, and JavaScript), back-end database and computation, and even machine learning.

Hence, we break down it into smaller steps.

- The first baby step is to **find the fastest route, given n destinations**, powered by JavaScript and Google Maps API. Then, extend the algorithm to find the shortest route, given n destinations.
- The next step is to **create a small database of 10-20 attractions**, so that we can use it to develop core algorithms that can recommend road trip routes. The area around Las Vegas is an ideal choice. There are many natural attractions within ~4 hours of driving, including Grand Canyon National Park, Death Valley National Park, Zion National Park, Bryce Canyon National Park, Horseshoe Bend, and Antelope Canyon.
- **Develop core algorithms that can intelligently recommend road trip routes**.
- In the meantime, **design and implement the big database** of attractions. We should further break this huge task down to smaller tasks. For example, a database of all National Parks in the US will be a good starting point, given there are only 58 of them. Then we can further include more attractions, and even in other countries. Because the world is huge, to save us some time, let's try to include attractions that are meaningful to road trips.
- In the meantime, **design the UI** of the web app.

---

## Contributing to this project

Please refer to our [Contributing Guidelines](https://github.com/BadwaterBay/intelli-trip-planner/blob/master/CONTRIBUTING.md).

---

## Essential file structure

```
- <root>
  - CONTRIBUTING.md
  - Dockerfile
  - LICENSE
  - README.md
  - package.json
  - pyproject.toml
  - requirements.txt
  - src
    - app.py: Flask API app
    - bin
      - www.sh: Flask API driver
    - core
      - find_route.py (Core functionality for finding route)
      - get_distance_matrix.py (Driver function for getting distance matrices from Google Maps API for development purposes)
      - data
        - distance_matrix.json (Raw JSON response from Google Maps API)
        - parsed_distance_matrix.json (Parsed distance matrix)
        - parsed_distance_matrix.pkl (Parsed distance matrix)
      - distancematrix
        - google_distance_matrix.py (Get distance matrices from Google Maps API)
      - helpers
        - general.py (Helper functions that don't fit into other files in this directory)
        - read_write.py (Helper functions for reading and writing files)
    - tests (test scripts for testing each script in src)
      - load_answer_key.py (load answer keys for certain testing scripts)
      - test_find_route.py
      - test_get_distance_matrix.py
      - test_google_distance_matrix.py
      - test_helpers_general.py
      - test_helpers_read_white.py
      - test_data (data for testing purposes)
        - distance_matrix.json
        - parsed_distance_matrix.json
        - parsed_distance_matrix.pkl
```
