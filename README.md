# Email/SMS Spam Classification

This project implements an Email/SMS Spam Classification application using Streamlit and machine learning models trained with scikit-learn. The app can distinguish between spam and ham (legitimate) messages.

## Features
- Classify SMS messages as spam or ham
- Interactive web interface built with Streamlit
- Preprocessing with NLTK (stopwords, tokenization)
- Utilizes machine learning models like Random Forest and Naive Bayes
- Final model trained with Multinomial Naive Bayes for better accuracy
- Applied knowledge of Natural Language Processing (NLP) and deep learning
- Used `matplotlib.pyplot` and `seaborn` for data visualization
- Evaluated model performance with a confusion matrix to analyze accuracy and precision
- Pickle used for model serialization

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AbhishekYadav915/Email-SMS_Spam_Classification.git

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

## Live App
Access the live application here: [SMS Spam Classifier](https://email-smsspamclassification-vfngqtlnkngjtg5dvwpwa9.streamlit.app/)

## GitHub Repository
Access the code here: [GitHub Repo](https://github.com/AbhishekYadav915/Email-SMS_Spam_Classification.git)

## License
This project is licensed under the MIT License.

