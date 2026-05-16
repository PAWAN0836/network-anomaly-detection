import streamlit as st
import numpy as np
import pickle

# ============================================================
# LOAD MODEL & SCALER
# ============================================================
@st.cache_resource
def load_model():
    try:
        model  = pickle.load(open("model.pkl", "rb"))
        scaler = pickle.load(open("scaler.pkl", "rb"))
        return model, scaler
    except FileNotFoundError as e:
        st.error(f"Model file not found: {e}. Make sure model.pkl and scaler.pkl are present.")
        st.stop()

model, scaler = load_model()

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(page_title="Network Anomaly Detection", layout="wide")

st.markdown("""
<style>
h1 { color: #00ffd5; text-align: center; }
.block-container { padding: 2rem; }
</style>
""", unsafe_allow_html=True)

# ============================================================
# TITLE
# ============================================================
st.title("🔍 Network Anomaly Detection System")
st.markdown("""
<div style="text-align:center; font-size:18px;">
Detect whether network traffic is <b>Normal</b> or an <b>Attack</b> using Machine Learning.
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# ============================================================
# ALL 41 NSL-KDD FEATURES
# Each entry: (display_label, unique_key)
# ============================================================
basic_features = [
    ("duration",                        "feat_duration"),
    ("protocol_type (0=tcp,1=udp,2=icmp)", "feat_protocol_type"),
    ("service",                         "feat_service"),
    ("flag",                            "feat_flag"),
    ("src_bytes",                       "feat_src_bytes"),
    ("dst_bytes",                       "feat_dst_bytes"),
]

content_features = [
    ("land",               "feat_land"),
    ("wrong_fragment",     "feat_wrong_fragment"),
    ("urgent",             "feat_urgent"),
    ("hot",                "feat_hot"),
    ("num_failed_logins",  "feat_num_failed_logins"),
    ("logged_in",          "feat_logged_in"),
    ("num_compromised",    "feat_num_compromised"),
    ("root_shell",         "feat_root_shell"),
    ("su_attempted",       "feat_su_attempted"),
    ("num_root",           "feat_num_root"),
    ("num_file_creations", "feat_num_file_creations"),
    ("num_shells",         "feat_num_shells"),
    ("num_access_files",   "feat_num_access_files"),
    ("num_outbound_cmds",  "feat_num_outbound_cmds"),
    ("is_host_login",      "feat_is_host_login"),
    ("is_guest_login",     "feat_is_guest_login"),
]

traffic_features = [
    ("count",             "feat_count"),
    ("srv_count",         "feat_srv_count"),
    ("serror_rate",       "feat_serror_rate"),
    ("srv_serror_rate",   "feat_srv_serror_rate"),
    ("rerror_rate",       "feat_rerror_rate"),
    ("srv_rerror_rate",   "feat_srv_rerror_rate"),
    ("same_srv_rate",     "feat_same_srv_rate"),
    ("diff_srv_rate",     "feat_diff_srv_rate"),
    ("srv_diff_host_rate","feat_srv_diff_host_rate"),
]

host_features = [
    ("dst_host_count",              "feat_dst_host_count"),
    ("dst_host_srv_count",          "feat_dst_host_srv_count"),
    ("dst_host_same_srv_rate",      "feat_dst_host_same_srv_rate"),
    ("dst_host_diff_srv_rate",      "feat_dst_host_diff_srv_rate"),
    ("dst_host_same_src_port_rate", "feat_dst_host_same_src_port_rate"),
    ("dst_host_srv_diff_host_rate", "feat_dst_host_srv_diff_host_rate"),
    ("dst_host_serror_rate",        "feat_dst_host_serror_rate"),
    ("dst_host_srv_serror_rate",    "feat_dst_host_srv_serror_rate"),
    ("dst_host_rerror_rate",        "feat_dst_host_rerror_rate"),
    ("dst_host_srv_rerror_rate",    "feat_dst_host_srv_rerror_rate"),
]

# ============================================================
# INPUT UI — read from st.session_state, NOT an appended list
# ============================================================
def create_section(title, features):
    st.subheader(title)
    cols = st.columns(2)
    for i, (label, key) in enumerate(features):
        cols[i % 2].number_input(label, value=0.0, key=key)

create_section("📊 Basic Features",   basic_features)
create_section("🧠 Content Features", content_features)
create_section("📡 Traffic Features", traffic_features)
create_section("🌐 Host Features",    host_features)

st.markdown("---")

# ============================================================
# PREDICTION — collect values fresh from session_state
# ============================================================
all_features = basic_features + content_features + traffic_features + host_features

if st.button("🚀 Predict", use_container_width=True):
    try:
        # Read current values directly from session_state using unique keys
        inputs = [st.session_state[key] for _, key in all_features]

        if len(inputs) != 41:
            st.error(f"Expected 41 features, got {len(inputs)}.")
        else:
            data       = np.array(inputs).reshape(1, -1)
            data       = scaler.transform(data)
            prediction = model.predict(data)

            st.markdown("## 🔎 Result")

            if prediction[0] == 1:
                st.markdown(
                    "<div style='background-color:#ff4b4b;padding:20px;border-radius:10px;'>"
                    "<h3 style='color:white;'>🚨 Attack Detected!</h3>"
                    "<p style='color:white;'>Suspicious network activity found.</p>"
                    "</div>", unsafe_allow_html=True
                )
            else:
                st.markdown(
                    "<div style='background-color:#00c853;padding:20px;border-radius:10px;'>"
                    "<h3 style='color:white;'>✅ Normal Traffic</h3>"
                    "<p style='color:white;'>No threat detected.</p>"
                    "</div>", unsafe_allow_html=True
                )
    except Exception as e:
        st.warning("⚠️ Prediction error occurred.")
        st.write(str(e))

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.caption("Built with Machine Learning & Streamlit | NSL-KDD Dataset")
st.markdown(
    "<div style='text-align:center;font-size:16px;color:gray;'>"
    "Developed by <b>Bairi Pawan Kumar</b></div>",
    unsafe_allow_html=True
)
