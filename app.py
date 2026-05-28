"""
Prosus PSU Onboarding Dashboard
Streamlit app with email whitelist authentication
"""

import streamlit as st
import pandas as pd
import os

# ---------------------------------------------------------------------------
# Authentication setup — email whitelist
# ---------------------------------------------------------------------------
def load_whitelist():
    """Load allowed email addresses from users.txt"""
    whitelist_path = os.path.join(os.path.dirname(__file__), "users.txt")
    if os.path.exists(whitelist_path):
        with open(whitelist_path) as f:
            return [line.strip() for line in f if line.strip()]
    return []

ALLOWED_EMAILS = load_whitelist()

# ---------------------------------------------------------------------------
# Page config — must be FIRST Streamlit call
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Prosus | PSU Onboarding",
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

/* Logout button styling */
[data-testid="stSidebar"] .stButton > button {
    background-color: #00D3AF !important;
    color: #081A54 !important;
    border: none !important;
    font-weight: bold !important;
    border-radius: 6px !important;
    width: 100% !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background-color: #00B89A !important;
    color: #081A54 !important;
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
.styled-table { width:100%; border-collapse:collapse; font-size:14px; }
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
    st.caption("A primer for new participants")
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
            <li><strong>Protect shareholders</strong> — the absolute underpin (post-CEO appointment)
            means awards lapse entirely if Group TSR is negative</li>
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
        "part of the recipient's employment contract. RemCo has full discretion over the "
        "administration and determination of awards.</div>",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Section: Types of PSUs
# ---------------------------------------------------------------------------
def show_types_of_psus():
    st.markdown("# Types of PSUs")
    st.markdown(
        "Prosus has operated three successive designs of PSU, each reflecting the "
        "Group's evolving strategy and listing structure."
    )
    st.markdown("")

    def html_table(rows):
        header = "<thead><tr><th>Design element</th><th>Detail</th></tr></thead>"
        body_rows = "".join(f"<tr><td>{r[0]}</td><td>{r[1]}</td></tr>" for r in rows)
        return f'<table class="styled-table">{header}<tbody>{body_rows}</tbody></table>'

    # Ecommerce CAGR — merged pre- and post-Prosus listing
    with st.expander("📊 Ecommerce CAGR | Pre- & post-Prosus listing · FY20–FY24"):
        # Merged 3-column table matching PPTX v7
        merged_html = """
<table class="styled-table">
  <thead>
    <tr>
      <th>Design element</th>
      <th>Ecommerce CAGR</th>
      <th>Group TSR (current)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="font-weight:bold">Plan</td><td>Naspers RSP Trust / Prosus Share Award Plan</td><td>Naspers RSP Trust & Prosus Share Award Plan</td></tr>
    <tr><td style="font-weight:bold">Settlement</td><td>Naspers Class N shares / Prosus Class N shares</td><td>Combination of Naspers and Prosus Class N shares</td></tr>
    <tr><td style="font-weight:bold">Performance measure</td><td>3-year Ecommerce CAGR of portfolio (ex-Tencent) vs peer group</td><td>Group TSR (Naspers + Prosus combined) vs peer group</td></tr>
    <tr><td style="font-weight:bold">Measurement period</td><td>3 years</td><td>4 years (extendable to 5 if peer avg TSR ≤ −10%)</td></tr>
    <tr><td style="font-weight:bold">Vesting*</td><td>100% cliff vest — 3rd anniversary</td><td>100% cliff vest — 4th anniversary</td></tr>
    <tr><td style="font-weight:bold">Absolute underpin</td><td>None</td><td>YES — lapses if Group TSR is negative</td></tr>
    <tr><td style="font-weight:bold">Malus</td><td>No (pre-Prosus listing) / Yes (post-Prosus listing)</td><td>Yes</td></tr>
    <tr><td style="font-weight:bold">Clawback</td><td>2 years post-vest</td><td>2 years post-vest</td></tr>
    <tr><td style="font-weight:bold">Peer group</td><td>~21 companies (pre-Prosus listing) / ~23 companies (post-Prosus listing)</td><td>~49 companies</td></tr>
    <tr><td style="font-weight:bold">Recipients</td><td>All eligible executives</td><td>CEO (FY25); CFO (FY26 onwards)</td></tr>  </tbody>
</table>
<p style="font-size:12px;color:#808080;font-style:italic;margin-top:8px;">* See 'How performance is measured' for the full vesting payout schedule.</p>
"""
        st.markdown(merged_html, unsafe_allow_html=True)
        st.markdown(
            '<div class="callout-blue">The Ecommerce CAGR plan ran in two sub-periods: '
            'pre-Prosus listing (Naspers RSP Trust, ~21 peers) and post-Prosus listing '
            '(Prosus SAP, ~23 peers). The core design was identical. See Types of PSUs for full '
            'design element comparison.</div>',
            unsafe_allow_html=True,
        )

        # Group TSR — post-CEO appointment (current)
    with st.expander(
        "📊 Group TSR | Post-CEO appointment · FY25 onwards ⭐ CURRENT", expanded=True
    ):
        rows3 = [
            ("Plan", "Naspers RSP Trust / Prosus Share Award Plan"),
            ("Settlement", "Naspers Class N ordinary shares OR Prosus ordinary shares"),
            ("Performance measure", "Group TSR (Total Shareholder Return) of the combined Naspers + Prosus group "
             "vs an expanded peer group of ~43 global tech/internet companies"),
            ("Measurement period", "4 years (extended from 3 years in the earlier Ecommerce CAGR periods)"),
            ("Vesting", "100% cliff vest on the 4th anniversary of grant date"),
            ("Threshold", "30th percentile → 50% of PSUs vest (raised from 25th in the earlier Ecommerce CAGR periods)"),
            ("Target", "50th percentile → 100% of PSUs vest"),
            ("Maximum", "75th percentile → 200% of PSUs vest (capped)"),
            ("Absolute underpin", "New: Award lapses entirely if Group TSR is negative over the period"),
            ("Malus", "Yes — applicable from grant date"),
            ("Clawback", "2 years post-vest"),
            ("Recipients", "CEO (FY25); CFO (FY26+)"),
        ]
        st.markdown(html_table(rows3), unsafe_allow_html=True)
        st.markdown(
            '<div class="callout-yellow">Three significant changes from the earlier Ecommerce CAGR periods: '
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

    vesting_table_html = """
<table class="styled-table">
  <thead>
    <tr>
      <th>Performance Level</th>
      <th>Percentile Rank</th>
      <th>Shares Vesting</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Below Threshold</td>
      <td>Below 25th percentile (Ecommerce CAGR) / Below 30th percentile (TSR PSUs)</td>
      <td>No shares vest</td>
    </tr>
    <tr>
      <td>Threshold</td>
      <td>25th percentile (Ecommerce CAGR) / 30th percentile (TSR PSUs)</td>
      <td>50% of awarded shares vest</td>
    </tr>
    <tr>
      <td>Target</td>
      <td>50th percentile (median)</td>
      <td>100% of awarded shares vest</td>
    </tr>
    <tr>
      <td>Maximum</td>
      <td>75th percentile</td>
      <td>200% of awarded shares vest</td>
    </tr>
  </tbody>
</table>
"""
    st.markdown(vesting_table_html, unsafe_allow_html=True)

    st.markdown(
        '<div class="callout-blue">'
        "Performance between threshold and maximum is interpolated on a straight-line (linear) basis.<br>"
        "Below threshold, no shares vest. Above the 75th percentile, the payout does not increase beyond 200%.<br><br>"
        "See <strong>Types of PSUs</strong> for full design element comparison."
        "</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="callout-red">'
        "<strong>TSR PSU absolute underpin:</strong> if Group TSR is negative over the measurement period, "
        "the award lapses in full — regardless of peer ranking."
        "</div>",
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

    st.markdown(
        """
**Key governance rules:**
- Approved by RemCo at the start of each measurement period — not changed mid-cycle
- Global technology and internet companies with broadly comparable business models
- Minimum market capitalisation threshold applies (typically US$5bn+)
- Delisted or acquired companies are removed; a replacement may be added at RemCo discretion
- TSR calculation uses 31-day trailing VWAP at start and end of the measurement period, in USD
"""
    )

    # FY26 current peer group only
    with st.expander("📊 FY26 TSR peer group — 43 companies (current)", expanded=True):
        st.caption(
            "Group TSR benchmark group — global technology, internet and ecommerce peers "
            "approved by RemCo for the post-CEO appointment period."
        )
        companies_fy26 = [
            "Adyen", "LY Corporation", "Airbnb", "Match Group", "Alphabet",
            "MercadoLibre", "Amazon", "Meta Platforms", "Auto Trader", "Ocado Group",
            "Bajaj Finance", "One97 Communications (Paytm)", "Block", "PayPal",
            "Booking Holdings", "Pinterest", "Chewy", "Rakuten Group", "Coupang",
            "Sea Limited", "Deliveroo", "Shopify", "DoorDash", "Snap", "eBay",
            "Uber", "Etsy", "Wayfair", "Expedia Group", "Zalando",
            "FSN Ecommerce (Nykaa)", "Zillow Group", "IAC", "Zomato", "Grab",
            "Ocado", "Just Eat Takeaway", "Chewy", "FSN Ecommerce",
            "Zillow", "Auto Trader", "Bajaj Finance", "Pinterest",
        ]
        chips_html = " ".join(f'<span class="chip">{c}</span>' for c in companies_fy26)
        st.markdown(chips_html, unsafe_allow_html=True)
        st.markdown(
            '<div class="callout-blue">The FY26 peer group reflects the shift to Group TSR '
            "and includes global internet, ecommerce and fintech peers. RemCo approves the "
            "peer group at the start of each measurement period.</div>",
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="callout-yellow"><strong>Next peer group review:</strong> A new peer group '
        "will be approved by RemCo at the <strong>June 2026</strong> meeting for future awards. "
        "Additions apply on a forward-looking basis only.</div>",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Section: Eligibility
# ---------------------------------------------------------------------------
def show_eligibility():
    st.markdown("# Eligibility")
    st.markdown(
        "Eligibility for PSU awards is determined by RemCo and disclosed in the annual "
        "Remuneration Report. Awards are personal and non-transferable."
    )
    st.markdown("")

    with st.expander("👤 Who is eligible?", expanded=True):
        st.markdown(
            """
**Pre-CEO appointment (Ecommerce CAGR period, FY20–FY24):**
Awards were granted to the CEO, CFO, and all other ELT (Executive Leadership Team) members.

**Post-CEO appointment (Group TSR period, FY25 onwards):**
Awards are granted to the CEO and CFO only.

RemCo reviews eligibility annually and may adjust at its discretion. Awards are personal and non-transferable.
"""
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
# Section: Historic Performance
# ---------------------------------------------------------------------------
def show_historic_performance():
    st.markdown("# Historic Performance")
    st.markdown(
        "Aggregated PSU grant history across all financial years. Individual award details "
        "are disclosed in the annual Remuneration Report."
    )
    st.markdown("")

    st.markdown(
        '<div class="callout-blue">'
        "Fair values, performance outcomes and payout figures for FY20–FY24 will be populated "
        "from the Remuneration Report. Unvested awards show current best estimates pending "
        "RemCo determination."
        "</div>",
        unsafe_allow_html=True,
    )

    historic_table_html = """
<table class="styled-table">
  <thead>
    <tr>
      <th>Financial Year</th>
      <th>PSU Type</th>
      <th>Measurement Metric</th>
      <th>Total Fair Value Awarded</th>
      <th>Measurement Period</th>
      <th>Vesting Date</th>
      <th>Status</th>
      <th>Performance %</th>
      <th>Payout</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>FY20</td>
      <td>Naspers Ecommerce CAGR PSU</td>
      <td>Ecommerce CAGR vs peers</td>
      <td>Placeholder</td>
      <td>FY20–FY23</td>
      <td>FY23</td>
      <td>Vested ✓</td>
      <td>Actual (TBC)</td>
      <td>Actual (TBC)</td>
    </tr>
    <tr>
      <td>FY21</td>
      <td>Naspers Ecommerce CAGR PSU</td>
      <td>Ecommerce CAGR vs peers</td>
      <td>Placeholder</td>
      <td>FY21–FY24</td>
      <td>FY24</td>
      <td>Vested ✓</td>
      <td>Actual (TBC)</td>
      <td>Actual (TBC)</td>
    </tr>
    <tr>
      <td>FY22</td>
      <td>Naspers + Prosus Ecommerce CAGR PSU</td>
      <td>Ecommerce CAGR vs peers</td>
      <td>Placeholder</td>
      <td>FY22–FY25</td>
      <td>FY25</td>
      <td>Vested ✓</td>
      <td>Actual (TBC)</td>
      <td>Actual (TBC)</td>
    </tr>
    <tr>
      <td>FY23</td>
      <td>Prosus Ecommerce CAGR PSU</td>
      <td>Ecommerce CAGR vs peers</td>
      <td>Placeholder</td>
      <td>FY23–FY26</td>
      <td>FY26</td>
      <td>Vested ✓</td>
      <td>Actual (TBC)</td>
      <td>Actual (TBC)</td>
    </tr>
    <tr>
      <td>FY24</td>
      <td>Prosus Ecommerce CAGR PSU</td>
      <td>Ecommerce CAGR vs peers</td>
      <td>Placeholder</td>
      <td>FY24–FY27</td>
      <td>FY27</td>
      <td>Vested ✓</td>
      <td>Actual (TBC)</td>
      <td>Actual (TBC)</td>
    </tr>
    <tr style="background-color: #FFF9E6;">
      <td>FY25</td>
      <td>Naspers TSR PSU + Prosus TSR PSU</td>
      <td>Group TSR vs peers</td>
      <td>US$27.0m (Fabricio CEO award)</td>
      <td>1 Jul 2024 – 30 Jun 2028</td>
      <td>~Jun 2028</td>
      <td>In flight ⏳</td>
      <td>Best estimate (TBC)</td>
      <td>Potential (TBC)</td>
    </tr>
    <tr style="background-color: #FFF9E6;">
      <td>FY26</td>
      <td>Naspers TSR PSU + Prosus TSR PSU</td>
      <td>Group TSR vs peers</td>
      <td>TBC (CFO award)</td>
      <td>FY26–FY30</td>
      <td>~FY30</td>
      <td>In flight ⏳</td>
      <td>Best estimate (TBC)</td>
      <td>Potential (TBC)</td>
    </tr>
  </tbody>
</table>
"""
    st.markdown(historic_table_html, unsafe_allow_html=True)

    st.markdown(
        '<div class="callout-yellow">'
        "<strong>FY25 award — absolute underpin:</strong> The FY25 award includes an absolute underpin: "
        "if Group TSR is negative over the measurement period, the award lapses entirely regardless of "
        "peer ranking."
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
        "🌍 Peer group",
        "👥 Eligibility",
        "⚖️ Malus & clawback",
        "📅 Historic Performance",
        "💰 Value creation",
    ]
    section = st.sidebar.radio("", sections, label_visibility="collapsed")

    st.sidebar.markdown("---")
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.user_email = ""
        st.rerun()
    return section


# ---------------------------------------------------------------------------
# Main app
# ---------------------------------------------------------------------------
def main():
    # Inject CSS
    st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)

    # Header bar
    st.markdown(
        '<div class="prosus-header">Prosus &nbsp;|&nbsp; PSU Onboarding '
        '<span class="prosus-header-right">Confidential</span></div>',
        unsafe_allow_html=True,
    )

    # Auth — email whitelist
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.user_email = ""

    if not st.session_state.authenticated:
        st.markdown("## Login")
        email = st.text_input("Enter your email address", key="login_email")
        if st.button("Sign In"):
            if email in ALLOWED_EMAILS:
                st.session_state.authenticated = True
                st.session_state.user_email = email
                st.rerun()
            else:
                st.error("Access denied. Your email is not on the whitelist.")
        st.info("Contact shares@prosus.com for access.")
        return

    name = st.session_state.user_email

    if True:
        # Show sidebar nav and route to section
        section = show_sidebar()

        if "What are PSUs" in section:
            show_what_are_psus()
        elif "Types of PSUs" in section:
            show_types_of_psus()
        elif "How performance" in section:
            show_how_performance_measured()
        elif "Peer group" in section:
            show_peer_group()
        elif "Eligibility" in section:
            show_eligibility()
        elif "Malus" in section:
            show_malus_clawback()
        elif "Historic" in section:
            show_historic_performance()
        elif "Value creation" in section:
            show_value_creation()


if __name__ == "__main__":
    main()
