import streamlit as st

st.title("Title -> Streamlit")
st.header("Header -> Streamlit")
st.subheader("Sub-Header -> Streamlit")
st.text("Text -> Streamlit")


st.markdown("# Hello")                        #Markdowns(or Headings in HTML) as in Jupyter's notebook 
st.markdown("## Hello")
st.markdown("### Hello")
st.markdown("#### Hello")
st.markdown("##### Hello")
st.markdown("###### Hello")


st.info("Information")                        #Information
st.success("Success")                         #Success
st.warning("Warning")                         #Warning
st.error("Error")                             #Error
st.exception(ZeroDivisionError("Division not possible with 0"))         #Exception


st.write("range(1,10)")                       #Write
st.write(range(1,10))
st.write("1+2+3+4")
st.write(1+2+3+4)
# st.write(1*2*30)


st.code('for i in range(1,10):\n'                               
        '\t print(i)')                       #Code              


st.subheader("Checkbox")                     #Checkbox
st.checkbox("Male")                          
if(st.checkbox("Adult")):
    st.write("You're an adult")


st.subheader("Radio button")                 #Radio button
radio_ch = st.radio('Select a Gender:', ('Male', 'Female', 'Other'))
if radio_ch == "Male":
    st.write("You're a Male")
elif radio_ch == "Female":
    st.write("You're a Female")
else:
    st.write("You're Other gender")


st.subheader("Select box")                              #Select Box
st.markdown("##### Select your domain in Data Science:")                    

sel = st.selectbox("Data Science: ", ["Data Analytics", "Machine Learning", "Natural Language Processing","Image Processing", "Web Scraping", "Computer Vision"])

st.write("You've selected",sel)


st.subheader("Multiple Select box")                     #Multiple select box
st.markdown("##### Select multiple courses:")

mulsel = st.multiselect("Data Science: ", ["Data Analytics", "Machine Learning", "Natural Language Processing","Image Processing", "Web Scraping", "Computer Vision"])

st.write("You've selected", len(mulsel),"courses.")


st.subheader("Button")                                   #Button
if(st.button("Click me")):
    st.write("Thanks for clicking me!")


st.subheader("Slider")                                   #Slider
vol = st.slider("Select the volume: ",1,100,step = 1)
st.write("The volume you've selected is: ",vol)


st.subheader("Text Input")                               #Text Input                  
username = st.text_input("Name: ")
password = st.text_input("Password: ",type="password") 


st.subheader("Text Area")                                #Text Area
st.text_area("Write something about yourself here...")


st.subheader("Number Input")                             #Number Input 
st.number_input("Select your age:",18,110)


st.subheader("Date Input")                               #Date Input 
st.date_input("Date")


st.subheader("Time Input")                               #Time Input 
st.time_input("Time")