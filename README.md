# Intelli Trip Planner

[https://github.com/Badwater-Apps/intelli-trip-planner](https://github.com/Badwater-Apps/intelli-trip-planner)

[![CodeFactor](https://www.codefactor.io/repository/github/badwaterbay/intelli-trip-planner/badge)](https://www.codefactor.io/repository/github/badwaterbay/intelli-trip-planner)
[![DeepScan grade](https://deepscan.io/api/teams/9440/projects/11966/branches/179827/badge/grade.svg)](https://deepscan.io/dashboard#view=project&tid=9440&pid=11966&bid=179827)
![Node.js CI](https://github.com/BadwaterBay/intelli-trip-planner/workflows/Node.js%20CI/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Grand Goal

The grand goal of this project is to build a web app that can intelligently recommend road trip routes, given a number of criteria, such as trip duration, budget, region of interest, must-visit destinations, lodging places, time spent at a given location, etc.

## Tasks

The grand goal is glorious but difficult to implement, requiring front-end website (HTML, CSS, and JavaScript), back-end database and computation, and even machine learning.

Hence, we break down it into smaller steps.

- The first baby step is to **find the fastest route, given n destinations**, powered by JavaScript and Google Maps API. Then, extend the algorithm to find the shortest route, given n destinations.
- The next step is to **create a small database of 10-20 attractions**, so that we can use it to develop core algorithms that can recommend road trip routes. The area around Las Vegas is an ideal choice. There are many natural attractions within ~4 hours of driving, including Grand Canyon National Park, Death Valley National Park, Zion National Park, Bryce Canyon National Park, Horseshoe Bend, and Antelope Canyon.
- **Develop core algorithms that can intelligently recommend road trip routes**.
- In the meantime, **design and implement the big database** of attractions. We should further break this huge task down to smaller tasks. For example, a database of all National Parks in the US will be a good starting point, given there are only 58 of them. Then we can further include more attractions, and even in other countries. Because the world is huge, to save us some time, let's try to include attractions that are meaningful to road trips.
- In the meantime, **design the UI** of the web app.

## Contributing to this project

This is a work in progress.

If you are interested in contributing to this project, you are welcome to reach out.

To contribute to this project, we follow a rather standard approach of open-source software development, such as: [https://github.com/firstcontributions/first-contributions](https://github.com/firstcontributions/first-contributions)

## Development

### Initial setup

- Prerequisites: having [Node.js 10.x or 12.x](https://nodejs.org/en/) and the latest [yarn](https://classic.yarnpkg.com/en/docs/install/) installed on your machine.
- Clone this repository. [How to clone a repository?](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
- Change directory to the project's root directory, run command `yarn --frozen-lockfile` to install all dependencies. This might take a while.
- Run the server on your machine for development with command `yarn dev-server:watch`. The server will be hosted at [http://localhost:9000/](http://localhost:9000/) by default. When you save changes inside `/server` directory, it will automatically recompile and reload the server.

### Other commands

- Formatting using Prettier:
  - `yarn format` will format files with Prettier and save changes.
  - Tip: when you git-commit, `yarn format` will be automatically triggrred.
- Linting using Eslint:
  - `yarn lint` will run Eslint to check the code quality. Please try to resolve these issues before commiting any changes.
  - Tip: when you git-commit, `yarn lint` will be automatically triggrred.
- Run tests:
  - `yarn test` will run preset tests. However, this is a dummy for now, because we haven't written any tests yet. This is to show that we are aware of the importance of unit testing.
- Create a production build:
  - `yarn build-server` will generate a production build of the Express app in directory `/dist-server`.

## Contributors

[Click here to see our contributors.](https://github.com/Badwater-Apps/intelli-trip-planner/graphs/contributors)

## Date created

October 27, 2019
