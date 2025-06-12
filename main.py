import requests
import json
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

# Load environment variables
BASE_API_URL = os.getenv("BASE_API_URL")  # e.g., http://localhost:7868
LANGFLOW_ID = os.getenv("LANGFLOW_ID")    # e.g., 2d461291-0362-435d-9737-ce8542b48d78
APPLICATION_TOKEN = os.getenv("APPLICATION_TOKEN")  # Your token, if needed

def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/api/v1/run/{LANGFLOW_ID}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat"
    }

    headers = {
        "Content-Type": "application/json"
    }

    if APPLICATION_TOKEN:
        headers["Authorization"] = f"Bearer {APPLICATION_TOKEN}"

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return {"error": str(e)}
    except ValueError as e:
        print(f"Response parsing error: {e}")
        return {"error": str(e)}

# ✅ Streamlit app
def main():
    st.title("Langflow Chat Interface")
    message = st.text_area("Message", placeholder="Ask something...")

    if st.button("Run Flow"):
        if not message.strip():
            st.error("Please enter a message.")
            return

        try:
            with st.spinner("Running flow..."):
                response = run_flow(message)
                # Extract response text safely
                try:
                    result = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
                except Exception:
                    result = response.get("error", "Unexpected response format.")
                st.markdown(f"**Response:** {result}")
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
