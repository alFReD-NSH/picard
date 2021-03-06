# -*- coding: utf-8 -*-
#
# Picard, the next-generation MusicBrainz tagger
# Copyright (C) 2008 Philipp Wolfer
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

from PyQt4 import QtCore, QtGui
from picard.config import BoolOption, TextOption, IntOption
from picard.ui.options import OptionsPage, OptionsCheckError, register_options_page
from picard.ui.ui_options_ratings import Ui_RatingsOptionsPage


class RatingsOptionsPage(OptionsPage):

    NAME = "ratings"
    TITLE = N_("Ratings")
    PARENT = "metadata"
    SORT_ORDER = 20
    ACTIVE = True

    options = [
        BoolOption("setting", "enable_ratings", False),
        TextOption("setting", "rating_user_email", "users@musicbrainz.org"),
        BoolOption("setting", "submit_ratings", True),
        IntOption("setting", "rating_steps", 6),
    ]

    def __init__(self, parent=None):
        super(RatingsOptionsPage, self).__init__(parent)
        self.ui = Ui_RatingsOptionsPage()
        self.ui.setupUi(self)

    def load(self):
        self.ui.enable_ratings.setChecked(self.config.setting["enable_ratings"])
        self.ui.rating_user_email.setText(self.config.setting["rating_user_email"])
        self.ui.submit_ratings.setChecked(self.config.setting["submit_ratings"])

    def save(self):
        self.config.setting["enable_ratings"] = self.ui.enable_ratings.isChecked()
        self.config.setting["rating_user_email"] = self.ui.rating_user_email.text()
        self.config.setting["submit_ratings"] = self.ui.submit_ratings.isChecked()


register_options_page(RatingsOptionsPage)
