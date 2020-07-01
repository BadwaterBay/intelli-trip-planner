# Intelli Trip Planner

Repository: [https://github.com/BadwaterBay/intelli-trip-planner](https://github.com/BadwaterBay/intelli-trip-planner)

---

## Table of contents

- [Description](#Description)
- [Badges](#Badges)
- [Tasks](#Tasks)
- [Contributing to this project](#Contributing-to-this-project)
  - [Workflow](#Workflow)
  - [Initial setup](#Initial-setup)
  - [Bring your fork up to date with the original repository](#Bring-your-fork-up-to-date-with-the-original-repository)
  - [Other useful commands](#Other-useful-commands)
  - [Recommended practices](#Recommended-practices)
- [Contributors](#Contributors)

---

## Description

The goal of this project is to build an API that can intelligently recommend road trip routes, given a number of criteria, including trip duration, budget, region of interest, must-visit destinations, lodging places and time spent at a given location.

---

## Badges

[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![Node.js CI](https://github.com/BadwaterBay/intelli-trip-planner/workflows/Node.js%20CI/badge.svg)
[![CodeFactor](https://www.codefactor.io/repository/github/badwaterbay/intelli-trip-planner/badge)](https://www.codefactor.io/repository/github/badwaterbay/intelli-trip-planner)
[![DeepScan grade](https://deepscan.io/api/teams/9440/projects/11966/branches/179827/badge/grade.svg)](https://deepscan.io/dashboard#view=project&tid=9440&pid=11966&bid=179827)

[![GitHub issues](https://img.shields.io/github/issues/BadwaterBay/intelli-trip-planner.svg)](https://GitHub.com/BadwaterBay/intelli-trip-planner/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/BadwaterBay/intelli-trip-planner.svg)](https://GitHub.com/BadwaterBay/intelli-trip-planner/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/BadwaterBay/intelli-trip-planner.svg)](https://GitHub.com/BadwaterBay/intelli-trip-planner/pulls/)
[![GitHub pull-requests closed](https://img.shields.io/github/issues-pr-closed/BadwaterBay/intelli-trip-planner.svg)](https://GitHub.com/BadwaterBay/intelli-trip-planner/pulls/)

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

### Workflow

Our workflow is:

- Find an [issue](https://github.com/BadwaterBay/intelli-trip-planner/issues) you'd like to solve and claim it by leaving a comment.
- Complete the [initial setup](#Initial-setup), if you haven't.
- [Bring your fork up to date with the original repository](#Bring-your-fork-up-to-date-with-the-original-repository).
- Modify the code to solve the issue and commit changes.
- Make sure your base is up to date with the original repository (`upstream`) with commands:
  ```
  git fetch upstream
  git rebase upstream/master
  ```
- Push your commit to the remote of your forked repository. ([How to push commits to remote?](https://help.github.com/en/github/using-git/pushing-commits-to-a-remote-repository))
- Submit a pull request (PR) to be merged into the original repository's `master` branch. ([How to create a PR?](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request))
- Peers will review your PR and may request revisions.
- Once your PR is approved, your commit will be merged to the `master` branch. Congratulations!

If you are new to this workflow, you can a practice run here: [https://github.com/firstcontributions/first-contributions](https://github.com/firstcontributions/first-contributions)

If you are stuck, you are welcome to reach out and leave a comment.

### Initial setup

- Prerequisites: having [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), [Node.js 12.x](https://nodejs.org/en/) and [Yarn](https://classic.yarnpkg.com/en/docs/install/) installed on your machine.
- Fork the repository. ([How to fork a repository?](https://help.github.com/en/github/getting-started-with-github/fork-a-repo#fork-an-example-repository))
- Clone this repository. ([How to clone a repository?](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository))
- In the terminal, change directory to the repository's root directory.
- Add the original repository as a remote called `upstream`:
  - To add the original repository as `upstream`, run command:
    ```
    git remote add upstream https://github.com/BadwaterBay/intelli-trip-planner.git
    ```
  - To verify you have added the original repository, run command:
    ```
    git remote -v
    ```
  - You should see the following output (assuming you are using HTTPS):\
    ```
    origin  https://github.com:<yourGitHubUsername>/intelli-trip-planner.git (fetch)
    origin  https://github.com:<yourGitHubUsername>/intelli-trip-planner.git (push)
    upstream  https://github.com/BadwaterBay/intelli-trip-planner.git (fetch)
    upstream  https://github.com/BadwaterBay/intelli-trip-planner.git (push)
    ```
- Install all dependencies with the following command. This could take a while.
  ```
  yarn --frozen-lockfile
  poetry install
  ```
- Run the server for development on your machine with command:
  ```
  yarn start
  ```
  By default, the server is hosted on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
- Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser to confirm the server is running.
- To stop the server, press "Ctrl + C".

### Bring your fork up to date with the original repository

- Completed the [initial setup](#Initial-setup), if you haven't.
- Fetch updates from the original repository (`upstream`):
  ```
  git fetch upstream
  ```
- Make sure you are on your local `master` branch:
  ```
  git checkout master
  ```
- Rebase your local `master` branch with `upstream/master` branch:
  ```
  git rebase upstream/master
  ```
- Push your local `master` to remote:
  ```
  git push origin master
  ```
  If your push is rejected ([why?](https://www.reddit.com/r/git/comments/6jzogp/why_am_i_force_pushing_after_a_rebase/)), you might need to force-push to remote:
  ```
  git push -f origin master
  ```

### Other useful commands

- Format your code using Prettier:
  - `yarn format` will format files with Prettier and save changes.
  - Tip: when you git-commit, `yarn format` will be automatically triggrred.
- Lint your code using Eslint:
  - `yarn lint` will run Eslint to check the code quality. Please try to resolve these issues before commiting any changes.
  - Tip: when you git-commit, `yarn lint` will be automatically triggrred.
- Create a production build:
  - `yarn build` will generate a production build of the Express app in directory `/dist-server`.
- Run tests:
  - `yarn test` will run preset tests. However, this is a dummy for now, because we haven't written any tests yet. This is to show that we are aware of the importance of unit testing.
- If you run into problems with dependencies:
  - Try `yarn --frozen-lockfile` to see if it solves your problems.
  - If not, run `yarn refresh` to remove all dependencies in the `node_modules` directory and do a clean install of dependencies.

### Recommended practices

- Sign commits with signature verifications
  - It is encouraged to sign your commits with signature verifications with GPG keys.
  - [How?](https://help.github.com/en/github/authenticating-to-github/managing-commit-signature-verification)

---

## Contributors

[Click here to see a list of our contributors.](https://github.com/BadwaterBay/intelli-trip-planner/graphs/contributors)
