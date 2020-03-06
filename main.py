# main.py
#
# Copyright 2020 Gabriel Torregrosa, Manuel Genovés
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio

from window import BayesianDeconvWindow


class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='val.torregrosa.BayesianDeconvolution',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        self.win = self.props.active_window
        if not self.win:
            self.win = BayesianDeconvWindow(application=self).window
        self.win.present()

    def do_startup(self, *args, **kwargs):

        Gtk.Application.do_startup(self)

        action = Gio.SimpleAction.new("run", None)
        action.connect("activate", self._on_run)
        self.add_action(action)

    def _on_run(self, _action, _value):
        self.win.show_result()


if __name__ == '__main__':
    app = Application()
    app.run(sys.argv)