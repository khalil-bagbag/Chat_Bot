## happy path 1 (/tmp/tmpl9s3gtyz/7f7926421c3149698e75ee02020af056_conversation_tests.md)
* greet: hello there!
    - utter_greet
    - action_listen   <!-- predicted: utter_first_message -->
* mood_great: amazing   <!-- predicted: greet: amazing -->
    - utter_happy   <!-- predicted: action_default_ask_affirmation -->
    - action_listen   <!-- predicted: utter_welcome_message -->


## happy path 2 (/tmp/tmpl9s3gtyz/7f7926421c3149698e75ee02020af056_conversation_tests.md)
* greet: hello there!
    - utter_greet
    - action_listen   <!-- predicted: utter_first_message -->
* mood_great: amazing   <!-- predicted: greet: amazing -->
    - utter_happy   <!-- predicted: action_default_ask_affirmation -->
    - action_listen   <!-- predicted: utter_welcome_message -->
* goodbye: bye-bye!   <!-- predicted: bye: bye-bye! -->
    - utter_goodbye   <!-- predicted: action_default_fallback -->


## sad path 1 (/tmp/tmpl9s3gtyz/7f7926421c3149698e75ee02020af056_conversation_tests.md)
* greet: hello
    - utter_greet
    - action_listen   <!-- predicted: utter_first_message -->
* mood_unhappy: not good   <!-- predicted: merci: not good -->
    - utter_cheer_up   <!-- predicted: action_default_ask_affirmation -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes   <!-- predicted: bye: yes -->
    - utter_happy   <!-- predicted: action_default_ask_affirmation -->


## sad path 2 (/tmp/tmpl9s3gtyz/7f7926421c3149698e75ee02020af056_conversation_tests.md)
* greet: hello
    - utter_greet
    - action_listen   <!-- predicted: utter_first_message -->
* mood_unhappy: not good   <!-- predicted: merci: not good -->
    - utter_cheer_up   <!-- predicted: action_default_ask_affirmation -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really   <!-- predicted: greet: not really -->
    - utter_goodbye   <!-- predicted: action_default_ask_affirmation -->
    - action_listen   <!-- predicted: utter_first_message -->


## sad path 3 (/tmp/tmpl9s3gtyz/7f7926421c3149698e75ee02020af056_conversation_tests.md)
* greet: hi
    - utter_greet   <!-- predicted: action_default_ask_affirmation -->
    - action_listen   <!-- predicted: utter_first_message -->
* mood_unhappy: very terrible   <!-- predicted: merci: very terrible -->
    - utter_cheer_up   <!-- predicted: action_default_ask_affirmation -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no   <!-- predicted: merci: no -->
    - utter_goodbye   <!-- predicted: action_default_ask_affirmation -->


## say goodbye (/tmp/tmpl9s3gtyz/7f7926421c3149698e75ee02020af056_conversation_tests.md)
* goodbye: bye-bye!   <!-- predicted: bye: bye-bye! -->
    - utter_goodbye   <!-- predicted: utter_bye -->


## bot challenge (/tmp/tmpl9s3gtyz/7f7926421c3149698e75ee02020af056_conversation_tests.md)
* bot_challenge: are you a bot?   <!-- predicted: merci: are you a bot? -->
    - utter_iamabot   <!-- predicted: action_default_ask_affirmation -->


