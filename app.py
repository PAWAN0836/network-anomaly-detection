import streamlit as st
import numpy as np
import pickle

# ================================
# LOAD MODEL
# ================================
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ================================
# PAGE CONFIG
# ================================
st.set_page_config(page_title="Anomaly Detection", layout="wide")

# ================================
# CUSTOM STYLE (COOL UI)
# ================================
st.markdown("""
<style>
.main {
    background-color: #0e1117;
    color: white;
}
h1 {
    color: #00ffd5;
    text-align: center;
}
.block-container {
    padding: 2rem;
}
</style>
""", unsafe_allow_html=True)

# ================================
# TITLE
# ================================
st.title("🔍 Network Anomaly Detection System")

st.markdown("""
<div style="text-align:center; font-size:18px;">
Detect whether network traffic is <b>Normal</b> or an <b>Attack</b> using Machine Learning.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ================================
# FEATURE GROUPS
# ================================
basic_features = [
    "duration",
    "protocol_type (0=tcp,1=udp,2=icmp)",
    "service",
    "flag",
    "src_bytes",
    "dst_bytes"
]

content_features = [
    "land", "wrong_fragment", "urgent", "hot",
    "num_failed_logins", "logged_in", "num_compromised",
    "root_shell", "su_attempted", "num_root"
]

traffic_features = [
    "count", "srv_count", "serror_rate", "srv_serror_rate",
    "rerror_rate", "srv_rerror_rate", "same_srv_rate",
    "diff_srv_rate", "srv_diff_host_rate"
]

host_features = [
    "dst_host_count", "dst_host_srv_count",
    "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate", "dst_host_srv_serror_rate",
    "dst_host_rerror_rate", "dst_host_srv_rerror_rate"
]

# ================================
# INPUT UI
# ================================
inputs = []

def create_section(title, features):
    st.subheader(title)
    cols = st.columns(2)
    for i, f in enumerate(features):
        val = cols[i % 2].number_input(f, value=0.0)
        inputs.append(val)

create_section("📊 Basic Features", basic_features)
create_section("🧠 Content Features", content_features)
create_section("📡 Traffic Features", traffic_features)
create_section("🌐 Host Features", host_features)

st.markdown("---")

# ================================
# PREDICTION BUTTON
# ================================
if st.button("🚀 Predict", use_container_width=True):

    try:
        data = np.array(inputs).reshape(1, -1)
        data = scaler.transform(data)

        prediction = model.predict(data)

        st.markdown("## 🔎 Result")

        if prediction[0] == 1:
            st.markdown(
                "<div style='background-color:#ff4b4b;padding:20px;border-radius:10px;'>"
                "<h3 style='color:white;'>🚨 Attack Detected!</h3>"
                "<p style='color:white;'>Suspicious network activity found.</p>"
                "</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<div style='background-color:#00c853;padding:20px;border-radius:10px;'>"
                "<h3 style='color:white;'>✅ Normal Traffic</h3>"
                "<p style='color:white;'>No threat detected.</p>"
                "</div>",
                unsafe_allow_html=True
            )

    except Exception as e:
        st.warning("⚠️ Error occurred")
        st.write(e)

# ================================
# FOOTER
# ================================
st.markdown("---")
st.caption("🚀 Built with Machine Learning & Streamlit")

st.markdown("""
<div style='text-align:center; font-size:16px; color:gray;'>
Developed by <b>Bairi Paawan Kumar</b>
</div>
""", unsafe_allow_html=True)