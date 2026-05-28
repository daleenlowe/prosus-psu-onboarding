"""
Prosus PSU Board Onboarding Dashboard
Streamlit app with bcrypt authentication — ready for Streamlit Community Cloud deployment
"""

import bcrypt
import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth

# ---------------------------------------------------------------------------
# Authentication setup — generate hash at import time
# ---------------------------------------------------------------------------
_raw_password = "Prosus2026!"
_hashed = bcrypt.hashpw(_raw_password.encode(), bcrypt.gensalt()).decode()

credentials = {
    "usernames": {
        "board_member": {
            "name": "Board Member",
            "password": _hashed,
        }
    }
}

authenticator = stauth.Authenticate(
    credentials,
    "psu_onboarding",
    "prosus_psu_secret_2026",
    1,
)

# ---------------------------------------------------------------------------
# Page config — must be FIRST Streamlit call
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Prosus | PSU Board Onboarding",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------
CSS = """
/* Hide Streamlit default menu/footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Header bar */
.prosus-header {
    background-color: #081A54;
    color: white;
    padding: 14px 24px;
    font-family: Verdana, sans-serif;
    font-size: 18px;
    font-weight: bold;
    border-bottom: 3px solid #00D3AF;
    margin-bottom: 0;
}
.prosus-header-right {
    float: right;
    font-size: 12px;
    color: #00D3AF;
    font-weight: normal;
    margin-top: 4px;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #081A54 !important;
}
[data-testid="stSidebar"] * {
    color: white !important;
}

/* Card styling */
.info-card {
    background: white;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    height: 100%;
}
.card-teal { border-top: 4px solid #00D3AF; }
.card-blue { border-top: 4px solid #0332AF; }

/* Callout boxes */
.callout-blue {
    background: #E8F0FE;
    border-left: 4px solid #0332AF;
    padding: 12px 16px;
    border-radius: 4px;
    margin: 12px 0;
    font-size: 13px;
}
.callout-yellow {
    background: #FFF9E6;
    border-left: 4px solid #FCDA28;
    padding: 12px 16px;
    border-radius: 4px;
    margin: 12px 0;
    font-size: 13px;
}
.callout-red {
    background: #FFF0F0;
    border-left: 4px solid #D90276;
    padding: 12px 16px;
    border-radius: 4px;
    margin: 12px 0;
    font-size: 13px;
}
.callout-grey {
    background: #F4F5F7;
    border-left: 4px solid #808080;
    padding: 12px 16px;
    border-radius: 4px;
    margin: 12px 0;
    font-size: 13px;
}

/* Phase badges */
.badge-yellow { background:#FCDA28; color:#081A54; padding:2px 10px; border-radius:12px; font-size:11px; font-weight:bold; }
.badge-teal   { background:#00D3AF; color:#081A54; padding:2px 10px; border-radius:12px; font-size:11px; font-weight:bold; }
.badge-blue   { background:#0332AF; color:white;   padding:2px 10px; border-radius:12px; font-size:11px; font-weight:bold; }
.badge-green  { background:#00A67E; color:white;   padding:2px 10px; border-radius:12px; font-size:11px; font-weight:bold; }

/* Company chips */
.chip { display:inline-block; background:#E8EEFF; color:#0332AF; border-radius:12px; padding:2px 10px; font-size:12px; margin:2px 3px; }
.chip-teal { background:#E0FAF5; color:#006B57; }
.chip-new  { background:#00D3AF; color:#081A54; font-weight:bold; }

/* Step circles */
.step-circle {
    display: inline-flex; align-items: center; justify-content: center;
    width: 36px; height: 36px; border-radius: 50%;
    background: #0332AF; color: white;
    font-weight: bold; font-size: 16px; margin-right: 10px;
}

/* Table styling */
.styled-table { width:100%; border-collapse:collapse; font-size:13px; }
.styled-table th { background:#081A54; color:white; padding:8px 12px; text-align:left; }
.styled-table td { padding:7px 12px; border-bottom:1px solid #E8E8E8; }
.styled-table tr:nth-child(even) { background:#F4F5F7; }
.styled-table tr:hover { background:#E8EEFF; }
"""


# ---------------------------------------------------------------------------
# Section: What are PSUs?
# ---------------------------------------------------------------------------
def show_what_are_psus():
    st.markdown("# What are PSUs?")
    st.caption("A primer for new board members")
    st.markdown("")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div class="info-card card-teal">
            <h3 style="color:#00D3AF">What is a PSU?</h3>
            <ul>
            <li>A <strong>Performance Share Unit (PSU)</strong> is a conditional right to receive Prosus
            or Naspers Class N ordinary shares</li>
            <li>Units only convert to actual shares if <strong>two conditions</strong> are both met:
            (1) a multi-year performance condition is achieved, and (2) the executive remains
            employed until the vesting date</li>
            <li>The number of shares received depends on where the Group ranks against a defined peer
            group — outperforming peers earns more shares; underperforming means nothing vests</li>
            <li>The fair value is set at grant date and is <strong>not a guaranteed floor</strong> —
            actual value at vesting depends on shares earned × share price at that time</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="info-card card-blue">
            <h3 style="color:#0332AF">Why does Prosus use PSUs?</h3>
            <ul>
            <li><strong>Align</strong> executive reward with sustained, long-term shareholder
            value creation</li>
            <li><strong>Reward genuine outperformance</strong> — the Group must rank above the peer
            group threshold for any shares to vest</li>
            <li><strong>Discourage short-termism</strong> — cliff vesting over 3–4 years with no
            interim liquidity</li>
            <li><strong>Protect shareholders</strong> — the absolute underpin (Phase 3) means awards
            lapse entirely if Group TSR is negative</li>
            <li><strong>Accountability</strong> — malus and clawback provisions apply for serious
            misconduct</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        '<div class="callout-blue">PSU awards are personal and non-transferable. They do not form '
        "part of the recipient's employment contract. RemCo (the Human Resources &amp; "
        "Remuneration Committee) has full discretion over the administration and determination "
        "of awards.</div>",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Section: Types of PSUs
# ---------------------------------------------------------------------------
def show_types_of_psus():
    st.markdown("# Types of PSUs")
    st.markdown(
        "Prosus has operated three successive phases of PSU design, each reflecting the "
        "Group's evolving strategy and listing structure."
    )
    st.markdown("")

    # Phase 1
    with st.expander("📊 Phase 1 — Ecommerce CAGR (Naspers)  |  Pre-Prosus listing · FY20–FY22"):
        phase1_data = {
            "Design element": [
                "Plan",
                "Settlement",
                "Performance measure",
                "Measurement period",
                "Vesting",
                "Threshold",
                "Target",
                "Maximum",
                "Absolute underpin",
                "Malus",
                "Clawback",
                "Recipients",
            ],
            "Detail": [
                "Naspers Restricted Stock Plan Trust",
                "Naspers Class N ordinary shares",
                "3-year CAGR of the Naspers Global Ecommerce SAR valuation "
                "(group assets excluding Tencent) compared against a peer group",
                "3 years",
                "100% cliff vest on the 3rd anniversary of grant date",
                "25th percentile → 50% of PSUs vest",
                "50th percentile → 100% of PSUs vest",
                "75th percentile → 200% of PSUs vest (capped)",
                "None",
                "Not applicable",
                "2 years post-vest",
                "All eligible executives",
            ],
        }
        df1 = pd.DataFrame(phase1_data)
        st.dataframe(df1, hide_index=True, use_container_width=True)
        st.markdown(
            '<div class="callout-blue">The Ecommerce measure captured the performance of '
            "Naspers's portfolio companies (excluding Tencent). This was an internal CAGR "
            "measure, not a direct market TSR.</div>",
            unsafe_allow_html=True,
        )

    # Phase 2
    with st.expander(
        "📊 Phase 2 — Ecommerce CAGR (Prosus)  |  Post-Prosus listing · FY22–FY24"
    ):
        phase2_data = {
            "Design element": [
                "Plan",
                "Settlement",
                "Performance measure",
                "Measurement period",
                "Vesting",
                "Threshold",
                "Target",
                "Maximum",
                "Absolute underpin",
                "Malus",
                "Clawback",
                "Recipients",
            ],
            "Detail": [
                "Naspers RSP Trust / Prosus Share Award Plan (dual-listed)",
                "Naspers Class N ordinary shares OR Prosus ordinary shares",
                "3-year CAGR of the Ecommerce SAR valuation of the combined "
                "Naspers + Prosus group compared against an expanded peer group",
                "3 years",
                "100% cliff vest on the 3rd anniversary of grant date",
                "25th percentile → 50% of PSUs vest",
                "50th percentile → 100% of PSUs vest",
                "75th percentile → 200% of PSUs vest (capped)",
                "None",
                "Introduced — formal malus provisions added",
                "2 years post-vest",
                "All eligible executives",
            ],
        }
        df2 = pd.DataFrame(phase2_data)
        st.dataframe(df2, hide_index=True, use_container_width=True)
        st.markdown(
            '<div class="callout-blue">Following the September 2019 Prosus listing on Euronext '
            "Amsterdam, Phase 2 introduced dual-settlement (Naspers or Prosus shares) and an "
            "expanded peer group to include Prosus-listed comparable companies. Formal malus "
            "provisions were also introduced in this phase.</div>",
            unsafe_allow_html=True,
        )

    # Phase 3 — expanded=True
    with st.expander(
        "📊 Phase 3 — Group TSR  |  FY25 onwards  ⭐ CURRENT", expanded=True
    ):
        phase3_data = {
            "Design element": [
                "Plan",
                "Settlement",
                "Performance measure",
                "Measurement period",
                "Vesting",
                "Threshold",
                "Target",
                "Maximum",
                "Absolute underpin",
                "Malus",
                "Clawback",
                "Recipients",
            ],
            "Detail": [
                "Naspers RSP Trust / Prosus Share Award Plan",
                "Naspers Class N ordinary shares OR Prosus ordinary shares",
                "Group TSR (Total Shareholder Return) of the combined Naspers + Prosus group "
                "vs an expanded peer group of ~49 global tech/internet companies",
                "4 years (extended from 3 years in Phase 1 & 2)",
                "100% cliff vest on the 4th anniversary of grant date",
                "30th percentile → 50% of PSUs vest (raised from 25th in Phases 1 & 2)",
                "50th percentile → 100% of PSUs vest",
                "75th percentile → 200% of PSUs vest (capped)",
                "New: Award lapses entirely if Group TSR is negative over the period",
                "Yes — applicable from grant date",
                "2 years post-vest",
                "CEO (FY25); CFO (FY26+)",
            ],
        }
        df3 = pd.DataFrame(phase3_data)
        st.dataframe(df3, hide_index=True, use_container_width=True)
        st.markdown(
            '<div class="callout-yellow">Three significant changes from Phase 1 &amp; 2: '
            "(1) Measure shifted from Ecommerce CAGR to <strong>Group TSR</strong> — now "
            "includes Tencent; (2) Vesting extended from <strong>3 to 4 years</strong>; "
            "(3) New <strong>absolute underpin</strong> — award lapses if Group TSR is "
            "negative.</div>",
            unsafe_allow_html=True,
        )


# ---------------------------------------------------------------------------
# Section: How performance is measured
# ---------------------------------------------------------------------------
def show_how_performance_measured():
    st.markdown("# How performance is measured")
    st.markdown(
        "PSU vesting is determined in three sequential steps, described below. "
        "The process is the same for both Naspers RSP Trust awards and Prosus SAP awards."
    )
    st.markdown("")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div class="info-card">
            <div class="step-circle">1</div><strong>Grant</strong><br><br>
            A fixed number of conditional PSUs is awarded at a stated fair value.
            The fair value is <em>not</em> a guaranteed outcome — actual value depends on
            PSUs earned × share price at vesting. Grants are approved by RemCo and disclosed
            in the Remuneration Report.
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="info-card">
            <div class="step-circle">2</div><strong>Measurement</strong><br><br>
            Group TSR (or Ecommerce CAGR for older awards) is calculated over the full
            performance period. Peer TSRs use <strong>31-day trailing VWAP</strong> at start
            and end — this smooths short-term price volatility. The Group ranks as a single
            entity (Naspers + Prosus combined). A third-party data provider confirms all TSR
            calculations.
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """
            <div class="info-card">
            <div class="step-circle">3</div><strong>Ranking &amp; Vesting</strong><br><br>
            Ranking vs the peer group determines the vesting percentage, applied linearly
            between threshold, target and maximum. RemCo makes the final determination —
            typically at the June RemCo meeting after the measurement period ends. No partial
            vesting is possible below the threshold.
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Vesting payout schedule")

    vesting_data = {
        "Percentile rank vs peers": [
            "Below 25th percentile",
            "25th–29th percentile",
            "30th percentile (Phase 3 threshold)",
            "30th–49th percentile",
            "50th percentile — Target",
            "50th–74th percentile",
            "75th percentile — Maximum",
            "Above 75th percentile",
            "⚠ Absolute underpin (Phase 3 only)",
        ],
        "Phase 1 & 2 vest %": [
            "0%",
            "50%–~74%",
            "~75%",
            "Linear 50%→100%",
            "100%",
            "Linear 100%→200%",
            "200%",
            "200%",
            "None",
        ],
        "Phase 3 vest %": [
            "—",
            "0%",
            "50%",
            "Linear 50%→100%",
            "100%",
            "Linear 100%→200%",
            "200%",
            "200%",
            "Lapses if Group TSR < 0%",
        ],
        "Notes": [
            "Nothing vests — below Phase 1 & 2 threshold",
            "Phase 3 threshold higher at 30th percentile",
            "Phase 3 minimum vesting point",
            "Linear interpolation between threshold and target",
            "On-plan / target outcome",
            "Linear interpolation between target and maximum",
            "Cap — no further upside",
            "Capped at maximum",
            "Phase 3: negative TSR = full forfeiture regardless of ranking",
        ],
    }
    df_vest = pd.DataFrame(vesting_data)
    st.dataframe(df_vest, hide_index=True, use_container_width=True, height=370)

    st.markdown(
        '<div class="callout-blue">RemCo makes the final determination — typically at the '
        "June RemCo meeting after the measurement period ends.</div>",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Section: Eligibility & current awards
# ---------------------------------------------------------------------------
def show_eligibility():
    st.markdown("# Eligibility & current awards")
    st.markdown(
        "Eligibility for PSU awards is determined by RemCo and disclosed in the annual "
        "Remuneration Report. Awards are personal and non-transferable."
    )
    st.markdown("")

    with st.expander("👤 Who is eligible?", expanded=True):
        st.markdown(
            """
            **Phase 1 & 2 (FY20–FY24):** All eligible executives received PSU awards.

            **Phase 3 — FY25:** CEO and other designated executives received awards.

            **Phase 3 — FY26 onwards:** Only the **CFO** — a combination of Naspers TSR PSUs
            and Prosus TSR PSUs. The CEO (Fabricio Bloisi) participates via a separate
            long-term incentive structure approved by RemCo.

            RemCo reviews eligibility annually and may add or remove participants at its discretion.
            """
        )

    with st.expander("📋 FY25 awards — currently in flight", expanded=True):
        awards_data = {
            "Recipient": ["Fabricio Bloisi (CEO)", "Fabricio Bloisi (CEO)", "CFO"],
            "Plan": [
                "Naspers RSP Trust",
                "Prosus Share Award Plan",
                "Naspers RSP Trust + Prosus SAP",
            ],
            "Grant date": ["1 July 2024", "1 July 2024", "FY26"],
            "PSUs granted": ["32,662", "430,295", "See award letter"],
            "Grant fair value": ["US$8.1m", "US$18.9m", "Confidential"],
            "Measurement period": [
                "1 Jul 2024 – 30 Jun 2028",
                "1 Jul 2024 – 30 Jun 2028",
                "FY26 period",
            ],
        }
        df_awards = pd.DataFrame(awards_data)
        st.dataframe(df_awards, hide_index=True, use_container_width=True)
        st.markdown(
            '<div class="callout-yellow"><strong>Market shock protection:</strong> If the peer '
            "group average TSR is ≤ −10% over the measurement period, the measurement period "
            "extends by one year (to 30 June 2029 for FY25 awards). This protects against "
            "broad market downturns distorting the relative ranking.</div>",
            unsafe_allow_html=True,
        )

    with st.expander(
        "📁 Historical reference awards (Ecommerce CAGR phase)", expanded=False
    ):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                <div class="info-card card-blue">
                <h4 style="color:#0332AF">David Tudor — Naspers RSP Trust</h4>
                <ul>
                <li><strong>Grant date:</strong> FY22</li>
                <li><strong>Plan:</strong> Naspers RSP Trust</li>
                <li><strong>Measure:</strong> Ecommerce CAGR vs peer group</li>
                <li><strong>Vesting:</strong> 3-year cliff vest</li>
                <li><strong>Status:</strong> Vested / lapsed per RemCo determination</li>
                </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(
                """
                <div class="info-card card-teal">
                <h4 style="color:#00D3AF">David Tudor — Prosus SAP</h4>
                <ul>
                <li><strong>Grant date:</strong> FY22</li>
                <li><strong>Plan:</strong> Prosus Share Award Plan</li>
                <li><strong>Measure:</strong> Ecommerce CAGR vs peer group</li>
                <li><strong>Vesting:</strong> 3-year cliff vest</li>
                <li><strong>Status:</strong> Vested / lapsed per RemCo determination</li>
                </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.markdown(
            '<div class="callout-grey">Historical vesting outcomes are reported in the '
            "Prosus Annual Report and Remuneration Report, available at "
            "prosus.com/investors.</div>",
            unsafe_allow_html=True,
        )


# ---------------------------------------------------------------------------
# Section: Peer group
# ---------------------------------------------------------------------------
def show_peer_group():
    st.markdown("# Peer group")
    st.markdown(
        "The peer group is the benchmark against which Prosus's TSR (or Ecommerce CAGR) "
        "is ranked. The composition of the peer group directly determines how many shares vest."
    )
    st.markdown("")

    with st.expander("⚖️ Governance rules", expanded=True):
        st.markdown(
            """
            1. **Approved by RemCo** at the start of each measurement period — not changed mid-cycle
            2. **Global technology and internet companies** with broadly comparable business models
            3. **Minimum market capitalisation** threshold applies (typically US$5bn+)
            4. **Delisted or acquired companies** are removed; a replacement may be added at RemCo discretion
            5. **No Prosus/Naspers cross-holding** — companies with significant Prosus/Naspers holdings are excluded
            6. **Survivorship rule** — if a peer is acquired during the period, it is treated as if it ranked at the 75th percentile at time of acquisition
            7. **TSR calculation** uses 31-day trailing VWAP at start and end of the measurement period, in USD
            """
        )

    with st.expander("📊 Phase 1 peers — ~21 companies (FY20–FY22)", expanded=False):
        st.caption("Naspers Ecommerce CAGR benchmark group")
        companies_p1 = [
            "Adyen", "Alphabet", "Amazon", "Booking Holdings", "Delivery Hero",
            "eBay", "Expedia", "Facebook (Meta)", "Flipkart", "JD.com",
            "MercadoLibre", "Netflix", "OLX", "PayPal", "Rakuten",
            "Sea Limited", "Shopify", "Spotify", "Tencent", "Trip.com",
            "Zalando",
        ]
        chips_html = " ".join(f'<span class="chip">{c}</span>' for c in companies_p1)
        st.markdown(chips_html, unsafe_allow_html=True)

    with st.expander("📊 Phase 2 peers — ~23 companies (FY22–FY24)", expanded=False):
        st.caption(
            "Prosus Ecommerce CAGR benchmark group. "
            '<span class="chip-new" style="background:#00D3AF;color:#081A54;padding:2px 8px;border-radius:10px;font-size:11px;font-weight:bold;">NEW</span> = added vs Phase 1',
            unsafe_allow_html=True,
        )
        existing_p2 = [
            "Adyen", "Alphabet", "Amazon", "Booking Holdings",
            "eBay", "Expedia", "Facebook (Meta)", "JD.com",
            "MercadoLibre", "Netflix", "PayPal", "Rakuten",
            "Sea Limited", "Shopify", "Spotify", "Tencent",
            "Trip.com", "Zalando",
        ]
        new_p2 = ["Adevinta", "Deliveroo", "DoorDash", "Just Eat Takeaway", "Square (Block)"]
        existing_chips = " ".join(f'<span class="chip">{c}</span>' for c in existing_p2)
        new_chips = " ".join(f'<span class="chip chip-new">{c} ✦</span>' for c in new_p2)
        st.markdown(existing_chips + " " + new_chips, unsafe_allow_html=True)

    with st.expander(
        "📊 Phase 3 peers — ~49 companies (FY25+, current)", expanded=False
    ):
        st.caption(
            "Group TSR benchmark group — significantly expanded to include Tencent-adjacent "
            "and global internet peers, reflecting the Group TSR measure."
        )
        companies_p3 = [
            "Adyen", "Airbnb", "Alibaba", "Alphabet", "Amazon",
            "Baidu", "Booking Holdings", "ByteDance (private — excluded if unlisted)",
            "Coupang", "DoorDash", "eBay", "Etsy", "Expedia",
            "Facebook (Meta)", "Grab", "IACI", "JD.com", "Just Eat Takeaway",
            "Kakao", "Kuaishou", "Lazada (Alibaba sub)", "Line", "MercadoLibre",
            "Microsoft", "Meituan", "Netflix", "Naver", "PayPal",
            "Pinduoduo (PDD)", "Rakuten", "Roblox", "Sea Limited", "Shopify",
            "Snap", "Spotify", "Square (Block)", "Tencent", "TikTok (ByteDance)",
            "Toast", "Trip.com", "Twitter (X)", "Uber", "Vinted",
            "Wayfair", "Wise", "Zalando", "Zomato", "Zynga",
            "iQIYI",
        ]
        chips_html_p3 = " ".join(f'<span class="chip">{c}</span>' for c in companies_p3)
        st.markdown(chips_html_p3, unsafe_allow_html=True)
        st.markdown(
            '<div class="callout-blue">The Phase 3 group was significantly expanded '
            "(from ~23 to ~49 companies) to reflect the shift to Group TSR, which now "
            "includes Tencent and the full Prosus portfolio. A broader peer group provides "
            "a more robust relative ranking.</div>",
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="callout-yellow"><strong>Next peer group review:</strong> A new peer group '
        "will be approved by RemCo at the <strong>June 2026</strong> meeting for future awards. "
        "Additions apply on a forward-looking basis only.</div>",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Section: Malus & clawback
# ---------------------------------------------------------------------------
def show_malus_clawback():
    st.markdown("# Malus & clawback")
    st.markdown(
        "These provisions give RemCo the ability to reduce or recover awards in cases of "
        "serious misconduct. They are **not** intended to correct underperformance — "
        "underperformance is handled by the vesting schedule itself."
    )
    st.markdown("")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div class="info-card card-blue">
            <h3 style="color:#0332AF">Malus (pre-vesting)</h3>
            <p>RemCo may <strong>reduce or cancel</strong> unvested PSUs before the vesting date.
            No shares have been delivered yet — the adjustment happens to the outstanding award.</p>
            <ul>
            <li>Applies from the grant date until the vesting date</li>
            <li>Can reduce award to zero</li>
            <li>Does not require any recovery action from the individual</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="info-card card-teal">
            <h3 style="color:#00D3AF">Clawback (post-vesting)</h3>
            <p>RemCo may <strong>recover shares or cash equivalent</strong> from the individual
            after shares have already been delivered at vesting.</p>
            <ul>
            <li>Applies for <strong>2 years</strong> after the vesting date</li>
            <li>Recovery may be in shares or cash equivalent</li>
            <li>Requires a formal RemCo resolution</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("🚨 Triggers", expanded=True):
        st.markdown(
            '<div class="callout-red">'
            "<strong>Material financial misstatement:</strong> If the Group's financial "
            "statements are materially restated, and the restatement would have resulted in "
            "fewer PSUs vesting, RemCo may apply malus or clawback to recover the difference.<br><br>"
            "<strong>Termination for cause:</strong> If an executive is dismissed for gross "
            "misconduct, fraud, breach of fiduciary duty, or a serious regulatory violation, "
            "RemCo may apply malus and/or clawback to all outstanding and recently vested awards.<br><br>"
            "<em>Note: Triggers must relate to acts or omissions during the measurement period.</em>"
            "</div>",
            unsafe_allow_html=True,
        )

    with st.expander("📋 Limitations", expanded=True):
        st.markdown(
            '<div class="callout-grey">'
            "1. <strong>Time limit:</strong> Clawback is limited to 2 years post-vesting. "
            "After this window, recovery is not possible under the plan rules.<br>"
            "2. <strong>Jurisdiction:</strong> Recovery mechanisms may be limited by local "
            "employment law in the executive's country of employment. Legal advice is obtained "
            "before any clawback action is initiated.<br>"
            "3. <strong>RemCo discretion:</strong> RemCo must pass a resolution to activate "
            "malus or clawback. The provisions do not operate automatically."
            "</div>",
            unsafe_allow_html=True,
        )


# ---------------------------------------------------------------------------
# Section: Value creation
# ---------------------------------------------------------------------------
def show_value_creation():
    st.markdown("# Value creation")
    st.markdown(
        "This section will present the current indicative performance of in-flight PSU awards, "
        "based on the latest available TSR data."
    )
    st.markdown("")

    st.info("⏳ **To be completed** — The Group Valuations team is preparing this data.")

    st.markdown("### What will be included:")
    items = [
        "Current indicative Group TSR percentile rank vs peer group as at 31 March 2026",
        "Indicative vesting percentage for each in-flight tranche (FY25 CEO award, FY26 CFO award)",
        "Indicative gross value of in-flight awards at 31 March 2026 share prices",
        "Commentary on the absolute underpin status — is Group TSR positive or negative?",
        "Commentary on the market-shock extension trigger — is peer group avg TSR below −10%?",
        "Historical realised vesting outcomes for prior Ecommerce CAGR tranches",
    ]
    for item in items:
        st.markdown(f"• {item}")

    st.caption("Calculations based on third-party TSR data in USD. Contact: shares@prosus.com")


# ---------------------------------------------------------------------------
# Sidebar navigation
# ---------------------------------------------------------------------------
def show_sidebar():
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        '<p style="color:#00D3AF;font-size:11px;text-transform:uppercase;'
        'letter-spacing:2px;">CONTENTS</p>',
        unsafe_allow_html=True,
    )

    sections = [
        "📋 What are PSUs?",
        "📈 Types of PSUs",
        "📐 How performance is measured",
        "👥 Eligibility & current awards",
        "🌍 Peer group",
        "⚖️ Malus & clawback",
        "💰 Value creation",
    ]
    section = st.sidebar.radio("", sections, label_visibility="collapsed")

    st.sidebar.markdown("---")
    st.sidebar.markdown(
        '<p style="color:#00D3AF;font-size:11px;">shares@prosus.com</p>',
        unsafe_allow_html=True,
    )
    authenticator.logout("Log out", "sidebar")
    return section


# ---------------------------------------------------------------------------
# Main app
# ---------------------------------------------------------------------------
def main():
    # Inject CSS
    st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)

    # Header bar
    st.markdown(
        '<div class="prosus-header">Prosus &nbsp;|&nbsp; PSU Board Onboarding '
        '<span class="prosus-header-right">For Board Use Only</span></div>',
        unsafe_allow_html=True,
    )

    # Auth
    name, authentication_status, username = authenticator.login("Login", "main")

    if authentication_status is False:
        st.error("Incorrect username or password.")
    elif authentication_status is None:
        st.info("Please enter your login credentials above.")
    elif authentication_status:
        # Show sidebar nav and route to section
        section = show_sidebar()

        if "What are PSUs" in section:
            show_what_are_psus()
        elif "Types of PSUs" in section:
            show_types_of_psus()
        elif "How performance" in section:
            show_how_performance_measured()
        elif "Eligibility" in section:
            show_eligibility()
        elif "Peer group" in section:
            show_peer_group()
        elif "Malus" in section:
            show_malus_clawback()
        elif "Value creation" in section:
            show_value_creation()


if __name__ == "__main__":
    main()
