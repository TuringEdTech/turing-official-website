from jinja2 import Environment, FileSystemLoader

loader = FileSystemLoader('templates')

env = Environment(loader = loader)

template = env.get_template('index.html')

result = template.render({
  "Title":"Turing EdTech"
})

with open('index.html', 'w') as index:
  index.write(result)