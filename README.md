# Insights Core Experiment #

## About ##

This is just a tiny experimental project to use the [insights-core] as standalone library without [Red Hat Insights]. Built using [a tutorial][tutorial] offered in the [insights-core] repository.

## Requirements ##

* [RHEL], possibly [Fedora]
* [Python 3], maybe it would work with Python 2 as well
* [PIP]

## Usage ##

1. Clone this repository: `git clone git@github.com:Glutexo/insights-core-experiment.git`
2. Go into the repository folder: `cd insights-core-experiment`
2. Create a [virtual enviroment]: `python3 -m venv venv`
3. Enter the [virtual environment]: `. venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the script `python run.py bash_affected`.

Run the script without arguments (`python run.py`) to see available rules.

[insights-core]: https://github.com/RedHatInsights/insights-core
[Red Hat Insights]: https://access.redhat.com/insights/info/
[tutorial]: https://github.com/RedHatInsights/insights-core/blob/master/docs/notebooks/Diagnostic%20Walkthrough.ipynb
[RHEL]: https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux
[Fedora]: https://getfedora.org/
[Python 3]: https://www.python.org/
[PIP]: https://pip.pypa.io/en/stable/
[virtual environment]: https://docs.python.org/3/library/venv.html
