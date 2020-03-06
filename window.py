# window.py
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

from gi.repository import Gtk


class BayesianDeconvWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'BayesianDeconvWindow'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        builder = Gtk.Builder()
        builder.add_from_file(
            "window.ui")
        self.window = builder.get_object("BayesianWindow")
        self.window.show_all()

        self.conv_n_gauss = builder.get_object("convolved_n_gaussians")
        self.autof_n_gaussians = builder.get_object("autof_n_gaussians")

        self.start_button = builder.get_object("start_button")
        self.start_button.connect('clicked', self.show_result)


    def show_result(self, _value):
        result = self.conv_n_gauss.get_value() * self.autof_n_gaussians.get_value()

        dialog = Gtk.MessageDialog(self,
                    Gtk.DialogFlags.MODAL | Gtk.DialogFlags.DESTROY_WITH_PARENT,
                    Gtk.MessageType.INFO,
                    Gtk.ButtonsType.CLOSE,
                    result)
        dialog.run()
        dialog.destroy()

