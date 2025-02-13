import streamlit as st
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
import pickle
import random

# Initialize Porter Stemmer
ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    # Remove non-alphanumeric characters
    y = [i for i in text if i.isalnum()]

    # Remove stopwords and punctuation
    y = [i for i in y if i not in stopwords.words('english') and i not in string.punctuation]

    # Apply stemming
    y = [ps.stem(i) for i in y]

    return ' '.join(y)

# Load vectorizer and model
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

# Streamlit UI
st.set_page_config(page_title="Spam Classifier", page_icon="📧", layout="wide")

# Apply colorful interactive background with gradient animation
def set_background():
    st.markdown("""
        <style>
            .main {
                background: linear-gradient(270deg, #FF6B6B, #6BCB77, #4D96FF, #FFD93D, #C65D7B);
                background-size: 1000% 1000%;
                animation: gradientAnimation 15s ease infinite;
            }
            @keyframes gradientAnimation {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
        </style>
    """, unsafe_allow_html=True)

set_background()

# Sidebar for search history
st.sidebar.title("🔍 Search History")
if "history" not in st.session_state:
    st.session_state.history = []

if st.sidebar.button("🔄 Reset History"):
    st.session_state.history.clear()

if st.session_state.history:
    for idx, entry in enumerate(reversed(st.session_state.history[-10:])):
        st.sidebar.markdown(
            f"**{idx + 1}.** {entry['message']} → `{entry['prediction']}`"
        )
else:
    st.sidebar.info("No search history available yet.")

# Main content
st.markdown("""
    <div style="text-align: center;">
        <h1 style="color: #3498db;">📧 Email/SMS Spam Classifier</h1>
    </div>
    <hr style="border: 2px solid #3498db;">
""", unsafe_allow_html=True)

# Input area
st.markdown("#### 📝 Enter the message below:")
input_sms = st.text_area("", placeholder="Type your message here...", height=150)

col1, col2 = st.columns([1, 1])

# Predict button and logic
with col1:
    if st.button("🔍 Predict", use_container_width=True):
        if input_sms.strip() == "":
            st.warning("⚠️ Please enter a message to classify.")
        else:
            # Preprocess, vectorize, and predict
            transform_sms = transform_text(input_sms)
            vector_input = tfidf.transform([transform_sms])
            result = model.predict(vector_input)[0]

            # Save to history
            prediction = "Spam" if result == 1 else "Not Spam"
            st.session_state.history.append({"message": input_sms, "prediction": prediction})

            # Display the result with styling
            if result == 1:
                st.markdown(
                    """<div style="text-align: center;">
                        <h2 style="color: red;">🚨 Spam!</h2>
                        <p style="color: darkred;">Be cautious — this message looks like spam.</p>
                    </div>""",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    """<div style="text-align: center;">
                        <h2 style="color: green;">✅ Not Spam</h2>
                        <p style="color: darkgreen;">This message seems safe.</p>
                    </div>""",
                    unsafe_allow_html=True
                )

# Reset input button
with col2:
    if st.button("🧹 Reset Input", use_container_width=True):
        st.session_state.input_sms = ""

# Footer
st.markdown("""
    <hr>
    <div style="text-align: center; color: grey;">
        Made with ❤️ using Streamlit By Abhishek Yadav
    </div>
""", unsafe_allow_html=True)
