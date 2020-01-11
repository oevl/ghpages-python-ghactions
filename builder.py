#!/usr/bin/env python3

import yaml
import jinja2

# Import Meetup Data from YAML file
with open('meetup.yaml') as f:
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    #print(data)

# Load the template
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "template.html"
template = templateEnv.get_template(TEMPLATE_FILE)
renderedTemplate= template.render(
	Meetup = data['Meetup'],
	Saludo = data['Saludo'],
	Actividades = data['Actividades'],
	Datos = data['Datos'],
	Expositores = data['Expositores'],
	Patrocinantes = data['Patrocinantes'],
	Testimonios = data ['Testimonios'],
	MeetupURL = data['MeetupURL']
)  # this is where to put args to the template renderer

with open('index.html', 'w') as writer:
	writer.write(renderedTemplate)



