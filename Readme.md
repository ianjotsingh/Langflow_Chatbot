# Langflow FAQ Chatbot 💬

This is a customer support chatbot powered by [Langflow](https://github.com/logspace-ai/langflow) and [Streamlit](https://streamlit.io/).  
It connects to a Langflow flow via API and provides real-time responses for FAQs, order tracking, or any support queries.

---

## 📂 Project Structure


---

## 🚀 How to Run Locally

### 1. Clone the Repo

git clone https://github.com/YOUR_USERNAME/langflow-chatbot.git
cd langflow-chatbot

2. Create and Fill .env
Create a .env file based on the example:
BASE_API_URL=http://localhost:7868
LANGFLOW_ID=your-langflow-id-here
APPLICATION_TOKEN=your-token-if-required
3. Install Requirements
pip install -r requirements.txt
4. Run the App
streamlit run app.py

🌐 Example Use Case

This chatbot can:
Answer product or service FAQs
Respond to customer queries about orders
Assist with troubleshooting steps
Generate dynamic answers using your own Langflow pipeline

🛡️ Security Note

Make sure you do not commit your .env file to GitHub. Use .gitignore to protect it and share only the .env.example.

🧠 Built With

Langflow
Streamlit
Python Requests
python-dotenv

🙋‍♂️ Author

Developed by Ianjot Singh

📄 License

This project is licensed under the MIT License

---

✅ You can now paste this entire content into a new `README.md` file in your project folder or directly on GitHub.

Let me know if you want:
- Markdown preview for how it looks
- GitHub badges (stars, forks, license, etc.)
- A LICENSE file (MIT or custom)



