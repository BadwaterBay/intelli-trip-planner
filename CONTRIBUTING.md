# Contributing to Intelli Trip Planner

---

## Table of contents

- [Thank you, contributors](#thank-you-contributors)
- [How can I contribute?](#how-can-I-contribute)
  - [Reporting bugs](#reporting-bugs)
  - [Suggesting features and enhancements](#suggesting-features-and-enhancements)
  - [Submitting pull requests](#submitting-pull-requests)
- [How do I get started?](#how-do-I-get-started)
  - [Initial setup](#initial-setup)
  - [Workflow](#workflow)
  - [Bring your fork up to date with the original repository](#bring-your-fork-up-to-date-with-the-original-repository)
  - [Other useful commands](#other-useful-commands)
- [Style guides](#style-guides)
  - [Git commit messages](#git-commit-messages)
  - [Python style guide](#python-style-guide)
  - [Prefer functional-styled programming](#prefer-functional-styled-programming)
- [Other recommended practices](#other-recommended-practices)
  - [Sign commits with signature verifications](#sign-commits-with-signature-verifications)

---

## Thank you, contributors

We'd like to thank all of our contributors.

[Click here to see a list of our contributors.](https://github.com/BadwaterBay/intelli-trip-planner/graphs/contributors)

---

## How can I contribute?

### Reporting bugs

In the bug report, please follow these steps:

- Use a clear and descriptive title for the issue to identify the problem.
- Describe the exact steps which reproduce the bug.
- Describe the behavior you **_observed_** and point out what exactly is the problem with that behavior.
- Explain the behavior you **_expected_** to see instead and why.
- Include screenshots, animated GIFs or videos to demonstrate the bug.
- Describe the environment in which the bug is observed, including the operating system, the Python version and the browser you are using (if applicable).

### Suggesting features and enhancements

In the feature or enhancement request, please follow these steps:

- Use a clear and descriptive title for the issue to identify the suggestion.
- Describe the current behavior and explain which behavior you expected to see instead and why.
- Explain why this enhancement would be useful.
- It's encouraged to use screenshots or drawings to demonstrate your point, if it helps.

### Submitting pull requests

Please follow these steps:

- Complete the [initial setup](#Initial-setup)
- Follow the [workflow](#Workflow)
- Follow the [style guides](#Style-guides)

---

## How do I get started?

### Prerequisites

Having the followings installed:

- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
- [Node.js 12.x](https://nodejs.org/en/).
- [Yarn](https://classic.yarnpkg.com/en/docs/install/).
- [Python 3.8.x](https://www.python.org/downloads/):
  - You can install Python with your favorite method, such as some sort of virtual environment.
  - You can also use the Dockerfile in the repository to install Python 3.8.x environment.
- [Poetry](https://python-poetry.org/docs/). This is optional if you are using Docker.

### Initial setup

- Satisfy the [prerequisites](#prerequisites).
- Fork the repository. We're going to call it the 'original repository'. ([How to fork a repository?](https://help.github.com/en/github/getting-started-with-github/fork-a-repo#fork-an-example-repository))
- Clone the forked repository. ([How to clone a repository?](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository))
- In the terminal, change directory to the repository's root directory.
- Add the original repository as a remote called `upstream` (assuming you're using HTTPS instead of SSH:
  - Run command:
    ```
    git remote add upstream https://github.com/BadwaterBay/intelli-trip-planner.git
    ```
  - To verify you have added the original repository, run command:
    ```
    git remote -v
    ```
  - You should see the following output:
    ```
    origin  https://github.com:<yourGitHubUsername>/intelli-trip-planner.git (fetch)
    origin  https://github.com:<yourGitHubUsername>/intelli-trip-planner.git (push)
    upstream  https://github.com/BadwaterBay/intelli-trip-planner.git (fetch)
    upstream  https://github.com/BadwaterBay/intelli-trip-planner.git (push)
    ```
- Install all Node dependencies:
  ```
  yarn --frozen-lockfile
  ```
- Install Python packages:
  - If you're using Python inside a virtual environment, run command:
    ```
    poetry install
    ```
  - If you're using Docker, build and run the image with the Dockerfile. [How?](https://docs.docker.com/get-started/part2/) (At this juncture, we're focusing on building the core functionalities in Python without the REST API part, so you don't need to expose any port inside the Docker image.)

<!-- - Run the server for development on your machine with command:
  ```
  yarn start
  ```
  By default, the server is hosted on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
- Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser to confirm the server is running.
- To stop the server, press "Ctrl + C". -->

---

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

---

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

---

### Other useful commands

- Format your code using Prettier:
  - `yarn format` will format files with Prettier and save changes.
  - Tip: when you git-commit, `yarn format` will be automatically triggered.
- Lint your code using Eslint:
  - `yarn lint` will run Eslint to check the code quality. Please try to resolve these issues before committing any changes.
  - Tip: when you git-commit, `yarn lint` will be automatically triggered.
- Create a production build:
  - `yarn build` will generate a production build of the Express app in directory `/dist-server`.
- Run tests:
  - `yarn test` will run preset tests. However, this is a dummy for now, because we haven't written any tests yet. This is to show that we are aware of the importance of unit testing.
- If you run into problems with Python dependencies:
  - Check if you are running Python 3.8.x in your local environment
  - Try `poetry install` to see if it solves your problems.
- If you run into problems with Node dependencies:
  - Try `yarn --frozen-lockfile` to see if it solves your problems.
  - If not, run `yarn refresh` to remove all dependencies in the `node_modules` directory and do a clean install of dependencies.

---

## Style guides

### Git commit messages

- Use the present tense ("Add feature" not "Added feature").
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...").
- Use '&' instead of spelling out 'and'.
- Limit the first line to 70 characters or less.
- Reference issues and pull requests liberally after the first line.
- When only changing documentation, include `[ci skip]` in the commit title.
- Consider starting the commit message with an applicable emoji:
  - :star: `:star:` when adding new features or enhancements.
  - :bug: `:bug:` when fixing bugs.
  - :art: `:art:` when improving the UI.
  - :memo: `:memo:` when writing documentations.
  - :shirt: `:shirt:` when fixing linter warnings or improving the format of the code.
  - :bath: `:bath:` when fixing CI builds.
  - :racehorse: `:racehorse:` when improving the performance.
  - :white_check_mark: `:white_check_mark:` when adding tests.
  - :lock: `:lock:` when dealing with security.
  - :arrow_up: `:arrow_up:` when upgrading dependencies.
  - :arrow_down: `:arrow_down:` when downgrading dependencies.
  - :wrench: `:wrench:` when configuring infrastructures.

### Python style guide

- We follow the [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/) and the [Black code style](https://github.com/psf/black/blob/master/docs/the_black_code_style.md). The [Black code style](https://github.com/psf/black/blob/master/docs/the_black_code_style.md) can be viewed as a strict subset of [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/).

### Prefer functional-styled programming

We prefer functional style programming, meaning that:

- Prefer local variables and avoid unnecessary global variables.
- Given the same input, a function should always return the same output, meaning that the function should not be implicitly (or weirdly) dependent on variables outside the scope of the function.
- Minimize unnecessary [side effects](<https://en.wikipedia.org/wiki/Side_effect_(computer_science)>) of a function.
- Prefer immutable data structures to mutable ones. For example, if you know a series of data isn't going to (or shouldn't) change in the future, use a tuple instead of a list.

---

## Other recommended practices

### Sign commits with signature verifications

It is encouraged to sign your commits with signature verifications with GPG keys. [How?](https://help.github.com/en/github/authenticating-to-github/managing-commit-signature-verification)
