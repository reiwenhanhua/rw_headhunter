# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


AVAILABLE_PRIORITIES = [
    ('0', 'Normal'),
    ('1', 'Good'),
    ('2', 'Very Good'),
    ('3', 'Excellent')
]



