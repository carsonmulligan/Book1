from weasyprint import HTML, CSS

html = HTML(filename='book_markdown_to_html.html')
css = CSS(string='''
    @page { size: A4; margin: 20mm 15mm; }
    body { max-width: 100% !important; }
    .vertical-container { height: auto !important; }
''')

html.write_pdf(
    'vertical-book.pdf',
    stylesheets=[css],
    presentational_hints=True
) 