import streamlit as st

st.title("📲🔰Unit Converter App")
st.markdown("### Converts Length, Weight And Time Instantly")
st.write("Welcome! Select a category, enter a value and get the converted result in real-time")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time", "Volume"], index=0,
    format_func=lambda x: f"🔗 {x}")

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24
        
    elif category == "Volume":
        if unit == "Liters to Gallons":
            return value * 0.264172
        elif unit == "Gallons to Liters":
            return value / 0.264172
        elif unit == "Milliliters to Cups":
            return value / 240
        elif unit == "Cups ti Milliliters":
            return value * 240
    return 0
        
if category == "Length":
    st.subheader("Length Conversion")
    unit = st.selectbox("📏 Select Conversation", ["Miles to Kilometers","Kilometers to Miles"])
elif category == "Weight":
    st.subheader("Weight Conversion")
    unit = st.selectbox("⚖️ Select Conversation", ["Kilograms to pounds", "Pounds to kilograms"])
              
elif category == "Volume":
    st.subheader("Volume Conversion")
    unit = st.selectbox("⏱️ Select Conversation", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])

elif category == "Time":
    st.subheader("Time Conversion")
    unit = st.selectbox("🌊 Select Conversion", ["Liters to Gallons", "Gallons to Liters", "Milliliters to Cups", "Cups to Milliliters"])

value = st.number_input("Enter the value to convert", min_value=0.0)

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"**Conversion Result**: {result:.2f} {unit.split(' to ')[1]}")
    