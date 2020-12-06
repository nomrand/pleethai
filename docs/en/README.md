![GaifaaYeepun](https://user-images.githubusercontent.com/42882840/80269234-b4ad1c80-86e8-11ea-8a02-567b854170d5.png)

![deploy gaifaa](https://github.com/jocv-thai/pleethai/workflows/deploy%20gaifaa/badge.svg)

[日本語](../../README.md) | English | [ภาษาไทย](../th/README.md)

# Overview
GaifaaYeepun is a dictionary website project for Japanese, Thai, and English words/sentences, powered by Django.
This project is designed for Thai people who are learning Japanese, and also Japanese people who are learning Thai language.

# Prerequisites
## Server

* Web Server(Windows Server+IIS)(for Production Environment)
* Python(3.6.7 recommended)
* Git

## Client

* PC / Smartphone


# Install
- Production Environment (**To Be Determined**)
- [Development Environment](./install_develop.md)


# Usage (for system users)
On the "Search Page", you can search for words/sentences.

In case a word/sentence you looked up was not registered, you can send a request for the new
words/sentences to the system manager from the "Request Page".


## details of each page

- [Search Page](./howtouse_search.md)  
[<img src ="https://user-images.githubusercontent.com/42882840/100090635-cf21c100-2e96-11eb-98ec-18694d4d44c9.gif" alt="search demo" width="320">](./howtouse_search.md)

- [Request Page](./howtouse_request.md)  
[<img src ="https://user-images.githubusercontent.com/42882840/100090636-d0eb8480-2e96-11eb-823e-e0059da94e58.gif" alt="request demo" width="320">](./howtouse_request.md)


# System Maintenance Procedure
- How to update system
  - Get the newest files from this repository, and restart the web server.
- [How to add or edit words/sentences](./maintenance_dataedit.md)
- [What to do when you receive a user’s request](./maintenance_reqreceived.md)


# System Configuration
- System Configuration Diagram  
![System Configuration Diagram](https://docs.google.com/drawings/d/e/2PACX-1vSLFh_yZhKKi0L7hnfksXXx2Rjc6bimx0RjocQRpwrI5KxMZSzmARUx9lNiZXjq-8R6oSboAkMqkxgV/pub?w=2024&h=996)

- [Database Structure](./database.md)
