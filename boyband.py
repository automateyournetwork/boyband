import requests

# -------------------------
# Jinja2
# -------------------------

from jinja2 import Environment, FileSystemLoader
template_dir = 'Mindmaps/Templates/'
env = Environment(loader=FileSystemLoader(template_dir))
bts_template = env.get_template('bts.j2')

# Get Quotes

quotes = requests.request("GET", "https://bts-quotes-api.herokuapp.com/quotes")
quoteJSON = quotes.json()

# -------------------------
# Template
# -------------------------

parsed_all_output = bts_template.render(quotes = quoteJSON)

# -------------------------
# Save File
# -------------------------

with open("Mindmaps/BTS/BTS_Quotes_MindMap.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()