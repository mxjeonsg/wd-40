import os
import sys
import json

import ownutils

class Multilang: 
    file: str
    json: any

    def __init__(self: object, filename: str) -> any:
        ownutils.typeCheck(filename, str, None)

        self.file = open(filename, "r")

        self.json = json.load(self.file)

    def getAvailableLangs(self: object) -> list[str]:
        return self.json.keys()

    def getStringInLang(self: object, string_id: str, lang_id: str) -> str:
        return self.json[lang_id][string_id]

    def langHasString(self: object, lang_id: str, string_id: str) -> bool:
        if self.json[lang_id][string_id] == "":
            return False
        else:
            return True
    
    def getGenericYes(self: object, lang_id: str) -> str:
        return self.json[lang_id]["BOT_GENERIC_YES"]
    
    def getGenericNo(self: object, lang_id: str) -> str:
        return self.json[lang_id]["BOT_GENERIC_NO"]