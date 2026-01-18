import streamlit as st
from ollama import chat
import os

# Page Configuration
st.set_page_config(page_title="AI-Edge Chat", layout="wide")
st.title("🤖 AI-Edge: Chat with AI Models")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar - Model Selection
st.sidebar.header("Select AI Model")
model_options = {
    "DeepSeek R1 (Fast & Reasoning)": "deepseek-r1:1.5b",
    "Gemma 2B (Lightweight)": "gemma:2b",
    "Gemma 3 (4B • Vision Enabled)": "gemma3:4b",
}
selected_model = st.sidebar.radio(
    "Choose a model:",
    list(model_options.keys())
)

# Prompt Input
st.subheader("💬 Enter Your Prompt")
prompt = st.text_area("Type your query here", height=150)

# Image Input (Only for Gemma 3 Vision)
image_path = None
if selected_model == "Gemma 3 (4B • Vision Enabled)":
    st.subheader("🖼️ Optional Image Input")

    image_path_input = st.text_input(
        "Enter image path (absolute or relative)",
        placeholder="e.g. ./image.jpg or C:/Users/Name/image.png"
    )

    if image_path_input:
        resolved_path = os.path.abspath(image_path_input)
        if os.path.exists(resolved_path):
            image_path = resolved_path
            st.success("Image found ✔")
        else:
            st.error("Image path not found ❌")

# Get Response
if st.button("🚀 Get Response"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        try:
            messages = [{"role": "user", "content": prompt}]

            # Add image only if valid & model supports vision
            if selected_model == "Gemma 3 (4B • Vision Enabled)" and image_path:
                messages[0]["images"] = [image_path]

            response = chat(
                model=model_options[selected_model],
                messages=messages
            )

            if response and "message" in response and "content" in response["message"]:
                ai_response = response["message"]["content"]

                st.session_state.chat_history.append({
                    "user": prompt,
                    "ai": ai_response,
                    "model": selected_model,
                    "image": image_path
                })

                st.success("✅ Response Received!")
            else:
                st.error("Unexpected response format.")

        except Exception as e:
            st.error(f"Error while getting response: {e}")

# Display Chat History
if st.session_state.chat_history:
    st.subheader("📝 Chat History")

    for item in reversed(st.session_state.chat_history):
        with st.chat_message("user"):
            st.markdown(f"**You ({item['model']}):**\n\n{item['user']}")
            if item.get("image"):
                st.caption(f"🖼️ Image: {item['image']}")

        with st.chat_message("assistant"):
            st.markdown(item["ai"])

# Clear Chat Button (Safe)
if st.button("🗑️ Clear Chat"):
    st.session_state.chat_history.clear()
    st.rerun()

# Footer
st.markdown("---")
st.caption("Powered by AI-Edge")
