# CASO Pro 3500 RC Demo
_Demonstration on how to control your [CASO Pro
3500](http://www.caso-germany.com/en/products/induction/mobile-single-hobs/product-view/p/77/) induction cooker remotely_

Demo video:

[![Little Demo](https://github.com/aellwein/aellwein.github.io/blob/master/casopro/preview.png)](https://www.youtube.com/watch?v=2UwJkc3DaE4)

## Hardware Installation
Look at the [wiki](https://github.com/aellwein/caso-pro-control/wiki) for detailed description.


## Software Requirements
* a RaspberryPi (Model B and higher)
* Python 3.4+ (Python 3.6 recommended)
* python-setuptools and python-virtualenv

## Software Installation
* ``mkdir some_dir ; cd some_dir``
* ``virtualenv venv``
* ``source venv/bin/activate``
* ``python3 setup.py install``

## Running
(run as root or with sudo) ``casopro``
For possible options, consult ``casopro --help``.

## Developer Mode
* ``python3 setup.py develop``
* (as root or with sudo) ``casopro --debug --logging=debug``


