# Enterprise Event Bus Developer Portal

This is the public-facing developer portal for all things Enterprise Event Bus. The Event Bus is in production and fairly stable, but the content in this repository will be updated regularly to keep information current. 

## Contributing

See something you think can be improved? We welcome collaboration on the Event Bus Portal. Feel free to file an issue, or follow the local development steps below and then submit a pull request. 

## Product documentation

The product documentation made available lives in the `/docs` directory of this repo. Documentation source files are written in Markdown and then rendered in HTML using [MkDocs](https://github.com/mkdocs/mkdocs) and [MkDocs Material](https://squidfunk.github.io/mkdocs-material/), based on settings in `mkdocs.yml`. 

Rendered documentation is viewable at https://department-of-veterans-affairs.github.io/ves-event-bus-developer-portal/.

## Search

Default search functionality provided by MkDocs has been turned off in this project to mitigate a few accessibility issues. These issues need to be fixed in Material for MkDocs or MkDocs source code, so we decided to disable this functionality for now. Search was disabled by adding `plugins: []` to [the mkdocs.yaml file](./mkdocs.yml). To turn search functionality back on, simply remove that line.

## Local Development

This project requires Python 3.x. For Mac users, Python can be installed using homebrew with:

`brew install python3`

In order to quickly iterate while working on documentation, install the following:

`pip3 install mkdocs mkdocs-material mkdocs-techdocs-core`

`mkdocs` may need to be added to `PATH`.

Changes to documentation can be viewed by running `mkdocs serve` in your terminal, from the root of this repository. The portal will be served at `http://127.0.0.1:8000/`

## Support

Need help with something? Feel free to [file an issue](https://github.com/department-of-veterans-affairs/ves-event-bus-developer-portal/issues). 
