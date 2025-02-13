# Email-SMS_Spam_Classification
# SMS Spam Classification

This project implements an SMS Spam Classification application using Streamlit and machine learning models trained with scikit-learn. The app can distinguish between spam and ham (legitimate) messages.

## Features
- Classify SMS messages as spam or ham
- Interactive web interface built with Streamlit
- Preprocessing with NLTK (stopwords, tokenization)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sms-spam-classification.git
cd sms-spam-classification
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Download necessary NLTK resources:
```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

## Running the App

```bash
streamlit run index.py
```

## File Structure
- `index.py`: Main application file
- `requirements.txt`: Dependencies for deployment

## Deployment on Streamlit Cloud
1. Push the code to a GitHub repository.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect your repository and deploy the application.

## Testing
For testing, you can use the following spam message:
```
Congratulations! 🎉 You’ve won a $1,000 gift card. Click here: http://fake-link.com to claim your prize now! 🚨
```

## License
This project is licensed under the MIT License.

