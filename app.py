from pathlib import Path

import streamlit as st

from pages.about import render_about
from pages.dashboard import render_dashboard
from pages.scanner import render_scanner


BASE_DIR = Path(__file__).resolve().parent
SCAN_MODES = ["Original", "Grayscale", "High Contrast", "Black & White"]


def apply_theme() -> None:
    """Apply a modern SaaS-style theme to the Streamlit interface."""
    st.markdown(
        """
        <style>
            :root {
                --primary: #2563EB;
                --primary-dark: #1D4ED8;
                --background: #F8FAFC;
                --card: #FFFFFF;
                --text: #0F172A;
                --muted: #64748B;
                --border: #E2E8F0;
                --success: #16A34A;
                --danger: #DC2626;
                --radius: 15px;
            }

            .stApp {
                background: var(--background);
                color: var(--text);
            }

            [data-testid="stSidebar"] {
                background: linear-gradient(180deg, #0F172A 0%, #1E293B 100%);
                border-right: 1px solid rgba(255, 255, 255, 0.08);
            }

            [data-testid="stSidebar"] * {
                color: #F8FAFC;
            }

            [data-testid="stSidebar"] .stRadio label,
            [data-testid="stSidebar"] .stSlider label {
                color: #E2E8F0 !important;
                font-weight: 750;
            }

            .app-header {
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 18px;
                padding: 24px 28px;
                margin: -24px -16px 22px;
                background:
                    radial-gradient(circle at 12% 18%, rgba(37, 99, 235, 0.34), transparent 28%),
                    linear-gradient(100deg, #0F172A 0%, #1E3A8A 100%);
                color: white;
                border-radius: 0 0 24px 24px;
                box-shadow: 0 18px 44px rgba(15, 23, 42, 0.18);
            }

            .brand {
                display: flex;
                align-items: center;
                gap: 16px;
            }

            .brand-icon,
            .sidebar-logo {
                display: grid;
                place-items: center;
                border-radius: var(--radius);
                background: linear-gradient(135deg, #60A5FA 0%, var(--primary) 100%);
                color: white;
                box-shadow: 0 14px 30px rgba(37, 99, 235, 0.35);
            }

            .brand-icon {
                width: 56px;
                height: 56px;
                font-size: 29px;
            }

            .brand h1 {
                margin: 0;
                font-size: 29px;
                letter-spacing: 0;
                line-height: 1.12;
            }

            .brand p {
                margin: 6px 0 0;
                max-width: 760px;
                color: #DBEAFE;
                font-size: 15px;
            }

            .header-pill {
                border: 1px solid rgba(255, 255, 255, 0.22);
                border-radius: 999px;
                padding: 10px 14px;
                background: rgba(255, 255, 255, 0.1);
                color: #EFF6FF;
                font-weight: 800;
                white-space: nowrap;
            }

            .scanner-card,
            .stat-card {
                background: var(--card);
                border: 1px solid var(--border);
                border-radius: var(--radius);
                padding: 20px;
                box-shadow: 0 14px 34px rgba(15, 23, 42, 0.07);
                height: 100%;
            }

            .stat-label {
                color: var(--muted);
                font-size: 12px;
                font-weight: 800;
                text-transform: uppercase;
            }

            .stat-value {
                color: var(--text);
                font-size: 25px;
                font-weight: 900;
                margin-top: 8px;
                word-break: break-word;
            }

            .section-title {
                margin: 0 0 14px;
                color: var(--text);
                font-size: 17px;
                font-weight: 900;
            }

            .muted-copy {
                color: var(--muted);
                font-size: 14px;
                line-height: 1.7;
            }

            .sidebar-logo {
                width: 62px;
                height: 62px;
                font-size: 32px;
                margin-bottom: 12px;
            }

            .sidebar-heading {
                color: #93C5FD;
                font-weight: 900;
                margin-top: 20px;
                margin-bottom: 10px;
                text-transform: uppercase;
                font-size: 12px;
                letter-spacing: 0.04em;
            }

            .upload-box {
                border: 1.8px dashed #93C5FD;
                border-radius: var(--radius);
                padding: 20px;
                background: linear-gradient(180deg, #FFFFFF 0%, #EFF6FF 100%);
            }

            .tips-list,
            .feature-list {
                margin: 8px 0 0;
                padding-left: 0;
                list-style: none;
                color: #334155;
                font-size: 14px;
                line-height: 1.9;
            }

            .tips-list li::before,
            .feature-list li::before {
                content: "✓";
                color: var(--primary);
                font-weight: 900;
                margin-right: 10px;
            }

            div.stButton > button,
            div.stDownloadButton > button {
                border-radius: 12px;
                font-weight: 850;
                min-height: 45px;
                border: 1px solid #CBD5E1;
            }

            div.stButton > button[kind="primary"],
            div.stDownloadButton > button[kind="primary"] {
                background: linear-gradient(135deg, var(--primary), var(--primary-dark));
                color: white;
                border: 0;
            }

            [data-testid="stFileUploaderDropzone"] {
                border: 1.8px dashed #93C5FD;
                border-radius: var(--radius);
                background: #F8FBFF;
            }

            [data-testid="stFileUploaderDropzone"] button {
                border-radius: 12px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header() -> None:
    """Render the main header shared by all pages."""
    st.markdown(
        """
        <div class="app-header">
            <div class="brand">
                <div class="brand-icon">📄</div>
                <div>
                    <h1>Smart Document Scanner</h1>
                    <p>Aplikasi Pengolahan Citra Digital untuk mengubah foto dokumen menjadi hasil scan yang rapi, lurus, dan jelas.</p>
                </div>
            </div>
            <div class="header-pill">OpenCV + Streamlit</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar() -> str:
    """Render navigation and scanner settings in the sidebar."""
    with st.sidebar:
        st.markdown('<div class="sidebar-logo">🖨️</div>', unsafe_allow_html=True)
        st.markdown("### Smart Document Scanner")
        st.caption("Digital Image Processing Project")

        st.markdown('<div class="sidebar-heading">Menu</div>', unsafe_allow_html=True)
        page = st.radio(
            "Navigation",
            ["Dashboard", "Scanner", "About"],
            label_visibility="collapsed",
        )

        st.markdown('<div class="sidebar-heading">Pengaturan Scanner</div>', unsafe_allow_html=True)
        st.radio(
            "Scan Mode",
            SCAN_MODES,
            index=SCAN_MODES.index(st.session_state.get("scan_mode", "High Contrast")),
            key="scan_mode",
        )
        st.slider("Brightness", -100, 100, st.session_state.get("brightness", 10), key="brightness")
        st.slider("Contrast", 0.5, 3.0, st.session_state.get("contrast", 1.25), 0.05, key="contrast")
        st.slider("Edge Threshold", 25, 250, st.session_state.get("edge_threshold", 90), key="edge_threshold")

        if st.button("Reset Pengaturan", use_container_width=True):
            st.session_state.scan_mode = "High Contrast"
            st.session_state.brightness = 10
            st.session_state.contrast = 1.25
            st.session_state.edge_threshold = 90
            st.rerun()

    return page


def prepare_directories() -> None:
    """Create runtime folders needed for uploads and scan outputs."""
    (BASE_DIR / "assets").mkdir(exist_ok=True)
    (BASE_DIR / "uploads").mkdir(exist_ok=True)
    (BASE_DIR / "outputs").mkdir(exist_ok=True)


def main() -> None:
    """Initialize the Streamlit app and route the selected page."""
    st.set_page_config(
        page_title="Smart Document Scanner",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    prepare_directories()
    apply_theme()
    render_header()

    page = render_sidebar()
    if page == "Dashboard":
        render_dashboard(BASE_DIR)
    elif page == "Scanner":
        render_scanner(BASE_DIR)
    else:
        render_about(BASE_DIR)


if __name__ == "__main__":
    main()
