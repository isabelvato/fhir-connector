
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
  - [1. Introduction](#1-introduction)
  - [2. Installation](#2-installation)
  - [2.1. Requirements](#21-requirements)
  - [2.2. Deployment](#22-deployment)
  - [Usage](#usage)
    - [Basic operation](#basic-operation)
    - [Additional options](#additional-options)
  - [Known issues and limitations](#known-issues-and-limitations)
  - [Getting help](#getting-help)
  - [Contributing](#contributing)
  - [License](#license)
  - [Authors and history](#authors-and-history)


1. Introduction
------------
This reporistory includes a first approach to a tool capable of transforming information from different sources into FHIR format. However, for the first version, the connector recreates how it works by means of an example of an Observation. 

The following sections in the README document help to install and deploy the connector and understand how the transformation tool has been developed. 

2. Installation
------------

## 2.1. Requirements

First of all, because the connector has been developed in Python, we will need a framework to deploy the application. In this case, it have been used _Flask v2.0.2_ for the simplicity and speed. 

At the same time, the development of the code requires the use of the _requests_ library, which is also included in this file.Thanks to this library, GET and POST methods can be executed.

- requirements.txt
  - Flask
  - requests 

## 2.2. Deployment

The deployment of the app is been explained in the following lines. 

Firstly, is necessary to clone the repository.  

```bash
> git clone _route_
```
After that, the folder with all the documents will be in local. We sholud go to the path where the folder has been saved:

```bash
> cd path/fhir-connector
```
Once this has been done, we could deploy the container to run the application. For that: 

```bash
> docker build -t _name container_ . 
```
Finally, the container has been created and is time run it. 

```bash
> docker run -it -p 5000:5000 _name container_  
```

By executing this command, ...... 

Usage
-----

### Basic operation


### Additional options

Known issues and limitations
----------------------------

Getting help
------------

Contributing
------------

License
-------


Authors and history
---------------------------
