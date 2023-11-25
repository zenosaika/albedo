import os
import pdfkit
from jinja2 import Environment, FileSystemLoader


def html2pdf(template_name, contexts, options):
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = Environment(loader=FileSystemLoader(templates_dir))
    
    try:
        template = env.get_template(f'{template_name}.html')
    except:
        return {'error': 'template not found'}, None
    
    rendered_template = template.render(contexts)

    css_path = os.path.join(root, 'templates', f'{template_name}.css')
    if os.path.exists(css_path):
        pdf = pdfkit.from_string(rendered_template, False, options=options, css=css_path)
    else :
        pdf = pdfkit.from_string(rendered_template, False, options=options)

    return None, pdf