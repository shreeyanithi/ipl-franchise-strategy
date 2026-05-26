# IPL Franchise Strategy Report Generator
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.units import inch
import os

OUTPUT_PATH = r"C:/Users/shree/OneDrive/ipl_project/outputs"
REPORT_PATH = r"C:/Users/shree/OneDrive/ipl_project/report"

doc = SimpleDocTemplate(
    os.path.join(REPORT_PATH, "IPL_Franchise_Strategy_Report.pdf"),
    pagesize=A4, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50
)

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle('Title', fontSize=24, fontName='Helvetica-Bold',
    textColor=colors.HexColor('#1F3864'), spaceAfter=8, alignment=1)
subtitle_style = ParagraphStyle('Subtitle', fontSize=13, fontName='Helvetica',
    textColor=colors.HexColor('#444444'), spaceAfter=20, alignment=1)
h1_style = ParagraphStyle('H1', fontSize=16, fontName='Helvetica-Bold',
    textColor=colors.HexColor('#1F3864'), spaceAfter=10, spaceBefore=15)
h2_style = ParagraphStyle('H2', fontSize=12, fontName='Helvetica-Bold',
    textColor=colors.HexColor('#2E75B6'), spaceAfter=6, spaceBefore=10)
body_style = ParagraphStyle('Body', fontSize=10, fontName='Helvetica',
    textColor=colors.HexColor('#333333'), spaceAfter=6, leading=15)
insight_style = ParagraphStyle('Insight', fontSize=10, fontName='Helvetica',
    textColor=colors.HexColor('#1F3864'), spaceAfter=4, leading=14,
    leftIndent=20, borderPad=5)

story = []

# ── PAGE 1: COVER ──────────────────────────────────────
story.append(Spacer(1, 1.5*inch))
story.append(Paragraph("IPL FRANCHISE STRATEGY", title_style))
story.append(Paragraph("Performance & Investment Analysis", subtitle_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("2008 – 2020 | All Franchises | Data-Driven Business Case", subtitle_style))
story.append(Spacer(1, 0.5*inch))

cover_data = [
    ['Prepared by', 'Shreeya Nithi G'],
    ['Dataset', 'IPL Matches, Deliveries & Auction Data'],
    ['Seasons Covered', '2008 – 2020 (13 seasons)'],
    ['Total Matches Analysed', '1,095'],
    ['Total Deliveries', '2,60,920'],
    ['Tools Used', 'Python · Excel · ReportLab'],
]
cover_table = Table(cover_data, colWidths=[2.5*inch, 3.5*inch])
cover_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#1F3864')),
    ('TEXTCOLOR', (0,0), (0,-1), colors.white),
    ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('ROWBACKGROUNDS', (1,0), (1,-1), [colors.HexColor('#EBF3FB'), colors.white]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
    ('PADDING', (0,0), (-1,-1), 8),
]))
story.append(cover_table)
story.append(PageBreak())

# ── PAGE 2: PROBLEM & DATA ─────────────────────────────
story.append(Paragraph("1. Business Problem", h1_style))
story.append(Paragraph(
    "IPL franchises invest hundreds of crores annually in player auctions with no guarantee of "
    "on-field success. This analysis addresses the central question facing every franchise "
    "management team: <b>Which strategies consistently drive playoff qualification and what does "
    "the data say about the real return on player investment?</b>", body_style))

story.append(Paragraph("2. Data Overview", h1_style))
data_table_data = [
    ['Dataset', 'Records', 'Key Fields'],
    ['matches.csv', '1,095 rows', 'season, teams, winner, toss, venue'],
    ['deliveries.csv', '2,60,920 rows', 'batter, bowler, runs, wickets'],
    ['IPLPlayerAuctionData.csv', '970 rows', 'player, team, role, amount, year'],
]
data_table = Table(data_table_data, colWidths=[2*inch, 1.5*inch, 3*inch])
data_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2E75B6')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#EBF3FB'), colors.white]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
    ('PADDING', (0,0), (-1,-1), 7),
]))
story.append(data_table)
story.append(PageBreak())

# ── PAGE 3: KEY FINDINGS ───────────────────────────────
story.append(Paragraph("3. Key Findings", h1_style))

story.append(Paragraph("Finding 1 — Franchise Win Rates", h2_style))
story.append(Paragraph(
    "Across 1,095 matches (2008–2020), win rates vary dramatically between franchises. "
    "Gujarat Titans lead at 62.2%, followed by CSK at 58.2% and Mumbai Indians at 55.2%. "
    "Critically, the three lowest-spending franchises in this group (GT, LSG, CSK) all "
    "outperform higher-spending rivals.", body_style))
img_path = os.path.join(OUTPUT_PATH, 'franchise_win_rate.png')
if os.path.exists(img_path):
    story.append(Image(img_path, width=5*inch, height=2.5*inch))

story.append(Paragraph("Finding 2 — Spend vs Performance", h2_style))
story.append(Paragraph(
    "Total auction spend shows a <b>negative correlation</b> with win rate among the top spenders. "
    "Punjab Kings (297 Cr, 45.5%) and RCB (270 Cr, 48.9%) represent the worst investment "
    "efficiency in the league. In contrast, CSK (157 Cr, 58.2%) and GT (51 Cr, 62.2%) "
    "demonstrate that smart retention beats aggressive auction spending.", body_style))
img_path2 = os.path.join(OUTPUT_PATH, 'spend_vs_wins.png')
if os.path.exists(img_path2):
    story.append(Image(img_path2, width=5*inch, height=2.5*inch))
story.append(PageBreak())

# ── PAGE 4: ROOT CAUSE ────────────────────────────────
story.append(Paragraph("4. Root Cause Analysis", h1_style))

story.append(Paragraph("Why do high-spending franchises underperform?", h2_style))
causes = [
    "• <b>Auction inflation:</b> Franchises overpay for marquee names at auction, driven by fan pressure rather than data.",
    "• <b>Poor player retention:</b> Releasing proven performers and rebuilding annually disrupts team cohesion.",
    "• <b>Toss strategy misalignment:</b> Fielding first wins 53.9% vs 45.4% for batting first — yet many franchises ignore this.",
    "• <b>Bowling neglect:</b> Top franchises build around high-wicket, low-economy bowlers (Narine: 200 wkts, 6.76 economy). Underperforming franchises prioritise batting at auction.",
]
for c in causes:
    story.append(Paragraph(c, insight_style))
    story.append(Spacer(1, 4))

story.append(Paragraph("Toss & Strategy Analysis", h2_style))
toss_data = [
    ['Metric', 'Value', 'Implication'],
    ['Toss winner wins match', '50.8%', 'Toss is effectively a coin flip'],
    ['Win rate — Field first', '53.9%', 'Strong advantage for fielding'],
    ['Win rate — Bat first', '45.4%', 'Batting first is a disadvantage'],
    ['Home team win rate', '50.9%', 'Home advantage is minimal'],
]
toss_table = Table(toss_data, colWidths=[2.5*inch, 1.2*inch, 2.8*inch])
toss_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1F3864')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#EBF3FB'), colors.white]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
    ('PADDING', (0,0), (-1,-1), 7),
]))
story.append(toss_table)
story.append(PageBreak())

# ── PAGE 5: RECOMMENDATIONS ───────────────────────────
story.append(Paragraph("5. Strategic Recommendations", h1_style))
story.append(Paragraph(
    "Based on data analysis across 13 IPL seasons, the following recommendations are "
    "presented for franchise management teams seeking to maximise playoff qualification probability:", 
    body_style))

recs = [
    ("Prioritise Player Retention Over Auction Spending",
     "CSK's model proves it: retaining proven performers costs less and wins more. "
     "Avoid rebuilding squads annually. Target a core retained squad of 8-10 players."),
    ("Field First — Always",
     "When you win the toss, field first. The data is unambiguous: fielding first "
     "delivers a 53.9% win rate vs 45.4% for batting first — an 8.5 percentage point advantage."),
    ("Build Bowling Around Economy, Not Just Wickets",
     "SP Narine (6.76 economy, 200 wickets) represents the ideal bowler profile. "
     "Target spinners with sub-7.0 economy rates — they win matches in the middle overs."),
    ("Target Undervalued Domestic Players",
     "Shubman Gill delivers 1,786 runs per crore — 4x the value of premium overseas buys. "
     "Allocate 40% of auction budget to emerging Indian talent under 5 Crore."),
]

for i, (title, body) in enumerate(recs):
    story.append(Paragraph(f"Recommendation {i+1}: {title}", h2_style))
    story.append(Paragraph(body, body_style))
    story.append(Spacer(1, 6))

story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("— End of Report —", subtitle_style))

doc.build(story)
print("✅ PDF Report generated successfully!")
print(f"Saved to: {REPORT_PATH}")