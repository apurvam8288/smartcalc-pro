
import streamlit as st
import math

st.set_page_config(
    page_title="SmartCalc Pro",
    page_icon="🧮",
    layout="wide"
)

# CUSTOM DARK THEME
st.markdown("""
<style>
.stApp {
    background-color: #101827;
    color: white;
}

[data-testid="stHeader"] {
    background-color: #101827;
}

[data-testid="stSidebar"] {
    background-color: #172338;
}

.stApp h1, .stApp h2, .stApp h3,
.stApp p, .stApp label, .stApp span,
.stApp li {
    color: white;
}

.stNumberInput input {
    background-color: #263449;
    color: white;
}

.stSelectbox div[data-baseweb="select"] {
    background-color: #263449;
    color: white;
}

.stButton button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
    border: none;
}

.stButton button:hover {
    background-color: #1d4ed8;
    color: white;
}

/* GREEN RESULT BOXES */
div[data-testid="stAlert"] {
    background-color: #052e16 !important;
    border: 1px solid #16a34a !important;
    border-radius: 10px;
}

div[data-testid="stAlert"] p,
div[data-testid="stAlert"] span,
div[data-testid="stAlert"] div,
div[data-testid="stAlert"] svg {
    color: #4ade80 !important;
    fill: #4ade80 !important;
}

[data-testid="stMetric"] {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 12px;
}

hr {
    border-color: #334155;
}
</style>
""", unsafe_allow_html=True)


# APP TITLE
st.title("🧮 SmartCalc Pro")
st.caption("Business & Scientific Calculator")
st.divider()


# SIDEBAR
st.sidebar.title("SMARTCALC PRO")

page = st.sidebar.radio(
    "Navigation",
    [
        "Basic Calculator",
        "Scientific Calculator",
        "Percentage Calculator",
        "Profit & Loss",
        "Simple Interest",
        "Compound Interest",
        "Unit Converter"
    ]
)


# HISTORY
if "history" not in st.session_state:
    st.session_state.history = []


# BASIC CALCULATOR
if page == "Basic Calculator":

    st.header("Basic Calculator")

    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("First Number", value=0.0)

    with col2:
        num2 = st.number_input("Second Number", value=0.0)

    operation = st.selectbox(
        "Choose Operation",
        ["Addition", "Subtraction", "Multiplication", "Division"]
    )

    if st.button("Calculate"):

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        else:
            result = None if num2 == 0 else num1 / num2

        if result is None:
            st.error("Cannot divide by zero!")
        else:
            st.success(f"Result: {result}")
            st.session_state.history.append(
                f"{num1} {operation} {num2} = {result}"
            )


# SCIENTIFIC CALCULATOR
elif page == "Scientific Calculator":

    st.header("Scientific Calculator")

    number = st.number_input("Enter Number", value=0.0)

    operation = st.selectbox(
        "Choose Operation",
        ["Square", "Square Root", "Sine", "Cosine"]
    )

    if st.button("Calculate"):

        if operation == "Square":
            result = number ** 2

        elif operation == "Square Root":
            if number < 0:
                st.error("Cannot calculate real square root of a negative number.")
                result = None
            else:
                result = math.sqrt(number)

        elif operation == "Sine":
            result = math.sin(math.radians(number))

        else:
            result = math.cos(math.radians(number))

        if result is not None:
            st.success(f"Result: {round(result, 4)}")
            st.session_state.history.append(
                f"{operation} of {number} = {result}"
            )


# PERCENTAGE CALCULATOR
elif page == "Percentage Calculator":

    st.header("Percentage Calculator")

    number = st.number_input("Enter Number", value=100.0)
    percentage = st.number_input("Enter Percentage", value=10.0)

    if st.button("Calculate Percentage"):

        result = number * percentage / 100

        st.success(f"Answer: {result}")

        st.session_state.history.append(
            f"{percentage}% of {number} = {result}"
        )


# PROFIT AND LOSS
elif page == "Profit & Loss":

    st.header("Profit & Loss Calculator")

    cost = st.number_input("Cost Price", min_value=0.0)
    selling = st.number_input("Selling Price", min_value=0.0)

    if st.button("Calculate"):

        if cost == 0:
            st.error("Cost price must be greater than zero.")

        elif selling > cost:
            profit = selling - cost
            percentage = profit / cost * 100

            st.success(f"Profit: {profit}")
            st.success(f"Profit Percentage: {percentage:.2f}%")

        elif selling < cost:
            loss = cost - selling
            percentage = loss / cost * 100

            st.success(f"Loss: {loss}")
            st.success(f"Loss Percentage: {percentage:.2f}%")

        else:
            st.success("No Profit, No Loss!")


# SIMPLE INTEREST
elif page == "Simple Interest":

    st.header("Simple Interest Calculator")

    principal = st.number_input("Principal Amount", min_value=0.0)
    rate = st.number_input("Annual Interest Rate (%)", min_value=0.0)
    time = st.number_input("Time in Years", min_value=0.0)

    if st.button("Calculate Interest"):

        interest = principal * rate * time / 100
        amount = principal + interest

        st.success(f"Simple Interest: {interest:.2f}")
        st.success(f"Total Amount: {amount:.2f}")


# COMPOUND INTEREST
elif page == "Compound Interest":

    st.header("Compound Interest Calculator")

    principal = st.number_input("Principal Amount", min_value=0.0)
    rate = st.number_input("Annual Interest Rate (%)", min_value=0.0)
    time = st.number_input("Time in Years", min_value=0.0)

    if st.button("Calculate Compound Interest"):

        amount = principal * (1 + rate / 100) ** time
        interest = amount - principal

        st.success(f"Compound Interest: {interest:.2f}")
        st.success(f"Final Amount: {amount:.2f}")


# UNIT CONVERTER
elif page == "Unit Converter":

    st.header("Unit Converter")

    conversion = st.selectbox(
        "Choose Conversion",
        [
            "Kilometres to Metres",
            "Metres to Kilometres",
            "Metres to Centimetres",
            "Centimetres to Metres",
            "Kilograms to Grams",
            "Grams to Kilograms",
            "Celsius to Fahrenheit",
            "Fahrenheit to Celsius"
        ]
    )

    value = st.number_input("Enter Value", value=0.0)

    if st.button("Convert"):

        if conversion == "Kilometres to Metres":
            result = value * 1000
        elif conversion == "Metres to Kilometres":
            result = value / 1000
        elif conversion == "Metres to Centimetres":
            result = value * 100
        elif conversion == "Centimetres to Metres":
            result = value / 100
        elif conversion == "Kilograms to Grams":
            result = value * 1000
        elif conversion == "Grams to Kilograms":
            result = value / 1000
        elif conversion == "Celsius to Fahrenheit":
            result = value * 9 / 5 + 32
        else:
            result = (value - 32) * 5 / 9

        st.success(f"Converted Value: {result:.2f}")


# CALCULATION HISTORY
st.sidebar.divider()
st.sidebar.subheader("Calculation History")

if st.session_state.history:

    for item in reversed(st.session_state.history[-10:]):
        st.sidebar.write("• " + item)

    if st.sidebar.button("Clear History"):
        st.session_state.history = []
        st.rerun()

else:
    st.sidebar.caption("No calculations yet.")
