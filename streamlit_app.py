import streamlit as st
import requests

BASE_URL = "http://localhost:9000"

st.title("Chat Summarization Interface")

user_id = st.text_input("User ID", "alice")
conversation_id = st.text_input("Conversation ID", "convo1")
sender = st.text_input("Sender Name", "Alice")

message = st.text_area("Your Message")
if st.button("Send Message"):
    res = requests.post(f"{BASE_URL}/chats", json={
        "user_id": user_id,
        "conversation_id": conversation_id,
        "message": message,
        "sender": sender,
    })
    st.success("Message sent!" if res.ok else res.text)

if st.button("Summarize Conversation"):
    res = requests.post(f"{BASE_URL}/chats/summarize", json={"conversation_id": conversation_id})
    if res.ok:
        st.subheader("Summary:")
        st.write(res.json().get("summary"))
    else:
        st.error("Failed to generate summary")

if st.button("Show Chat History"):
    res = requests.get(f"{BASE_URL}/chats/{conversation_id}")
    if res.ok:
        st.subheader("Chat History:")
        for msg in res.json():
            st.markdown(f"**{msg['sender']}**: {msg['message']} ({msg['timestamp']})")
    else:
        st.error("Error loading chat")
