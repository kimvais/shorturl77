# -*- coding: utf-8 -*-
#
# Copyright © 2016 Kimmo Parviainen-Jalanko <k@77.fi>
#

from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
    return "Foobar!"


if __name__ == '__main__':
    app.run()
