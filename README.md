# 🚗 Car Price Prediction API

A machine learning-based **Car Price Prediction System** built using **Random Forest Regression, FastAPI, Pydantic, and Streamlit**.

The project provides a REST API for predicting the estimated selling price of a used car based on its features, along with a user-friendly Streamlit web interface.


## 📌 Project Overview

The goal of this project is to predict the **selling price of a used car** using machine learning.

The system takes information such as:

* Car name
* Manufacturing year
* Present price
* Kilometers driven
* Fuel type
* Seller type
* Transmission
* Number of previous owners

and uses a trained **Random Forest Regression model** to estimate the car's selling price.

The model prediction is returned in **lakhs**.

---

## ✨ Features

* 🤖 Random Forest Regression model
* 🚀 FastAPI REST API
* ✅ Pydantic input validation
* 🔄 Automatic categorical feature encoding
* 📊 Streamlit interactive frontend
* 📖 Swagger/OpenAPI API documentation
* 🧠 Serialized machine learning model
* 🛡️ Input validation and error handling
* 💻 Local development support
* ☁️ Deployment-ready project structure

---

## 🛠️ Technologies Used

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Programming language |
| Pandas       | Data processing      |
| Scikit-learn | Machine learning     |
| Joblib       | Model serialization  |
| FastAPI      | REST API             |
| Pydantic     | Data validation      |
| Uvicorn      | ASGI server          |
| Streamlit    | Web interface        |
| Requests     | API communication    |

---

## 📂 Project Structure

```text
car-price-prediction-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── model.py
│   ├── schema.py
│   └── streamlit_app.py
│
├── cardekho_data.csv
├── feature_columns.pkl
├── random_forest_model.pkl
├── train.py
├── requirements.txt
├── runtime.txt
├── .gitignore
└── README.md
```

---

## 📊 Dataset

This project uses the **CarDekho used-car dataset**.

The dataset contains information about used cars and their selling prices.

### Input Features

The model uses the following features:

| Feature         | Description                      |
| --------------- | -------------------------------- |
| `Car_Name`      | Name/model of the car            |
| `Year`          | Manufacturing year               |
| `Present_Price` | Current/present price of the car |
| `Kms_Driven`    | Kilometers driven                |
| `Fuel_Type`     | Petrol, Diesel, or CNG           |
| `Seller_Type`   | Dealer or Individual             |
| `Transmission`  | Manual or Automatic              |
| `Owner`         | Number of previous owners        |

### Target Variable

```text
Selling_Price
```

The target represents the estimated selling price of the car.

The dataset prices are represented in **lakhs**.

For example:

```text
5.50 = 5.50 Lakhs
```

---

## 🧠 Machine Learning Model

The project uses:

```text
Random Forest Regressor
```

The trained model is stored as:

```text
random_forest_model.pkl
```

The feature column information used during training is stored as:

```text
feature_columns.pkl
```

These files are loaded by the FastAPI application when the server starts.

---

## 🔄 Prediction Workflow

The application follows this workflow:

```text
User
  │
  ▼
Streamlit Interface
  │
  ▼
FastAPI /predict Endpoint
  │
  ▼
Pydantic Validation
  │
  ▼
Feature Preprocessing
  │
  ▼
Random Forest Model
  │
  ▼
Predicted Selling Price
  │
  ▼
Streamlit Result
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/car-price-prediction-api.git
```

Move into the project directory:

```bash
cd car-price-prediction-api
```

---

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ⚡ Running the FastAPI Backend

From the project root, run:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically provides interactive Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can test the `/predict` endpoint directly from Swagger UI.

---

## 🔮 Prediction Endpoint

### POST

```text
/predict
```

### Example Request

```json
{
    "Car_Name": "alto 800",
    "Year": 2014,
    "Present_Price": 5.5,
    "Kms_Driven": 2184,
    "Fuel_Type": "Diesel",
    "Seller_Type": "Individual",
    "Transmission": "Automatic",
    "Owner": 1
}
```

### Example Response

```json
{
    "prediction_price": 3.25
}
```

The prediction is returned in **lakhs**.

For example:

```text
3.25 Lakhs
```

is approximately:

```text
Rs. 325,000
```

---

# 🖥️ Running the Streamlit Application

Open another terminal while FastAPI is running.

Activate the virtual environment if necessary:

```powershell
.venv\Scripts\Activate.ps1
```

Then run:

```bash
streamlit run app/streamlit_app.py
```

The Streamlit application will open in your browser.

The frontend communicates with the FastAPI backend through:

```text
http://127.0.0.1:8000/predict
```

---

# 🔗 API + Streamlit Architecture

The project separates the frontend and backend.

```text
                ┌─────────────────────┐
                │     Streamlit UI    │
                │  User enters data   │
                └──────────┬──────────┘
                           │
                           │ HTTP POST
                           ▼
                ┌─────────────────────┐
                │      FastAPI        │
                │    /predict         │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    Preprocessing    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Random Forest Model │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Predicted Price     │
                └─────────────────────┘
```

---

## 📦 Model Artifacts

The following files are required by the API:

```text
random_forest_model.pkl
feature_columns.pkl
```

They should be located in the **project root directory**:

```text
car-price-prediction-api/
│
├── random_forest_model.pkl
└── feature_columns.pkl
```

---

## ⚠️ Scikit-learn Compatibility

The trained Random Forest model was created using:

```text
scikit-learn 1.5.1
```

Therefore, the project uses:

```text
scikit-learn==1.5.1
```

in `requirements.txt`.

Keeping the same scikit-learn version helps avoid compatibility issues when loading the serialized `.pkl` model.

---

## 🔧 API Response

### Health Check

```text
GET /
```

Example response:

```json
{
    "success": true,
    "message": "Car Price Prediction API is running"
}
```

---

## 📁 Important Files

### `app/main.py`

Contains the FastAPI application and API endpoints.

### `app/schema.py`

Contains Pydantic models and input validation.

### `app/model.py`

Handles:

* Loading the trained model
* Loading feature columns
* Preprocessing input
* Generating predictions

### `app/streamlit_app.py`

Contains the Streamlit user interface.

### `train.py`

Used for training the machine learning model.

### `random_forest_model.pkl`

Serialized trained Random Forest model.

### `feature_columns.pkl`

Stores the feature columns required by the trained model.

---

## 🎯 Future Improvements

Possible future improvements include:

* [ ] Deploy FastAPI backend to the cloud
* [ ] Connect Streamlit to the deployed API
* [ ] Add model performance metrics
* [ ] Add prediction confidence/uncertainty information
* [ ] Improve feature engineering
* [ ] Add more machine learning models for comparison
* [ ] Add charts and data visualizations
* [ ] Add automatic model retraining
* [ ] Add Docker support
* [ ] Add CI/CD pipeline
* [ ] Add authentication for the API
* [ ] Add database support
* [ ] Improve UI/UX

---

## 📌 Disclaimer

This application provides an **estimated car selling price** based on a machine learning model trained on historical data.

Predictions should not be considered a guaranteed market price. Actual prices may vary depending on vehicle condition, location, market demand, documentation, and other factors.

---

## 👨‍💻 Author

**Burhan Arshad**

Computer Science Student & Machine Learning Enthusiast

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

```
```
