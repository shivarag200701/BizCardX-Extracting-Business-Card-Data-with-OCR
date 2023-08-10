from function import *
from sql import *
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import io
import numpy as np
import os


st.set_page_config(page_title=":BizCardX: Extracting Business Card Data with OCR | by SHIVA RAGHAV",
                   page_icon= "🇮🇳",
                   layout="wide",
                   initial_sidebar_state="expanded",
                   menu_items={'About': """# This OCR app is created by *SHIVA RAGHAV*!"""})
st.markdown("<h1 style='text-align: center; color: violet;'>BizCardX: Extracting Business Card Data with OCR</h1>",
            unsafe_allow_html=True)

css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"]  p{font-size: 25px;}  p{font-family: Arial;}  p {color: blue;}
</style>
'''
def setting_bg():
    st.markdown(f""" <style>.stApp {{
                        background:url("https://pixabay.com/get/gbdc0f9b72eb0e52e48f14cfee02caaedf21335131e182859a0607f6392ed2230cc9c060a9c51d5aeb00dd34bd3f395f9.jpg");
                        background-size: cover}}
                     </style>""", unsafe_allow_html=True)


setting_bg()
selected = option_menu(None, ["Home","Data Extraction","View The Stored Data"],
                       icons=["house","cloud-upload","list-task"],
                       default_index=0,
                       orientation="horizontal",
                       styles={"nav-link": {"font-size": "35px", "text-align": "centre", "margin": "-2px", "--hover-color": "#6495ED"},
                               "icon": {"font-size": "35px"},
                               "container" : {"max-width": "6000px"},
                               "nav-link-selected": {"background-color": "#6495ED"}})
st.markdown(css, unsafe_allow_html=True)

if selected == "Home":
    col1 , col2 = st.columns(2)
    with col1:
        st.image(Image.open(r"C:\Users\SHIVA\Downloads\Business-Cards-extraction-2.png"),width=500)
        st.markdown("## :green[**Technologies Used :**] :violet[Python,easy OCR, Streamlit, SQL, Pandas,OpenCV]")
    with col2:
       st.write("## :green[**About :**] :violet[Bizcard is a Python application designed to extract information from business cards.]")
       st.write('## :violet[The main purpose of Bizcard is to automate the process of extracting key details from business card images, such as the name, designation, company, contact information, and other relevant data. By leveraging the power of OCR (Optical Character Recognition) provided by EasyOCR, Bizcard is able to extract text from the images.]')


if selected == "Data Extraction":
    a=st.file_uploader("Choose a file")
    if a is not None:
        def save_card(uploaded_card):
            uploaded_cards_dir = os.path.join(os.getcwd(), "uploaded_cards")
            with open(os.path.join(uploaded_cards_dir,a.name), "wb") as f:
                f.write(uploaded_card.getbuffer())


        save_card(a)

        saved_img = os.getcwd() + "\\" + "uploaded_cards" + "\\" + a.name
        reader = easyocr.Reader(['en'])
        result = reader.readtext(saved_img)


        #function for converting img to binary format
        def img_to_binary(img):
            input_image = Image.open(img)
            image_bytes = io.BytesIO()
            input_image.save(image_bytes, format='PNG')
            image_data = image_bytes.getvalue()
            return image_data

        data = {'Name': [], 'Designation': [], 'area': [], 'city': [], 'state': [], 'pin_code': [], 'Contact_no': [],
                'Email_id': [], 'Website': [], 'Company_name': [],'image':img_to_binary(saved_img)}
        data = fun(result,data)
        df = pd.DataFrame(data)
        st.dataframe(df)
        # # DISPLAYING THE UPLOADED CARD
        col1, col2 = st.columns(2, gap="large")
        with col1:
            st.markdown("#     ")
            st.markdown("#     ")
            st.markdown("### :violet[**You have uploaded the card**]")
            st.image(a)
        # # DISPLAYING THE CARD WITH HIGHLIGHTS
        with col2:
            st.markdown("#     ")
            st.markdown("#     ")
            with st.spinner("### :violet[**Please wait processing image...**]"):
                img = cv2.imread(saved_img)
                for detection in result:
                    top_left = tuple(int(val) for val in detection[0][0])
                    bottom_right = tuple(int(val) for val in detection[0][2])
                    text = detection[1]
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 4)
                    img = cv2.putText(img, text, top_left, font, 0.75, (255, 0, 0), 2, cv2.LINE_AA)
                st.markdown("### :violet[ **Image Processed and Data Extracted**]")
                st.image(img)
        upload=st.button("### :violet[upload to MySql server]")
        if upload:
            for i, row in df.iterrows():
                sql = '''INSERT INTO biz_card_data(name ,designation ,area ,city ,state ,pin_code ,Contact_no ,email_id ,website ,company_name ,image) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                cursor.execute(sql, tuple(row))
                # the connection is not auto committed by default, so we must commit to save our changes
                cnx.commit()
                st.write("successfully uploaded ")
if selected == "View The Stored Data":
    cursor.execute('''select id, name ,designation ,area ,city ,state ,pin_code ,Contact_no ,email_id ,website ,company_name ,image from biz_card_data''')
    df1 = pd.DataFrame(cursor.fetchall(), columns=['S.no','Name', 'Designation', 'area', 'city', 'state', 'pin_code', 'Contact_no','Email_id', 'Website', 'Company_name','image'])
    st.dataframe(df1)
