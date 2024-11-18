# Real Estate Price Predictor

A real estate price prediction application based on location, size, number of bathrooms, and more within Bengaluru city. Data Pre-Processing, Exploratory Data Analysis, Machine Learning, and a simple HTML, CSS, and JavaScript frontend using Flask as the backend.

---

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset Overview](#dataset-overview)
- [Modeling and Prediction](#modeling-and-prediction)
- [Web Deployment](#web-deployment)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- Data cleaning and preprocessing for structured analysis.
- Outlier detection and removal for accurate predictions.
- Custom prediction model using Linear Regression.
- Interactive web interface for user-friendly predictions.
- Exported machine learning model for deployment.

---

## Technologies Used
- **Programming Languages:** Python, JavaScript, HTML, CSS
- **Libraries:**
  - Data Analysis: `pandas`, `numpy`
  - Visualization: `matplotlib`
  - Machine Learning: `sklearn`
- **Frameworks:** Flask
- **Tools:** JSON, Pickle for model and data management.

---

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip
- Virtual environment (optional but recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/real-estate-price-predictor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd real-estate-price-predictor
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask server:
   ```bash
   python app.py
   ```
5. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

---

## Usage

### Using the Web Interface
1. Enter the following inputs:
   - Location
   - Total Square Feet
   - Number of Bedrooms (BHK)
   - Number of Bathrooms
2. Click on the "Predict" button to get the estimated price.

### Prediction via Python Script
```python
from predict import predict_price

# Example Prediction
price = predict_price('Indira Nagar', 1000, 2, 2)
print(f"Estimated Price: ₹{price} Lakhs")
```

---

## Dataset Overview
The project uses a dataset containing house prices in Bengaluru with features like:
- Location
- Total square feet
- Number of bedrooms (BHK)
- Bathrooms
- Price

Key steps in data processing:
- Handled missing values and inconsistent data.
- Converted total square feet from ranges to numeric values.
- Added features like `price_per_sqft` and `bhk`.

---

## Modeling and Prediction
- **Model:** Linear Regression.
- **Cross-validation:** Shuffle Split cross-validation with 5 splits.
- **Performance Metric:** R² score.
- **Deployment:** Model serialized with Pickle and integrated with Flask.

Example predictions:
```python
predict_price('1st Phase JP Nagar', 1000, 2, 2)  # Expected Output: Price in Lakhs
predict_price('Indira Nagar', 1000, 3, 2)        # Expected Output: Price in Lakhs
```

---

## Web Deployment

The application uses:
- **Backend:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **Interaction:** Users input property details, and the backend predicts the price.

### Frontend Screenshot
![Frontend Screenshot](screenshot.png)

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit changes:
   ```bash
   git commit -m "Add a feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## **License**
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

Feel free to expand sections as needed or modify for your specific use case!
