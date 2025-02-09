import streamlit as st
from web3 import Web3
import backend  # Import backend functions

# Set Page Config
st.set_page_config(page_title="Blockchain Land Registry", page_icon="🏡", layout="wide")

# Custom CSS for Styling
st.markdown(
    """
    <style>
        .stButton button {
            border-radius: 12px;
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px 24px;
        }
        .stTextInput, .stNumberInput, .stSelectbox {
            border-radius: 10px;
            border: 1px solid #ccc;
            padding: 8px;
        }
        .stTitle {
            color: #2E86C1;
            text-align: center;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Connect to Ethereum (Ganache)
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Ensure Web3 connection
if not web3.is_connected():
    st.error("🚨 Web3 is not connected. Ensure Ganache is running.")
    st.stop()

# Streamlit UI
st.markdown("<h1 class='stTitle'>🏡 Blockchain Land Registry</h1>", unsafe_allow_html=True)

# Select Ethereum account
accounts = web3.eth.accounts
if not accounts:
    st.error("❌ No Ethereum accounts found! Ensure Ganache is running.")
    st.stop()
else:
    selected_account = st.sidebar.selectbox("🔹 Select Your Ethereum Account", accounts)

# UI Layout with Columns
col1, col2 = st.columns(2)

# 🌍 Register New Land
with col1:
    st.subheader("📝 Register New Land")
    land_id = st.number_input("🔢 Land ID", min_value=1, step=1, key="register_id")
    location = st.text_input("📍 Land Location", key="register_location")
    area = st.number_input("📏 Area (sq. meters)", min_value=1, step=1, key="register_area")

    if st.button("✅ Register Land"):
        result = backend.register_land(selected_account, land_id, location, area)
        if "Error" in result:
            st.error(f"❌ {result}")
        else:
            st.success(f"🎉 {result}")

# 🔄 Transfer Ownership
with col2:
    st.subheader("🔄 Transfer Ownership")
    land_id_transfer = st.number_input("🔢 Land ID to Transfer", min_value=1, step=1, key="transfer_id")
    new_owner = st.selectbox("👤 Select New Owner", accounts, key="new_owner")

    if st.button("🔁 Transfer Ownership"):
        result = backend.transfer_ownership(selected_account, land_id_transfer, new_owner)
        if "Error" in result:
            st.error(f"❌ {result}")
        else:
            st.success(f"✅ {result}")

# 📊 View Land Details
st.subheader("📜 View Land Details")
land_id_view = st.number_input("🔎 Enter Land ID to View", min_value=1, step=1, key="view_id")

if st.button("🔍 Fetch Details"):
    details = backend.get_land_details(land_id_view)
    if "Error" in details:
        st.error(f"❌ {details['Error']}")
    elif details["Registered"]:
        st.markdown(f"""
        ✅ **Land Details**  
        - **Land ID:** {details['ID']}  
        - **Location:** 📍 {details['Location']}  
        - **Area:** 📏 {details['Area']} sqm  
        - **Owner:** 👤 {details['Owner']}  
        """)
    else:
        st.warning("⚠️ Land not registered.")

# Sidebar Info
st.sidebar.info("🔗 Connected to Ethereum Blockchain (Ganache)")

# Future Scope: Add Transaction History Here in the Sidebar
st.sidebar.subheader("📜 Transaction History (Coming Soon...)")
