from typing import Dict, Text, Any, List, Union, Optional 

from rasa_sdk import Tracker 
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk import Action
from rasa_sdk.forms import FormAction


import json , re


class RDV(FormAction):
 def name(self):
  return "RDV"

 def required_slots(self,tracker) -> List[Text]:
  return ["Nom_Prenom","objet","phno"]
 def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
    return {
            "Nom_Prenom": 
             [self.from_entity(entity="firstname"), self.from_text()],
            "objet": [
                self.from_text(),
            ]
            ,
            "phno": [
                self.from_text(),
            ],
        }
 def validate_phno(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> Dict[Text,Any]:
            if len(value)==8:
                try:
                    float(value)
                    return {"phno":value}
                except ValueError:
                    dispatcher.utter_message("Veuillez entre un numero valide (exp: 21012345) ")
                    return {"phno":None}
            else:
                dispatcher.utter_message("Veuillez entre un numero valide (exp: 21012345) ")
                return {"phno":None}
 

 def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:
        dispatcher.utter_message("❤️❤️❤️ Merci pour votre confiance ")    
        return []

 

"""
class action_Temoignages(Action):
 def name(self):
  "name of the custom action"
  return "action_Temoignages"  
 def run(self,dispatcher,tracker,domain):
  gt = {
            
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": "Marine Drive",
                            "image_url":"https://www.trawell.in/admin/images/upload/486072642MarineDrive_Main.jpg",
                            "subtitle": "Marine Drive is a buzzing waterfront district known for the Marine Walkway, popular for evening strolls,..",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/marine_drive",
                                    "title": "Read More"
                                },
                              {
                                    "type": "web_url",
                                    "url": "https://www.google.com/maps/d/viewer?ie=UTF8&source=embed&oe=UTF8&msa=0&mid=1TQ2nVI6cF8LtWZxKIdXSkIJs5JI&ll=49.21193400000003%2C-123.10863&z=17",
                                    "title": "Location"
                                },  
                            ]
                        },
                        {
                            "title": "Mattancherry",
                            "image_url":"https://th.thgim.com/migration_catalog/article11297834.ece/alternates/FREE_660/MATTANCHERRY_PALACE",
                            "subtitle": "Historic Mattancherry is known for 16th-century Mattancherry Palace, built by the Portuguese in traditional Keralan style",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/mattancherry",
                                    "title": "Read More"
                                },
                                {
                                    "type": "web_url",
                                    "url": "https://www.google.com/maps/place/Mattancherry,+Kochi,+Kerala/@9.9601158,76.2455098,15z/data=!3m1!4b1!4m5!3m4!1s0x3b086d4f2efb0045:0xbfbce1be3e2c1399!8m2!3d9.9578326!4d76.2555324",
                                    "title": "Location"
                                },
                            ]
                        },
                        {
                            "title": "Fort Kochi",
                            "image_url":"https://monicasuricom.files.wordpress.com/2017/02/shutterstock_104171108.jpg",
                            "subtitle": "A charming seaside area, Fort Kochi is known for its Dutch, Portuguese, and British colonial architecture",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/fort_kochi",
                                    "title": "Read More"
                                },
                                {
                                    "type": "web_url",
                                    "url": "https://www.google.com/maps/place/Fort+Kochi,+Kochi,+Kerala/@9.9624501,76.2337644,16z/data=!4m5!3m4!1s0x3b086d314f0b178d:0xc545233f390db43b!8m2!3d9.9657787!4d76.2421147",
                                    "title": "Location"
                                }, 
                            ]
                        },
                        
                    ]
                }
            
        }
  dispatcher.utter_message(attachement=gt)
  return [] """
 


