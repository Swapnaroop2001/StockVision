## Getting Started

1. Clone the project repository to your local machine.
2. Navigate to the project directory and install dependencies
3. Start the development server


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

## Sample Image

Here’s a sample image for reference:

![Sample Image](https://github.com/Swapnaroop2001/StockVision/blob/main/src/assets/aapl.png)