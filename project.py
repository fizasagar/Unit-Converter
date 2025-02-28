#Project: Unit Converter

import streamlit as st

# Custom CSS 
st.markdown(
    """
    <style>
    body {
        background-color: #e0f7fa;  /* Soft cyan background */
        color: #2c3e50;
    }
    .stApp {
        background: linear-gradient(135deg, #1e3c72, #00ffff);  
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 40px;
        color: #102a43;  /* Dark blue for a professional look */
        font-weight: bold;
    }

    .stButton>button {
        background: linear-gradient(45deg, #6a11cb, #2575fc);
        color: white;
        font-size: 18px;
        padding: 12px 24px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 225, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #ff758c, #ff7eb3);
        color: white;
    }
    .result-box {
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.2);
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 225, 0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 16px;
        color: #34495e;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title & Description
st.markdown("<h1>🔢 Unit Converter Using Python 🔄</h1>", unsafe_allow_html=True)
st.subheader("Convert length, weight, and temperature instantly! 🚀")

# Sidebar Menu
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length 📏", "Weight ⚖️", "Temperature 🌡️"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length 📏":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])

elif conversion_type == "Weight ⚖️":
    with col1:
        from_unit = st.selectbox("From", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])

elif conversion_type == "Temperature 🌡️":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion Functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches': 39.3701
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1, 'Grams': 1000, 'Milligrams': 1000000,
        'Pounds': 2.20462, 'Ounces': 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return ((value - 32) * 5/9) if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32) if to_unit == "Fahrenheit" else value
    return value 

# Button for conversion
if st.button("🔄 Convert Now!"):
    if conversion_type == "Length 📏":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight ⚖️":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature 🌡️":
        result = temp_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>✅ {value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>💡 Created by Fiza Asif ✨</div>", unsafe_allow_html=True)
