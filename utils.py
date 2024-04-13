import io
import streamlit as st
from docx import Document
from docx.shared import Pt
from docx.enum.style import WD_STYLE_TYPE
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def download_word(content, filename):
    doc = Document()
    
    # Define styles for section headings and paragraphs
    section_heading_style = doc.styles.add_style('Section Heading', WD_STYLE_TYPE.PARAGRAPH)
    section_heading_style.font.name = 'Arial'
    section_heading_style.font.size = Pt(14)
    section_heading_style.font.bold = True
    
    paragraph_style = doc.styles.add_style('Paragraph', WD_STYLE_TYPE.PARAGRAPH)
    paragraph_style.font.name = 'Arial'
    paragraph_style.font.size = Pt(12)
    
    # Split the content into sections
    sections = content.split('\n\n')
    
    for section in sections:
        lines = section.split('\n')
        if len(lines) > 0:
            # Add section heading
            section_heading = lines[0].strip()
            doc.add_paragraph(section_heading, style='Section Heading')
            
            # Add section content
            for line in lines[1:]:
                if line.strip():
                    doc.add_paragraph(line.strip(), style='Paragraph')
    
def download_pdf(content, filename):
    styles = getSampleStyleSheet()
    custom_style = ParagraphStyle(
        name='CustomStyle',
        parent=styles['Normal'],
        fontSize=12,
        leading=18,
        spaceAfter=12
    )
    heading_style = ParagraphStyle(
        name='HeadingStyle',
        parent=styles['Heading1'],
        fontSize=14,
        leading=18,
        spaceBefore=12,
        spaceAfter=6
    )
    elements = []
    for section in content.split('\n\n'):
        lines = section.split('\n')
        if len(lines) > 0:
            elements.append(Paragraph(lines[0].strip(), heading_style))
            for line in lines[1:]:
                if line.strip():
                    elements.append(Paragraph(line.strip(), custom_style))
            elements.append(Spacer(1, 12))
    
    def canvasmaker(filename):
        doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
        return doc

    byte_io = io.BytesIO()
    doc = canvasmaker(byte_io)
    doc.build(elements)
    byte_io.seek(0)
    
    st.download_button(
        label="Download PDF",
        data=byte_io,
        file_name=filename,
        mime="application/pdf"
    )

def download_pdf(content, filename):
    styles = getSampleStyleSheet()
    custom_style = ParagraphStyle(
        name='CustomStyle',
        parent=styles['Normal'],
        fontSize=12,
        leading=18,
        spaceAfter=12
    )
    heading_style = ParagraphStyle(
        name='HeadingStyle',
        parent=styles['Heading1'],
        fontSize=14,
        leading=18,
        spaceBefore=12,
        spaceAfter=6
    )
    elements = []
    for section in content.split('\n\n'):
        lines = section.split('\n')
        if len(lines) > 0:
            elements.append(Paragraph(lines[0].strip(), heading_style))
            for line in lines[1:]:
                if line.strip():
                    elements.append(Paragraph(line.strip(), custom_style))
            elements.append(Spacer(1, 12))
    
    def canvasmaker(filename):
        doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
        return doc

    byte_io = io.BytesIO()
    doc = canvasmaker(byte_io)
    doc.build(elements)
    byte_io.seek(0)
    
    st.download_button(
        label="Download PDF",
        data=byte_io,
        file_name=filename,
        mime="application/pdf"
    )