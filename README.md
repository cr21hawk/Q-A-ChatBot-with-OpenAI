# Q&A ChatBot with OpenAI

## Step 1: Create an environment
```bash
conda create -n ENV_NAME python=3.11.10 -y
```
> [!NOTE]
> You should have to replace `ENV_NAME` with your custom environment name.

## Step 2: Activate environment
```bash
conda create -n ENV_NAME
```

## Step 3: Install the requiremnts.txt
```bash
pip install -r requiremnets.txt
```

## Step 4: Create `.env` file
```bash
touch .env
```
## Step 5: Create a secret API key
1. Follow the steps mentioned on this page <a href="https://smith.langchain.com/settings" target="_blank">smith.langchain.com/settings</a>

    ```bash
    LANGCHAIN_API_KEY = ""
    LANGCHAIN_PROJECT = "Q&A ChatBot with OpenAI"
    ```
2. Create an OpenAI API key <a href="https://platform.openai.com/api-keys" target="_blank">platform.openai.com/api-keys</a>

## Step 6: Run the app
```bash
streamlit run app.py
```


