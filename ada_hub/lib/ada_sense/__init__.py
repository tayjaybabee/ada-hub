from subprocess import Popen, PIPE


class AdaSense(object):

    @staticmethod
    def check_gui():




    def load_emulator(self):
        """

        Load the emulated version of the SenseHat library. This will only work if there is a GUI windowing system
        installed on the OS.

        Returns:
            An instance of sense_emu.SenseHat

        """
        from sense_emu import SenseHat

        return SenseHat()


    def load_sense(self, emulate=False):
        if not emulate:
            from sense_hat import SenseHat



    def add_default_settings(self, config):
        conf_section = 'ADA_SENSE_SETTINGS'

        # Add the section
        config.add_section(conf_section)
        config.set(conf_section, 'always_emulate', 'False')



        config.set(conf_section, 'never_emulate', 'False')
        config.set

    def get_humidity(self):
        pass

    def get_temp(self):
        pass

    def convert_temp_to_f(self):
        pass

    def __init__(self, config, emulate=False, temp_units=None):

        if 'ADA_SENSE_SETTINGS' not in config.sections():
            self.config = self. add_default_settings()
