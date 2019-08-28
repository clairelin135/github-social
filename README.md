# GitHub Social
Platform to like and comment on user events.

## Project Details & Dependencies
Database: MySQL
Backend: Flask (python3)
Frontend: ReactJS
Other: Data supplied through GitHub API

## Introduction
Welcome! This is a short introductory CS project designed to help you learn full-stack fundamentals in under 20 hours. As a high level overview, this project is meant to be a copy of GitHub, except that you can view, like, and comment on user activity.

Currently, the only functionality is to view and like activity. The first task will be to add the functionality to add comments. Along any step of the way if you have questions, please ask!!! This is the first time that this project has been implemented, so I anticipate there may be a couple of bumps along the way.

## Installation
1. Fork the repository and clone it to your desktop.
Click "Fork" in the upper right corner. Then, on your own repository, click the green "clone" button on the upper right of the repository. Copy the link, and in terminal enter `git clone <link>` in your desired directory.

2. Navigate into the repository. (`cd github-social`)

3. Create a virtual environment and activate it.
```
python3 -m venv venv
. venv/bin/activate
```
You will know if this is successful if the terminal command is prepended by `(venv)`.

4. Install the required dependencies.
`pip install -r requirements.txt`

5. Start the python server, enter `python3 run.py`.
If there are no errors, you should see a number of lines, including this one:
```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Then, you can enter `http://127.0.0.1:5000/` (your link may be different) into your browser URL to view the platform.
I recommend you open it on incognito (to prevent caching where the display doesn't reflect current changes). Then, upon making changes on the frontend, you should use a hard reload instead (`cmd` + `shift` + `r`)

6. Open a new terminal window (`ctrl` + `t`) -- This should be in the same directory

7. Navigate to the frontend files (`cd templates/static`)

8. Install frontend dependencies (`npm install`)

9. Run this command so that the frontend updates automatically (`npm run watch`).

You may need to install several dependencies such as python3. You may also need to install libraries such as node, which you can install via HomeBrew.

If you closed the program and need to reopen it, follow these steps:

1. Navigate to the repository. (`cd github-social`)

2. Activate the python virtual environment. (`. venv/bin/activate`)

3. Start the python server, enter `python3 run.py`.

4. Open a new terminal window (`ctrl` + `t`) -- This should be in the same directory

5. Navigate to the frontend files (`cd templates/static`)

6. Run this command so that the frontend updates automatically (`npm run watch`).
