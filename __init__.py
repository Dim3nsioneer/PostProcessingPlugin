# Copyright (c) 2015 Jaime van Kessel, Ultimaker B.V.
# The PostProcessingPlugin is released under the terms of the AGPLv3 or higher.

from . import PostProcessingPlugin
from UM.i18n import i18nCatalog
i18n_catalog = i18nCatalog("PostProcessingPlugin")
def getMetaData():
    return {
        "type": "extension",
        "plugin": 
        {
            "name": "Post Processing",
            "author": "Ultimaker",
            "version": "15.06",
            "description": i18n_catalog.i18nc("Description of plugin","Extension that allows for user created scripts for post processing")
        }
    }
        
def register(app):
    return { "extension": PostProcessingPlugin.PostProcessingPlugin()}