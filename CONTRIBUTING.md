# Contributing
This is the main Enterprise Event Bus documentation repository. All of our product facing documentation is hosted here.

## Product documentation
The product documentation made available lives in the `/docs` directory of this repo. Documentation source files are written in Markdown and then rendered in HTML using [MkDocs](https://github.com/mkdocs/mkdocs) and [MkDocs Material](https://squidfunk.github.io/mkdocs-material/), based on settings in `mkdocs.yml`. 

Rendered documentation is viewable at https://department-of-veterans-affairs.github.io/ves-event-bus-developer-portal/.


## Local Development
In order to quickly iterate while working on documentation, install the following:

`pip install mkdocs mkdocs-material mkdocs-techdocs-core`

Changes to documentation can be viewed by running `mkdocs serve` in your terminal, from the root of this repository. 