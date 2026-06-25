import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

class ReportGenerator:
    @staticmethod
    def generate_scan_pdf(scan_id: int, data: dict, output_path: str):
        doc = SimpleDocTemplate(output_path, pagesize=letter)
        styles = getSampleStyleSheet()
        
        # Custom Security Branded Style
        title_style = ParagraphStyle(
            'ReportTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor("#1e293b"),
            spaceAfter=20
        )
        
        story = []
        story.append(Paragraph("DEEPFAKE AUDIT & FORENSIC REPORT", title_style))
        story.append(Spacer(1, 12))
        
        # Report Body
        story.append(Paragraph(f"<b>Scan ID:</b> {scan_id}", styles['Normal']))
        story.append(Paragraph(f"<b>Target File:</b> {data['file_name']}", styles['Normal']))
        story.append(Paragraph(f"<b>Verdict:</b> {data['prediction']}", styles['Normal']))
        story.append(Paragraph(f"<b>Confidence Score:</b> {data['confidence_score']}%", styles['Normal']))
        story.append(Spacer(1, 10))
        story.append(Paragraph(f"<b>Cyber-Security Metadata:</b> {data.get('logs', 'N/A')}", styles['Normal']))
        
        doc.build(story)
        return output_path