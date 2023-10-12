# LACC Scientific Library

## Overview

This python module contains functions that are used for all the calculations required for lab reports as well as other
scientific ventures at Los Angleles City College.

## Publishing

To publish updates to these packages, please register with the [LACC Organizational Account](https://github.com/la-edu) on [GitHub](https://github.com/). Email department chair Dr. Jayesh Bhakta @ [bhaktaj@lacitycollege.edu](mailto:bhaktaj@lacitycollege.edu) for further information.

Most of the code that requires maintainance is grouped by lab folders. Please maintain shared lab modules within the `utils` directory.

## Development

### Requirements

* [Python 3.11.3](https://www.python.org/downloads/release/python-3113/)
* [Virtual Env](https://virtualenv.pypa.io/en/latest/installation.html)

### Quickstart

```
$> cd <ROOT_DIR>
$> virtualenv venv
$> source venv/bin/activate
$> pip install -r requirements.txt
```

#### Tests

```
$> cd <ROOT_DIR>
$> source venv/bin/activate
$> pytest
```