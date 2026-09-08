import requests
import streamlit as st


st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)


API_URL = "http://127.0.0.1:8000/predict"


st.markdown(
    """
    <style>
        .main {
            padding-top: 2rem;
        }

        .title {
            text-align: center;
            font-size: 42px;
            font-weight: 700;
        }

        .subtitle {
            text-align: center;
            font-size: 18px;
            margin-bottom: 30px;
        }

        .price {
            text-align: center;
            font-size: 36px;
            font-weight: 700;
            padding: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    '<div class="title">Car Price Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Enter the car details and get an estimated selling price.</div>',
    unsafe_allow_html=True
)


with st.form("car_prediction_form"):

    st.subheader("Car Information")

    col1, col2 = st.columns(2)

    with col1:

        car_name = st.text_input(
            "Car Name",
            placeholder="e.g. swift"
        )

        year = st.number_input(
            "Year",
            min_value=1990,
            max_value=2026,
            value=2018,
            step=1
        )

        present_price = st.number_input(
            "Present Price (Lakhs)",
            min_value=0.0,
            value=5.0,
            step=0.1
        )

        kms_driven = st.number_input(
            "Kilometers Driven",
            min_value=0.0,
            value=50000.0,
            step=1000.0
        )

    with col2:

        fuel_type = st.selectbox(
            "Fuel Type",
            ["Petrol", "Diesel", "CNG"]
        )

        seller_type = st.selectbox(
            "Seller Type",
            ["Dealer", "Individual"]
        )

        transmission = st.selectbox(
            "Transmission",
            ["Manual", "Automatic"]
        )

        owner = st.number_input(
            "Number of Owners",
            min_value=0,
            max_value=10,
            value=0,
            step=1
        )

    submitted = st.form_submit_button(
        "Predict Price",
        use_container_width=True
    )


if submitted:

    if not car_name.strip():
        st.error("Please enter the car name.")
        st.stop()

    payload = {
        "Car_Name": car_name.strip(),
        "Year": int(year),
        "Present_Price": float(present_price),
        "Kms_Driven": float(kms_driven),
        "Fuel_Type": fuel_type,
        "Seller_Type": seller_type,
        "Transmission": transmission,
        "Owner": int(owner)
    }

    try:

        with st.spinner("Predicting car price..."):

            response = requests.post(
                API_URL,
                json=payload,
                timeout=10
            )

        if response.status_code == 200:

            result = response.json()

            predicted_price_lakhs = float(
                result["prediction_price"]
            )

            predicted_price_pkr = (
                predicted_price_lakhs * 100000
            )

            st.success(
                "Prediction completed successfully."
            )

            st.markdown(
                f"""
                <div class="price">
                    Estimated Selling Price<br>
                    Rs. {predicted_price_pkr:,.0f}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.info(
                f"Estimated Price: "
                f"{predicted_price_lakhs:.2f} Lakhs"
            )

        else:

            st.error(
                f"API Error ({response.status_code}): "
                f"{response.text}"
            )

    except requests.exceptions.ConnectionError:

        st.error(
            "Could not connect to the FastAPI server. "
            "Make sure FastAPI is running on http://127.0.0.1:8000"
        )

    except requests.exceptions.Timeout:

        st.error(
            "The API took too long to respond."
        )

    except Exception as e:

        st.error(
            f"Something went wrong: {str(e)}"
        )