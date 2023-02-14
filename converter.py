# created by Vincent Munyalo

from markdown2 import markdown 
from jinja2 import Environment, FileSystemLoader
from json import load

template_env = Environment(loader=FileSystemLoader(searchpath='./'))
template = template_env.get_template('./site/templates/layout.html')


class Converter:
    # initialize converter class
    def __init__(self):
        self.info_files = ['articles', 'aboutus', 'contactus']
        self.output_files = ['articles.html', 'aboutus.html', 'contactus.html']

    # read markdown files from markdown folder
    def read_files(self):
        for i,file in enumerate(self.info_files):
            with open(f'./site/markdown/{file}.md') as markdown_file:
                self.info_files[i] = markdown(
                    markdown_file.read(),
                    extras=['fenced-code-blocks', 'code-friendly'])

    # convert the markdown files into a static site
    def convert_files(self):
        with open('config.json') as config_file:
            config = load(config_file)

        # save the converted files in output files
        for i,file in enumerate(self.output_files):
            with open(f'./site/templates/{file}', 'w') as output_file:
                output_file.write(
                    template.render(
                        title=config['title'],
                        description=config['description'],
                        author=config['author'],
                        code_link=config['code_link'],
                        identifier=config['identifier'],
                        url=config['url'],
                        content=self.info_files[i],
                    )
                )

    # run the necessary functions
    def run(self):
        self.read_files()
        self.convert_files()

if __name__ == "__main__":
    converter = Converter()
    converter.run()

'''
with open('./site/markdown/articles.md') as markdown_file:
    article = markdown(
        markdown_file.read(),
        extras=['fenced-code-blocks', 'code-friendly'])

with open('./site/markdown/aboutus.md') as aboutus_file:
    aboutus = markdown(
        aboutus_file.read(),
        extras=['fenced-code-blocks', 'code-friendly'])

with open('./site/markdown/contactus.md') as contactus_file:
    contactus = markdown(
        contactus_file.read(),
        extras=['fenced-code-blocks', 'code-friendly'])

with open('config.json') as config_file:
    config = load(config_file)

with open('./site/templates/articles.html', 'w') as output_file:
    output_file.write(
        template.render(
            title=config['title'],
            description=config['description'],
            author=config['author'],
            code_link=config['code_link'],
            identifier=config['identifier'],
            url=config['url'],
            content=article,
        )
    )

with open('./site/templates/aboutus.html', 'w') as output_file:
    output_file.write(
        template.render(
            title=config['title'],
            description=config['description'],
            author=config['author'],
            code_link=config['code_link'],
            identifier=config['identifier'],
            url=config['url'],
            content=aboutus
        )
    )

with open('./site/templates/contactus.html', 'w') as output_file:
    output_file.write(
        template.render(
            title=config['title'],
            description=config['description'],
            author=config['author'],
            code_link=config['code_link'],
            identifier=config['identifier'],
            url=config['url'],
            content=contactus
        )
    )'''