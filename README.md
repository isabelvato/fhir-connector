
FHIR-CONNECTOR 
=================================================

[![Latest release](https://img.shields.io/github/v/release/mhucka/readmine.svg&color=b44e88)](https://github.com/mhucka/readmine/releases)
[![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)]
[![Build Status](https://travis-ci.org/anfederico/clairvoyant.svg?branch=master)](https://travis-ci.org/anfederico/clairvoyant)
[![Tests](https://img.shields.io/jenkins/tests?compact_message)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Table of contents
-----------------

- [FHIR-CONNECTOR](#fhir-connector)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Installation](#installation)
  - [Requirements](#requirements)
  - [Usage](#usage)
    - [Basic operation](#basic-operation)
    - [Additional options](#additional-options)
  - [Known issues and limitations](#known-issues-and-limitations)
  - [Getting help](#getting-help)
  - [Contributing](#contributing)
  - [License](#license)
  - [Authors and history](#authors-and-history)


Introduction
------------
This reporistory includes a first approach to a tool capable of transforming information from different sources into FHIR format. However, for the first version, the connector recreates how it works by means of an example of an Observation. 

The following sections in the README document help to install and deploy the connector and understand how the transformation tool has been developed. 

Installation
------------

## Requirements

First of all, because the connector has been developed in Python, we will need a framework to deploy the application.  

In thi case, it have been used Fl

Begin this section by mentioning any prerequisites that may be important for users to have before they can use your software.  Examples include hardware and operating system requirements.

Next, provide step-by-step instructions for installing the software, preferably with command examples that can be copy-pasted by readers into their software environments. For example:

```bash
a command-line command here
```

Sometimes, subsections may be needed for different operating systems or particularly complicated installations.
 

Usage
-----

This section explains the principles behind this README file.  If this repository were for actual _software_, this [Usage](#usage) section would explain more about how to run the software, what kind of output or behavior to expect, and so on.

### Basic operation

A suggested approach for using this example README file is as follows:

1. Copy the [source file](README.md) for this file to your repository and commit it to your version control system
2. Delete all the body text but keep the section headings
3. Write your README content
4. Commit the new text to your version control system
5. Update your README file as your software evolves

The first paragraph in the README file (under the title at the very top) should summarize your software in a concise fashion, preferably using no more than one or two sentences.

<p align="center"><img width="80%" src=".graphics/screenshot-top-paragraph.png"></p>

The space under the first paragraph and _before_ the [Table of Contents](#table-of-contents) is a good location for optional [badges](https://github.com/badges/shields), which are small visual tokens commonly used on GitHub repositories to communicate project status, dependencies, versions, DOIs, and other information.  The particular badges and colors you use depend on your project and personal tastes.

The [Introduction](#introduction) and [Usage](#usage) sections are described above.

In the [Known issues and limitations](#known-issues) section, summarize any notable issues and/or limitations of your software.  The [Getting help](#getting-help) section should inform readers of how they can contact you, or at least, how they can report problems they may encounter.  The [Contributing](#contributing) section is optional; if your repository is for a project that accepts open-source contributions, then this section is where you can explain to readers how they can go about making contributions.

The [License](#license) section should state any copyright asserted on the project materials as well as the terms of use of the software, files and other materials found in the project repository.  Finally, the [Authors and history](#authors-and-history) section should inform readers who the authors are; it is also a place where you can acknowledge other contributions to the work and the use of other people's software or tools.

### Additional options

Some projects need to communicate additional information to users and can benefit from additional sections in the README file.  It's difficult to give specific instructions &ndash; a lot depends on your software, your intended audience, etc.  Use your judgment and ask for feedback from users or colleagues to help figure out what else is worth explaining.


Known issues and limitations
----------------------------

In this section, summarize any notable issues and/or limitations of your software.  If none are known yet, this section can be omitted (and don't forget to remove the corresponding entry in the [Table of Contents](#table-of-contents) too); alternatively, you can leave this section in and write something along the lines of "none are known at this time".


Getting help
------------

Inform readers of how they can contact you, or at least how they can report problems they may encounter.  This may simply be a request to use the issue tracker on your repository, but many projects have associated chat or mailing lists, and this section is a good place to mention those.


Contributing
------------

Mention how people can offer contributions, and point them to your guidelines for contributing.


License
-------

This README file is distributed under the terms of the [Creative Commons 1.0 Universal license (CC0)](https://creativecommons.org/publicdomain/zero/1.0/).  The license applies to this file and other files in the [GitHub repository](http://github.com/mhucka/readmine) hosting this file. This does _not_ mean that you, as a user of this README file in your software project, must also use CC0 license!  You may use any license for your work that you see fit.


Authors and history
---------------------------

In this section, list the authors and contributors to your software project.  (The original author of this file is [Mike Hucka](http://www.cds.caltech.edu/~mhucka/).)  Adding additional notes here about the history of the project can make it more interesting and compelling.
