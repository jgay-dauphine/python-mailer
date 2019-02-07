from jinja2 import Environment, FileSystemLoader
from email.mime.text import MIMEText

class Builder:
    def __init__(self):
        return
    
    def build_template(self, symbols, summary, articles, company_name, exchange):
        try:
            # Declare jinja2 template
            file_loader = FileSystemLoader('templates')
            env = Environment(loader=file_loader)
            template = env.get_template('email.html')
            # Build template from email.html file
            output = template.render(symbols=symbols, summary=summary, articles=articles, companyName=company_name, exchange=exchange)
            body = MIMEText(output, 'html')
            return body
        except Exception as e:
            # Dispaly error
            print(str(e))

