import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:9000"

st.title("Chat Summarization Interface")

user_id = st.text_input("User ID", "alice")
conversation_id = st.text_input("Conversation ID", "convo1")
sender = st.text_input("Sender Name", "Alice")

# Always Show Chat History
st.subheader("Chat History")
try:
    res = requests.get(f"{BASE_URL}/chats/{conversation_id}")
    if res.ok:
        for msg in res.json():
            st.markdown(f"**{msg['sender']}**: {msg['message']}")
    else:
        st.warning("No chat history found or error fetching chat.")
except Exception as e:
    st.error(f"Failed to fetch chat history: {e}")

# Send Message
message = st.text_area("Your Message")
if st.button("Send Message"):
    try:
        res = requests.post(f"{BASE_URL}/chats", json={
            "user_id": user_id,
            "conversation_id": conversation_id,
            "message": message,
            "sender": sender,
        })
        if res.ok:
            st.success("Message sent!")
            st.experimental_rerun() 
        else:
            st.error(res.text)
    except Exception as e:
        st.error(f"Failed to send message: {e}")

# Summarize
if st.button("Summarize Conversation"):
    res = requests.post(f"{BASE_URL}/chats/summarize", json={"conversation_id": conversation_id})
    if res.ok:
        st.subheader("Summary:")
        st.write(res.json().get("summary"))
    else:
        st.error("Failed to generate summary")

# Analyze
if st.button("Conversation Analysis"):
    res = requests.post(f"{BASE_URL}/chats/analyze", json={"conversation_id": conversation_id})
    if res.ok:
        st.subheader("Analysis:")
        st.write(res.json().get("summary"))
    else:
        st.error("Failed to generate analysis")
