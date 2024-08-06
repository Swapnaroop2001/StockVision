# Stuut Fullstack Interview

## Overview

This project is designed to assess your fullstack development skills using Vue and Python.

The goal of this project is to create an application where users can search for stocks and view stock data.

## Getting Started

1. Clone the project repository to your local machine.
2. Navigate to the project directory and install dependencies
3. Start the development server

## Project Requirements

- **Stock Search:** Implement a search feature that allows users to find stocks by ticker symbol.

- **View Stock Information:** Create a flow that allows users to view individual stock information after searching for a stock.

- **3rd Party Libraries:** Look through the recommended stock data libraries and implement them in your project.
  
- **ReadMe:** Include a `readme.md` file with next steps you'd take to get this project ready for production. Please feel free to also include any thoughts on what else you would've added if you did not get through all the project requirements within the allotted time. 

## Recommended Libraries

1. [yfinance](https://pypi.org/project/yfinance/)

## API Endpoint

An API endpoint has been provided to give an example on how the Python Flask API functionality works.

## Evaluation Criteria

Your project will be evaluated based on the following criteria:

- **Functionality:** Search and viewing stock information should work as expected
- **Organization/Quality:** Ensure code is structured well and extensible for future use
- **Design Decisions:** Ability to implement a reasonable design without much direction and the limited time

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/)

## Type Support for `.vue` Imports in TS

TypeScript cannot handle type information for `.vue` imports by default, so we replace the `tsc` CLI with `vue-tsc` for type checking. In editors, we need [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) to make the TypeScript language service aware of `.vue` types.

## Project Setup

### Python Server

1. Ensure you have Python 3 installed. You can check this by running `python3 --version` in your terminal.
   If Python 3 is not installed, you can install it using Homebrew with the command `brew install python3`.

2. Install the required Python packages. In the project directory, run the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
pip install flask-cors
```

3. Run the Python server

```bash
python server.py
```

### Frontend UI

Install dependencies

```bash
npm install
```

Compile and hot-reload the frontend

```bash
npm run dev
```

Open `http://localhost:5173/` in your browser to see the project.
