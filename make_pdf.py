# -*- coding: utf-8 -*-
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Preformatted
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            super().showPage()
        super().save()

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#718096"))
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(letter[0] - 40, 30, page_text)
        self.drawString(40, 30, "Quantitative Finance Toolkit - Integrated Report (Lean, awesome-quant, qlib, vectorbt)")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(40, 42, letter[0] - 40, 42)
        self.restoreState()

def generate_pdf():
    pdf_path = "e:/comp_memory/library/Quant_Analysis_Report.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=40,
        bottomMargin=55
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#475569"),
        spaceAfter=15
    )

    h1_style = ParagraphStyle(
        'Header1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor("#1E3A8A"),
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Header2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor("#1E40AF"),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#1E293B"),
        spaceAfter=6
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=6
    )

    story = []

    # Title & Metadata
    story.append(Paragraph("Quantitative Finance Toolkit - Integrated Academic & Technical Report", title_style))
    story.append(Paragraph("<b>Source Repositories:</b> Lean, awesome-quant, qlib, vectorbt &nbsp;|&nbsp; <b>Domain:</b> Alpha Engineering & Financial Machine Learning Systems", subtitle_style))
    story.append(Spacer(1, 4))

    # Section 1: Overview
    story.append(Paragraph("1. System Overview and Core Strengths of the 4 Repositories", h1_style))
    story.append(Paragraph("The four repositories comprise a complete institutional-grade algorithmic trading architecture:", body_style))

    table_data = [
        [Paragraph("<b>Repository</b>", body_style), Paragraph("<b>Tech Architecture</b>", body_style), Paragraph("<b>Core Strengths and Strategic Role</b>", body_style)],
        [
            Paragraph("<b>Lean</b><br/>(QuantConnect)", body_style),
            Paragraph("C# Core / Python API<br/>Event-driven Engine", body_style),
            Paragraph("<b>Production Execution Engine & Risk Management:</b> Institutional architecture with full connectivity to major brokers (Interactive Brokers, Binance, OANDA). Handles tick-level execution, slippage models, transaction fees, dividend corporate actions, and margin control.", body_style)
        ],
        [
            Paragraph("<b>awesome-quant</b>", body_style),
            Paragraph("Academic Directory &<br/>Curated Repository", body_style),
            Paragraph("<b>Academic Knowledge Base:</b> Curated repository of empirical asset pricing papers (Fama-French, Lopez de Prado, Gu & Xiu), datasets (CRAN, macro feeds), and reference implementations.", body_style)
        ],
        [
            Paragraph("<b>qlib</b><br/>(Microsoft AI)", body_style),
            Paragraph("Python AI Platform<br/>Distributed Pipelines", body_style),
            Paragraph("<b>Large-Scale AI & Alpha Factory:</b> Data-centric platform optimized for machine learning in finance. Contains binary fast data storage, Alpha101 and Alpha158 factor libraries, and end-to-end model training wrappers (LightGBM, Transformer, GNN).", body_style)
        ],
        [
            Paragraph("<b>vectorbt</b>", body_style),
            Paragraph("NumPy / Numba JIT<br/>Rust Kernels", body_style),
            Paragraph("<b>Ultra-Fast Vectorized Backtesting:</b> Bypasses Python GIL via Numba JIT, processing millions of bars per second. Unlocks exhaustive hyperparameter optimization and interactive multidimensional visualization.", body_style)
        ]
    ]

    t = Table(table_data, colWidths=[90, 110, 330])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#F1F5F9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))

    # Section 2: Deep Dive into Alpha & ML
    story.append(Paragraph("2. Academic Foundations: Alpha Factor Engineering & Financial ML", h1_style))
    
    story.append(Paragraph("2.1. Alpha Factor Generation and Normalization Pipeline", h2_style))
    story.append(Paragraph("An alpha factor maps past market information to future expected asset returns: <code>f_t: F_t -> R^N</code>.", body_style))
    story.append(Paragraph("<b>1. MAD Winsorization (Outlier Control):</b> Instead of sensitive Mean/Std, compute <code>Median = median(X)</code> and <code>MAD = median(|X - Median|)</code>. Bound data to <code>[Median - 3*1.4826*MAD, Median + 3*1.4826*MAD]</code>.", body_style))
    story.append(Paragraph("<b>2. Neutralization (Pure Alpha Extraction):</b> Regress raw factor against Market Cap and Industry Dummies using OLS: <code>f_i = beta_0 + beta_m*ln(Cap_i) + sum(gamma_k * Industry_i,k) + epsilon_i</code>. The residual <code>epsilon_i</code> is pure alpha.", body_style))
    story.append(Paragraph("<b>3. Factor Evaluation Metrics:</b>", body_style))
    story.append(Paragraph("• <b>Information Coefficient (IC):</b> <code>IC_t = corr(f_t, R_t+1)</code>.<br/>"
                           "• <b>Rank IC:</b> Spearman correlation <code>Rank IC_t = 1 - (6 * sum(d_i^2)) / (N*(N^2 - 1))</code>.<br/>"
                           "• <b>Information Ratio (IR):</b> <code>IR = Mean(IC) / Std(IC) * sqrt(252)</code> (Target: IR > 1.5).", body_style))

    story.append(Paragraph("2.2. Financial Machine Learning System Architecture", h2_style))
    story.append(Paragraph("<b>1. Purged & Embargoed Cross-Validation:</b> Standard random k-fold leaks future returns due to serial correlation. Purging drops train labels whose holding periods overlap test windows; Embargoing adds a buffer zone immediately after test folds.", body_style))
    story.append(Paragraph("<b>2. Triple-Barrier Labeling:</b> Replaces arbitrary fixed-horizon returns with path-dependent dynamic barriers based on volatility: Upper Barrier (Take Profit, label +1), Lower Barrier (Stop Loss, label -1), and Vertical Barrier (Holding time expiration, label 0).", body_style))
    story.append(Paragraph("<b>3. Model Family:</b> LightGBM/CatBoost optimized with LambdaMART for cross-sectional ranking; Sequence models (TCN, Transformer) for capturing temporal order flow regimes.", body_style))

    story.append(Spacer(1, 10))

    # Section 3: The 4 Core Skills
    story.append(Paragraph("3. The Four Core Skills to Master", h1_style))

    skills_data = [
        [
            Paragraph("<b>SKILL 1: Alpha Factor Engineering</b><br/><i>(qlib, awesome-quant)</i>", body_style),
            Paragraph("• Formulate mathematical cross-sectional alphas using time-series operators (Ts_Rank, Ts_ArgMax, Decay_Linear).<br/>"
                      "• Build automated data cleansing pipelines: MAD Winsorization, OLS Industry/Market-Cap Neutralization, and Z-Score standardization.<br/>"
                      "• Verify predictive power using Information Coefficient (IC), Rank IC, Information Ratio (IR > 1.5), and Quantile Monotonicity.", body_style)
        ],
        [
            Paragraph("<b>SKILL 2: Financial Machine Learning Systems</b><br/><i>(qlib Model Zoo, PyTorch, LightGBM)</i>", body_style),
            Paragraph("• Enforce strict Point-in-Time (PIT) data structures to eliminate look-ahead and survivorship bias.<br/>"
                      "• Implement Purged and Embargoed Walk-Forward Cross-Validation.<br/>"
                      "• Deploy Triple-Barrier Labeling and Meta-Labeling (secondary model filtering false-positive trade signals and calibrating bet size).", body_style)
        ],
        [
            Paragraph("<b>SKILL 3: Vectorized Simulation & Risk Profiling</b><br/><i>(vectorbt, Numba, Rust)</i>", body_style),
            Paragraph("• Compile high-performance signal generators using Numba JIT (<code>@njit(nogil=True)</code>).<br/>"
                      "• Incorporate market friction models: Almgren-Chriss quadratic slippage, borrow financing rates for short positions, and exchange tiers.<br/>"
                      "• Compute rigorous risk metrics: Deflated Sharpe Ratio (DSR), Expected Shortfall (CVaR 99%), and Max Drawdown Duration.", body_style)
        ],
        [
            Paragraph("<b>SKILL 4: Production Execution & Modular Framework</b><br/><i>(QuantConnect Lean Framework)</i>", body_style),
            Paragraph("• Master Lean's 5-stage algorithm modularization: <i>Universe Selection -> Alpha Creation -> Portfolio Construction -> Execution -> Risk Management</i>.<br/>"
                      "• Implement institutional execution algorithms (TWAP, VWAP) to minimize market impact.<br/>"
                      "• Containerize trading pipelines via Docker, with automated real-time broker reconnection and fail-safe circuit breakers.", body_style)
        ]
    ]

    st = Table(skills_data, colWidths=[150, 380])
    st.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#F8FAFC")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(st)

    story.append(Spacer(1, 10))

    # Section 4: Unified Workflow Blueprint
    story.append(Paragraph("4. End-to-End Unified Quantitative Blueprint", h1_style))
    pipeline_code = """[ Raw Market Feeds (Tick / Minute / Daily) ]
       |---> (qlib DataHandler: Point-in-Time cleaning, binary tensor storage)
[ Alpha Matrix: Alpha101 / Alpha158 Factors ]
       |---> (Triple-Barrier Path Labeling + Purged Cross-Validation)
[ Ensemble ML Model: LightGBM / Temporal Transformer ]
       |---> (Predicted Alpha Scores & Probability Signals)
[ vectorbt Fast Engine: Parameter Surface Exploration, DSR & CVaR Filtering ]
       |---> (Validated Strategy Parameters)
[ QuantConnect LEAN Algorithm Engine: Live Brokerage Execution & Real-Time Risk ]"""
    story.append(Preformatted(pipeline_code, code_style))

    story.append(Paragraph("5. Academic References & Citations", h1_style))
    refs = (
        "• <b>Gu, S., Kelly, B., & Xiu, D. (2020).</b> <i>Empirical Asset Pricing via Machine Learning.</i> The Review of Financial Studies, 33(5), 2223-2273.<br/>"
        "• <b>López de Prado, M. (2018).</b> <i>Advances in Financial Machine Learning.</i> John Wiley & Sons.<br/>"
        "• <b>Kakushadze, Z. (2016).</b> <i>101 Formulaic Alphas.</i> Wilmott Magazine, 2016(84), 72-81.<br/>"
        "• <b>Almgren, R., & Chriss, N. (2000).</b> <i>Optimal execution of portfolio transactions.</i> Journal of Risk, 3, 5-40."
    )
    story.append(Paragraph(refs, body_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully generated at: {pdf_path}")

if __name__ == "__main__":
    generate_pdf()
