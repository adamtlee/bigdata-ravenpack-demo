# Bigdata API Client

This repository contains a simple Python script to interact with the Bigdata.com API, demonstrating dependency management and secure environment variable handling.

## 🚀 Getting Started

Follow these steps to set up the project environment and run the main script.

### 1. Clone the Repository

If you haven't already, clone the project to your local machine:

```bash
git clone https://github.com/adamtlee/bigdata-ravenpack-demo
cd bigdata-ravenpack-demo

```

----------

## 2. Environment Setup (macOS/Linux)

This project uses a Python **virtual environment** to isolate dependencies.

### A. Create and Activate the Environment

The following commands use the standard `venv` module. Since the original environment was created on a Mac, we'll assume a Unix-like shell (macOS/Linux):

Bash

```
# 1. Create the virtual environment named 'venv'
python3 -m venv env

# 2. Activate the environment
source env/bin/activate

# Your terminal prompt should now show (env)

```

### B. Install Dependencies

Install all necessary packages using the `requirements.txt` file:

Bash

```
pip install -r requirements.txt

```

----------

## 3. Configuration

### Securely Specify the API Key

For security, the project requires an API key to be stored in a local `.env` file, which is ignored by Git.

1.  **Create the `.env` file:** Copy the provided example file to create your local environment file:
    
    Bash
    
    ```
    cp .env.example .env
    
    ```
    
2.  **Edit the `.env` file:** Open the newly created `.env` file and replace the placeholder with your actual test key:
    
    Code snippet
    
    ```
    # .env
    BIGDATA_API_KEY=your_actual_test_key_goes_here
    
    ```
    

----------

## 4. Run the Script

The main execution file is located in the `chat/` directory.

### Execute `main.py`

Navigate to the `chat` folder and execute the script:

Bash

```
# 1. Change to the script directory
cd chat

# 2. Run the main script
python main.py

```

The script will now load the API key from the root-level `.env` file and execute its logic.

### 🛑 To Exit the Environment

When you are done working on the project, deactivate the virtual environment:

Bash

```
deactivate
```
