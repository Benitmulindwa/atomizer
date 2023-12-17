from dotenv import load_dotenv
import os

load_dotenv()

FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")

config = {
    "apiKey": FIREBASE_API_KEY,
    "authDomain": "atomizer-97d91.firebaseapp.com",
    "projectId": "atomizer-97d91",
    "storageBucket": "atomizer-97d91.appspot.com",
    "messagingSenderId": "105852276751",
    "appId": "1:105852276751:web:cac78a95e1107d7dc3537a",
    "measurementId": "G-9N42Q7YXY1",
    "databaseURL": "",
}
