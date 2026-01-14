from django.shortcuts import render
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch
from io import BytesIO


def my_home(request):
    """Render the home page"""
    context = {
        'name': 'Software Engineer',
        'title': 'Backend Developer',
        'email': 'robelhossain783@gmail.com',
        'phone': '+8801303750286',
        'location': 'Mohammadpur, Dhaka, Bangladesh',
    }
    return render(request, 'my_index.html', context)


# def download_cv(request):
#     """Generate and download CV as PDF"""
#     buffer = BytesIO()
#     doc = SimpleDocTemplate(buffer, pagesize=letter)
#     story = []
#     styles = getSampleStyleSheet()
#
#     # Custom styles
#     title_style = ParagraphStyle(
#         'CustomTitle',
#         parent=styles['Heading1'],
#         fontSize=24,
#         textColor=colors.HexColor('#1e40af'),
#         spaceAfter=30,
#         alignment=1  # Center
#     )
#
#     heading_style = ParagraphStyle(
#         'CustomHeading',
#         parent=styles['Heading2'],
#         fontSize=16,
#         textColor=colors.HexColor('#1e40af'),
#         spaceAfter=12,
#         spaceBefore=12
#     )
#
#     # Title
#     story.append(Paragraph("SOFTWARE ENGINEER", title_style))
#     story.append(Paragraph("Backend Developer | Python | Golang | DevOps", styles['Normal']))
#     story.append(Spacer(1, 0.2 * inch))
#
#     # Contact Info
#     contact_data = [
#         ['Email:', 'contact@example.com', 'Phone:', '+880 XXX-XXXXXX'],
#         ['Location:', 'Kafrul, Dhaka, Bangladesh', '', '']
#     ]
#     contact_table = Table(contact_data, colWidths=[1 * inch, 2.5 * inch, 1 * inch, 1.5 * inch])
#     contact_table.setStyle(TableStyle([
#         ('FONTSIZE', (0, 0), (-1, -1), 10),
#         ('TEXTCOLOR', (0, 0), (-1, -1), colors.grey),
#     ]))
#     story.append(contact_table)
#     story.append(Spacer(1, 0.3 * inch))
#
#     # Experience
#     story.append(Paragraph("PROFESSIONAL EXPERIENCE", heading_style))
#
#     story.append(Paragraph("<b>UCB Bank</b> - Software Engineer", styles['Normal']))
#     story.append(Paragraph("<i>March 2025 - Present (10 months)</i>", styles['Normal']))
#     story.append(Paragraph("• Working on banking solutions and financial systems", styles['Normal']))
#     story.append(Paragraph("• Developing scalable backend services using Python and Django", styles['Normal']))
#     story.append(Spacer(1, 0.2 * inch))
#
#     story.append(Paragraph("<b>Upay</b> - Software Engineer", styles['Normal']))
#     story.append(Paragraph("<i>May 2024 - March 2025 (10 months)</i>", styles['Normal']))
#     story.append(Paragraph("• Developed mobile financial services and payment solutions", styles['Normal']))
#     story.append(Paragraph("• Implemented REST APIs using Django REST Framework", styles['Normal']))
#     story.append(Spacer(1, 0.3 * inch))
#
#     # Skills
#     story.append(Paragraph("TECHNICAL SKILLS", heading_style))
#     skills_text = "Python • Golang • Django REST Framework • PostgreSQL • Redis • Docker • Kubernetes"
#     story.append(Paragraph(skills_text, styles['Normal']))
#     story.append(Spacer(1, 0.3 * inch))
#
#     # Education
#     story.append(Paragraph("EDUCATION", heading_style))
#     story.append(Paragraph("<b>Daffodil International University</b>", styles['Normal']))
#     story.append(Paragraph("Bachelor of Science in Computer Science & Engineering", styles['Normal']))
#     story.append(Paragraph("<i>January 2018 - February 2022</i>", styles['Normal']))
#     story.append(Paragraph("Department: CSE", styles['Normal']))
#
#     # Build PDF
#     doc.build(story)
#     buffer.seek(0)
#
#     response = HttpResponse(buffer, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="CV_Software_Engineer.pdf"'
#     return response
#
#

def download_cv(request):
    """Generate and download CV as PDF"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1e40af'),  # Indigo
        spaceAfter=20,
        alignment=1  # Center
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#1e40af'),
        spaceAfter=12,
        spaceBefore=12
    )

    normal_style = styles['Normal']

    # Title
    story.append(Paragraph("ROBEL HOSSAIN", title_style))
    story.append(Paragraph("Software Engineer | Backend Developer | Python | FinTech", normal_style))
    story.append(Spacer(1, 0.2 * inch))

    # Contact Info
    contact_data = [
        ['Email:', 'robelhossain783@gmail.com', 'Phone:', '+8801303-750286'],
        ['Location:', 'Mohammadpur, Dhaka, Bangladesh', 'GitHub:', 'github.com/robelhossain783'],
        ['LinkedIn:', 'linkedin.com/in/robelhossain783', '', '']
    ]
    contact_table = Table(contact_data, colWidths=[1.2*inch, 2.5*inch, 1.2*inch, 2.5*inch])
    contact_table.setStyle(TableStyle([
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.grey),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(contact_table)
    story.append(Spacer(1, 0.3 * inch))

    # Experience
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", heading_style))

    # Lite Technology Ltd.
    story.append(Paragraph("<b>Lite Technology Ltd.</b> - Software Engineer", normal_style))
    story.append(Paragraph("<i>October 2022 - Present</i>", normal_style))
    story.append(Paragraph("• Developing scalable backend solutions and integrating REST APIs.", normal_style))
    story.append(Paragraph("• Maintaining microservice architecture for high performance.", normal_style))
    story.append(Paragraph("• Implementing MFS features including fund transfer, customer authentication, and management services.", normal_style))
    story.append(Spacer(1, 0.2 * inch))

    # UCB Bank
    story.append(Paragraph("<b>UCB Bank</b> - Software Engineer", normal_style))
    story.append(Paragraph("<i>March 2025 - Present</i>", normal_style))
    story.append(Paragraph("• Working on core banking backend systems.", normal_style))
    story.append(Paragraph("• Developing secure and scalable financial services.", normal_style))
    story.append(Paragraph("• Optimizing transaction workflows and integrating third-party systems.", normal_style))
    story.append(Spacer(1, 0.2 * inch))

    # Upay
    story.append(Paragraph("<b>Upay</b> - Software Engineer", normal_style))
    story.append(Paragraph("<i>May 2024 - March 2025</i>", normal_style))
    story.append(Paragraph("• Developed mobile financial services and payment solutions.", normal_style))
    story.append(Paragraph("• Implemented REST APIs using Django REST Framework.", normal_style))
    story.append(Spacer(1, 0.3 * inch))

    # Skills
    story.append(Paragraph("TECHNICAL SKILLS", heading_style))
    skills_text = "Python • Golang • Django REST Framework • PostgreSQL • Redis • Docker • Kubernetes • Microservices • MFS • Payment Systems • Fund Transfer • Customer Auth & Management"
    story.append(Paragraph(skills_text, normal_style))
    story.append(Spacer(1, 0.3 * inch))

    # Education
    story.append(Paragraph("EDUCATION", heading_style))
    story.append(Paragraph("<b>Daffodil International University</b>", normal_style))
    story.append(Paragraph("Bachelor of Science in Computer Science & Engineering", normal_style))
    story.append(Paragraph("<i>January 2018 - February 2022</i>", normal_style))
    story.append(Paragraph("Department: CSE", normal_style))
    story.append(Spacer(1, 0.2 * inch))

    # Recent Projects (optional)
    story.append(Paragraph("RECENT PROJECTS", heading_style))
    story.append(Paragraph("Ucbbone, Super App, Upay services - contributed to backend services, system integration, and optimized financial workflows.", normal_style))

    # Build PDF
    doc.build(story)
    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Robel_Hossain_CV.pdf"'
    return response
def find_me(request):
    return render(request, "find_me.html")

def services(request):
    return render(request, "services.html")