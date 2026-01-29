import streamlit as st
#header
st.header("Welcome to the Streamlit App")

#title
st.title("welcome to student Application")

#subheader
st.subheader("This is a subheader for additional context")

#text
st.text("This is a simple text element in the Streamlit app.")

#markdown
st.markdown("### ------------ Markdown Section ------------")
st.markdown("This is a **bold** text and this is an *italic* text in markdown.")
st.markdown("- Item 1\n- Item 2\n- Item 3")
st.divider()

#write
st.write("hello streamlit.")
#write method with different data types
st.write(123)
st.write([1, 2, 3])
st.write({"name": "Alice", "age": 30})

st.markdown("<h3 style='color:blue;'>--RED TEXT-- </h3>", unsafe_allow_html=True)

#caption
st.caption("This is a caption providing additional information.")
st.divider()

#code methodto display code snippets
st.code("""
        def add(a, b):
            return a + b
        """, language='python')

#latex
st.latex(r''' a^2 + b^2 = c^2 ''')

#divider method to separate sections(horizontal line)
st.divider()

#button with success message and balloons
if st.button("Click Me"):
    st.write("Button clicked!")
    st.success("Success! You clicked the button.")
    st.balloons()
else:
    st.write("Button not clicked yet.")
    st.error("Error! You haven't clicked the button yet.")
st.divider()

   
#number input
age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25)
st.write(f"You are {age} years old.")


#text input
name = st.text_input("Enter your name:")
st.write(f"Hello, {name}!")
st.divider()

#validation for name input
if name == " ":
    st.warning("name cannot be empty!.")
elif not name.isalpha():
    st.error("name should only contain alphabetic characters.")
else:
    st.success("name is valid.")
st.divider()

#text area
comments = st.text_area("Enter your comments:")
st.write("Your comments:", comments)
st.divider()

#checkbox
if st.checkbox("I agree to the terms and conditions"):
    st.write("Thank you for agreeing!")
st.divider()

#radio buttons
gender = st.radio("Select your gender:",("Male","Female","Other"))
st.write(f"You selected: {gender}")
st.divider()

#selectbox
country = st.selectbox("Select your country:",("USA","Canada","UK","Australia","india "))
st.write(f"You selected: {country}")
st.divider()

#multiselect method to create multiple selection options dropdown
hobbies = st.multiselect("Select your hobbies:",("Reading","Traveling","Cooking","Sports","Music"))
st.write(f"Your hobbies: {', '.join(hobbies)}")

st.divider()

#slider
satisfaction = st.slider("Rate your satisfaction level:",0,10,5)
st.write(f"Satisfaction level: {satisfaction}")

st.divider()

#file uploader
uploaded_file = st.file_uploader("Upload a file:")
if uploaded_file is not None:
    st.write(f"File '{uploaded_file.name}' uploaded successfully!")

st.divider()

#form
with st.form("my_form"):
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0, max_value=120)
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(f"Form submitted! Name: {name}, Age: {age}")

st.divider()

#form_submit_button outside the form
with st.form("login_form"):
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    login_submitted = st.form_submit_button("Login")
    if login_submitted:
        st.write(f"Login successful! Welcome, {username}.")

st.divider()

#columns
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Column 1")
    st.write("This is the first column.")
with col2:
    st.header("Column 2")
    st.write("This is the second column.")
with col3:
    st.header("Column 3")
    st.write("This is the third column.")
st.divider()

#container
container = st.container()
container.write("This is inside the container.")
container.button("Container Button")
st.divider()

data = {
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)

#sidebar
st.sidebar.title("Sidebar Section")
options = st.sidebar.selectbox("Choose an option:", ["home", "about", " contact"])
st.sidebar.write(f"You selected: {options}")
if options == "home":
    st.sidebar.write("Welcome to the home page!")

st.divider()

#info, warning, error, success messages
st.info("This is an informational message.")
st.warning("This is a warning message.")    
st.error("This is an error message.")
st.success("This is a success message.")

st.divider()

#cache decorator example
@st.cache_data
def load_data():
    # Simulate a time-consuming data loading process
    return {"data": [1, 2, 3, 4, 5]}
data = load_data()
st.write("Loaded data:", data)

st.divider()
st.markdown("### ------------ Markdown Section ------------")


