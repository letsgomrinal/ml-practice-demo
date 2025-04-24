from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib

# 1. Data
data = pd.DataFrame({
    "text": [
        "Reset my password", "Delete account", "Talk to support",
        "Update email", "Cancel subscription", "Recover account"
    ] * 2,
    "intent": [
        "reset_password", "delete_account", "contact_support",
        "update_profile", "cancel_subscription", "recover_account"
    ] * 2
})

X_train, X_test, y_train, y_test = train_test_split(
    data["text"], data["intent"], test_size=0.3, stratify=data["intent"], random_state=42
)

# 2. Pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), stop_words="english")),
    ("clf", LogisticRegression(max_iter=1000))
])

# 3. Train
pipeline.fit(X_train, y_train)

# 4. Export
joblib.dump(pipeline, "intent_classifier.joblib")

# 5. Load elsewhere
model = joblib.load("intent_classifier.joblib")

# 6. Predict
print(model.predict(["I forgot my password"]))
