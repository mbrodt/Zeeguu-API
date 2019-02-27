# -*- coding: utf8 -*-
from zeeguu_core.configuration.configuration import load_configuration_or_abort
from flask_cors import CORS
from flask import Flask
import flask

# *** Creating and starting the App *** #
app = Flask("Zeeguu-API")
CORS(app)

load_configuration_or_abort(app,
                            'ZEEGUU_API_CONFIG',
                            [  # first three are required by core
                                'MAX_SESSION',
                                'SQLALCHEMY_DATABASE_URI',
                                'SQLALCHEMY_TRACK_MODIFICATIONS',

                                # next three are required by API when
                                # run locally
                                'DEBUG',
                                'HOST',
                                'SECRET_KEY',

                                # the following are required by the API
                                # for user account creation & password recovery
                                'INVITATION_CODES',
                                'SMTP_SERVER',
                                'SMTP_USERNAME',
                                'SMTP_PASSWORD',
                            ])

# The zeeguu_core.model  module relies on an app being injected from outside
# ----------------------------------------------------------------------
import zeeguu_core

zeeguu_core.app = app
import zeeguu_core.model

assert zeeguu_core.model
# -----------------

from .api import api

app.register_blueprint(api)

try:
    import flask_monitoringdashboard as dashboard

    dashboard.config.init_from(envvar='FLASK_MONITORING_DASHBOARD_CONFIG')

    from zeeguu_core.model import Session

    dashboard.config.get_group_by = lambda: Session.find(request=flask.request).user_id
    dashboard.bind(app=app)
    print("Started the Flask Monitoring Dashboard")
except Exception as e:
    print("Could not install the flask_monitornig_dashboard")
    print(e)
    import traceback
    print(traceback.format_exc())

try:
    from zeeguu_api.machine_specific import machine_specific_config

    machine_specific_config(app)
except ModuleNotFoundError as e:
    print("no machine specific code found")
