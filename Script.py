# Copyright (c) 2015 Jaime van Kessel, Ultimaker B.V.
# The PostProcessingPlugin is released under the terms of the AGPLv3 or higher.
from UM.Settings.SettingsCategory import SettingsCategory
from UM.Logger import Logger
from UM.Qt.Bindings.SettingsFromCategoryModel import SettingsFromCategoryModel

from UM.i18n import i18nCatalog
i18n_catalog = i18nCatalog("PostProcessingPlugin")

## Base class for scripts. All scripts should inherit the script class. 
class Script():
    def __init__(self):
        super().__init__()
        self._settings = None
        self._settings_model = None
        try:
            setting_data = self.getSettingData()
            if "key" in setting_data:
                self._settings = SettingsCategory(setting_data["key"], i18n_catalog, self)
                self._settings.fillByDict(self.getSettingData())
                self._settings_model = SettingsFromCategoryModel(self._settings)
            else: 
                Logger.log("e", "Script has no key in meta data. Unable to use.")
        except NotImplementedError:
            pass 
    
    ##  Needs to return a dict that can be used to construct a settingcategory file. 
    #   See the example script for an example.
    #   It follows the same style / guides as the Uranium settings.
    def getSettingData(self):
        raise NotImplementedError()
    
    ##  Get the initialised settings 
    def getSettings(self):
        return self._settings
    
    def getSettingsModel(self):
        return self._settings_model
    
    ##  Get setting by key. (convenience function)
    #   \param key Key to select setting by (string)
    #   \return Setting or none if no setting was found.
    def getSettingByKey(self, key):
        return self._settings.getSettingByKey(key)
    
    ##  Set the value of a setting by key.
    #   \param key Key of setting to change.
    #   \param value value to set.
    def setSettingValueByKey(self, key, value):
        setting = self.getSettingByKey(key)
        if setting is not None:
            setting.setValue(value)
    
    ##  Get the value of setting by key.
    #   \param key Key of the setting to get value from
    #   \return value (or none)
    def getSettingValueByKey(self, key):
        setting = self.getSettingByKey(key)
        if setting is not None:
            return setting.getValue()
        return None
    
    ##  This is called when the script is executed. 
    #   It gets a list of g-code strings and needs to return a (modified) list.
    def execute(self, data):
        raise NotImplementedError()