import requests
import streamlit as st
from dotenv import load_dotenv
import os

# ✅ Load .env variables
load_dotenv()
BASE_API_URL = os.getenv("BASE_API_URL")
LANGFLOW_ID = os.getenv("LANGFLOW_ID")
APPLICATION_TOKEN = os.getenv("APPLICATION_TOKEN")

# ✅ Call Langflow API
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
        return {"error": f"Request error: {e}"}
    except ValueError as e:
        return {"error": f"Response error: {e}"}

# ✅ Streamlit UI
def main():
    st.title("🚀 Langflow FAQ Assistant")
    message = st.text_area("Enter your message:")

    if st.button("Run Flow"):
        if not message.strip():
            st.warning("Please enter a message.")
            return

        with st.spinner("Sending message to Langflow..."):
            result = run_flow(message)
            try:
                output = result["outputs"][0]["outputs"][0]["results"]["message"]["text"]
                st.markdown(f"### 💬 Response:\n{output}")
            except Exception:
                st.error(result.get("error", "❌ Unexpected response format."))

if __name__ == "__main__":
    main()
