import pcbnew
import complex_plugin_utils

class ComplexPluginAction(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "A complex action plugin"
        self.category = "Examples"
        self.description = "An example of a plugin with several files"

    def Run(self):
        # The entry function of the plugin that is executed on user action
        print("Use another file")
        board = complex_plugin_utils.get_board()
