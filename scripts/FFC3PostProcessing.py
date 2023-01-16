# Copyright (c) 2021 ArteFlux, heavily based on the PostProcessingPlugin from Ruben Dulek
# The FFC3PostProcessing plugin is released under the terms of the "Fuck you flashforge for giving us crippled printer firmware v3 (FYFFFGUCPFv3)" or higher.
# Also thank you for keeping your gcode secret. Good luck selling your printers and frustrate your users with that joke of a slicer called flashprint.
# Why does M6 T0 and M6 T1 (yes, thats really your wait for temperature command, doing it completely different than reprap suggests) only works once in the beginning?
# Dont you think people want to make temperature towers, or change temperatures during the print without jamming their nozzles? Why is M104 S220 (Without T1 or T0)
# always applied to T0? Why do you ignore the currently active tool with such commands? Get your shit together, this is an insult to everyone buying such expensive machines!
# Seriously: Please open up your printer firmware, give us more things to play with. Release an official profile for CURA, Sli3er and other slicers. You can only win.

import re #To perform the search and replace.

from ..Script import Script


class FFC3PostProcessing(Script):
    """Performs a search-and-replace on all g-code.

    Due to technical limitations, the search can't cross the border between
    layers.
    """

    def getSettingDataString(self):
        return """{
            "name": "FFC3 Post Processing Script",
            "key": "FFC3PostProcessing",
            "metadata": {},
            "version": 2,
            "settings": {}
        }"""

    def execute(self, data):
        search_string = "M104 S[0-9]{1,3}\n"
        search_regex = re.compile(search_string)

        replace_string = ""

        for layer_number, layer in enumerate(data):
            data[layer_number] = re.sub(search_regex, replace_string, layer) #Replace all.

        return data