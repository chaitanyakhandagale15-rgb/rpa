import json
import subprocess
import pandas as pd
import streamlit as st
import io

# Set the page configuration with a custom title and layout
st.set_page_config(
    page_title="E-commerce Price Tracker",
    page_icon="🛒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Add some custom CSS to style the page
st.markdown("""
    <style>
    /* Add a background color */
    body {
        background-color: #f0f2f6;
    }

    /* Custom font for headers */
    h1, h2 {
        font-family: 'Arial Black', Gadget, sans-serif;
        color: #333;
    }

    /* Center the input box */
    .stTextInput {
        text-align: center;
        padding: 10px;
    }

    /* Style the button */
    .stButton button {
        background-color: #ff4b4b;
        color: white;
        padding: 10px;
        border-radius: 10px;
        border: none;
        font-size: 16px;
        cursor: pointer;
        width: 200px;
        margin-top: 10px;
    }

    .stButton button:hover {
        background-color: #ff3333;
    }

    /* Center content */
    .block-container {
        max-width: 600px;
        padding-top: 50px;
    }

    /* Add footer */
    footer {
        font-size: 12px;
        text-align: center;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# Define a function to trigger UiPath automation
def run_uipath_automation(product_name):
    # Format the product name into a valid JSON string
    input_data = json.dumps({"product_name": product_name})

    # Path to your published .nupkg file
    package_path = r"C:\Users\nithy\Documents\UiPath\BlankProcess\BlankProcess.1.0.3.nupkg"

    # Call UiRobot.exe with the published package path
    result = subprocess.run(
        [r"C:\Users\nithy\AppData\Local\Programs\UiPath\Studio\UiRobot.exe", "execute", "-f", package_path, f"--input={input_data}"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    if result.returncode == 0:
        return True  # Return success
    else:
        return False, result.stderr.decode()

# Streamlit App Layout
st.title("🛒 E-commerce Price Tracker")
st.subheader("Easily track product prices from various online stores")

# Centered container with box shadow effect for better UI
st.markdown("""
    <div style="background-color: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    """, unsafe_allow_html=True)

# Input text box for product name
product_name = st.text_input("Enter the Product Name", "")

# Button to track prices
if st.button("Track Prices"):
    if product_name:
        st.info("Tracking prices, please wait...")
        success = run_uipath_automation(product_name)  # Call UiPath automation
        if success:
            st.success(f"Tracking initiated for {product_name}")

            # Load data from Excel sheet
            excel_file_path = r"C:\Users\nithy\Documents\UiPath\BlankProcess\productprice.xlsx"  # Change this to your Excel file path
            try:
                df = pd.read_excel(excel_file_path)  # Load the Excel file into a DataFrame
                st.table(df)  # Display the DataFrame as a table

                # Prepare to download the Excel file
                excel_buffer = io.BytesIO()
                with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False)
                excel_buffer.seek(0)  # Move to the start of the buffer

                st.download_button(
                    label="Download Excel File",
                    data=excel_buffer.getvalue(),
                    file_name='product_prices.xlsx',
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
            except Exception as e:
                st.error(f"Failed to load data from Excel: {str(e)}")
        else:
            st.error("Failed to initiate tracking.")
    else:
        st.error("Please enter a product name.")

# Close the container
st.markdown("</div>", unsafe_allow_html=True)
