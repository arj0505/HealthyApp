import streamlit as st
from PIL import Image
import google.generativeai as genai
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configure Gemini Pro Vision API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini response
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0]])
    return response.text

# Function to handle image setup
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Main Streamlit app
st.set_page_config(page_title="Health Calories Information App 👨‍⚕️")
st.title("Health Calories Information App")

# Sidebar with explanation about the app
st.sidebar.title("App Explanation")


# Load your image
#image_path1 = r"C:\Arjun_workstation\NLP_Models\Healthapp\doctor.jpg"
#image_path1 = r"https://github.com/arj0505/HealthyApp/blob/main/doctor.jpg"
#image1 = Image.open(image_path1)

# Display the image on the left side of the sidebar
#st.sidebar.image(image1, use_column_width=True)

st.sidebar.markdown("""
    Building a Health Calories Information App involves leveraging image recognition technology to analyze images of 
    food and extract valuable information related to their caloric content. Here's a more detailed explanation:

**Step 1:** User Upload any food Image

**Step 2:** Image Recognition Technology

**Step 3:** Caloric Content Extraction

                    """)

# Main content area
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    input_prompt = """
        You are an expert in nutritionist where you need to see the food items from the image
        and calculate the total calories. Provide details for each food item in the format:

        1. Item 1 - no of calories
        2. Item 2 - no of calories
        ----
        ----

        Mention whether the food is healthy and provide the percentage split of carbohydrates, fats, fibers, sugar, etc.
    """

    st.image(Image.open(uploaded_file), caption="Uploaded Image.", use_column_width=True)
    input_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, input_data)
    
    st.subheader("Calories Information:")
    st.write(response)
