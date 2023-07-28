# Enterprise Event Bus Developer Portal
This is the public facing developer portal for all things Enterprise Event Bus. The Event Bus is in active development and content in this repository is prone to change frequently. 

## Contributing
See something you think can be improved? We welcome collaboration on the Event Bus Portal. Feel free to file an issue, or follow the local development steps below and then submit a pull request. 

## Product documentation
The product documentation made available lives in the `/docs` directory of this repo. Documentation source files are written in Markdown and then rendered in HTML using [MkDocs](https://github.com/mkdocs/mkdocs) and [MkDocs Material](https://squidfunk.github.io/mkdocs-material/), based on settings in `mkdocs.yml`. 

Rendered documentation is viewable at https://department-of-veterans-affairs.github.io/ves-event-bus-developer-portal/.

## Local Development
In order to quickly iterate while working on documentation, install the following:

`pip install mkdocs mkdocs-material mkdocs-techdocs-core`

Changes to documentation can be viewed by running `mkdocs serve` in your terminal, from the root of this repository. 

**Note:** For Mac users, you can install `mkdocs` via homebrew

## Support
Need help with something? Feel free to [file an issue](https://github.com/department-of-veterans-affairs/ves-event-bus-developer-portal/issues). 
