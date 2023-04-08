
# SystemBOT

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![Languages Count](https://img.shields.io/github/languages/count/theSystemFall/SystemBOT)
![Top language](https://img.shields.io/github/languages/top/theSystemFall/SystemBOT)

### What is this ?
*SystemBOT is a personal project created to be a multi purpose discord bot with moderation, economy, and fun features*

## Table of contents
- [SystemBOT](#systembot)
    - [What is this ?](#what-is-this-)
  - [Table of contents](#table-of-contents)
  - [Running](#running)
      - [1. **Some things to know before running**](#1-some-things-to-know-before-running)
      - [2. **Clone this repository to your machine**](#2-clone-this-repository-to-your-machine)
      - [3. **Install dependencies**](#3-install-dependencies)
      - [4. **Create the data directories**](#4-create-the-data-directories)
      - [5. **Run the bot**](#5-run-the-bot)
  - [Privacy Policy and Terms of Service](#privacy-policy-and-terms-of-service)
  - [License](#license)


## Running

*I would prefer you don't run an instance of my bot, just join my server to use it, the code is open-source for educational purposes.*

Nevertheless, the installation steps are as follows:
#### 1. **Some things to know before running**

This project was developed on a Windows environment and using Python 3.11, it's highly recommended that you run it on the same to avoid any bugs.

#### 2. **Clone this repository to your machine**

```bash
$ git clone https://github.com/theSystemFall/SystemBOT
```
#### 3. **Install dependencies**

```bash
$ pip install -r requirements.txt
```

#### 4. **Create the data directories**

Create the following directories inside the project folder for the config and logs files, see [base_config.yaml]() for a basic config structure.
```bash
.
└── data
    ├── config.yaml
    └── logs
```

#### 5. **Run the bot**
```bash
$ python launcher.py
```

## Privacy Policy and Terms of Service

Discord requires me to make one of these.

There isn't really anything to note. No personal data is stored.

## License

MIT License

Copyright (c) 2022 Matheus Henrique Lougen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
