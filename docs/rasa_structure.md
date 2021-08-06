# **RASA BOT STRUCTURE**

## **1. DATA**
### 1.1 nlu.yml
Contain  example user utterances categorized by intent.
format:
```
{
  "text": "Book a flight from Berlin to SF",
  "intent": "book_flight",
  "entities": [
    {
      "start": 19,
      "end": 25,
      "value": "Berlin",
      "entity": "city",
      "role": "departure",
      "extractor": "DIETClassifier",
    },
    {
      "start": 29,
      "end": 31,
      "value": "San Francisco",
      "entity": "city",
      "role": "destination",
      "extractor": "DIETClassifier",
    }
  ]
}
```
```
{
  "text": "I want to fly from [Berlin]{"entity": "city"} to [San Francisco]{"entity": "city"} .",
  "intent": "book_flight",
  
}
```

### 1.2 rules.yml
Handle small specific conversation patterns
```
  rules:

  - rule: Only say `hello` if the user provided a name
    condition:
    - slot_was_set:
      - user_provided_name: true
    steps:
    - intent: greet
    - action: utter_greet
```
### 1.3 stories.yml
Representation of conversations between a user and an AI assistant
```
stories:
- story: collect restaurant booking info  # name of the story - just for debugging
  steps:
  - intent: greet                         # user message with no entities
  - action: utter_ask_howcanhelp
  - intent: inform                        # user message with entities
    entities:
    - location: "rome"
    - price: "cheap"
  - action: utter_on_it                  # action that the bot should execute
  - action: utter_ask_cuisine
  - intent: inform
    entities:
    - cuisine: "spanish"
  - action: utter_ask_num_people
```

## **2. ACTIONS**
- Response: normal response the assistant will send back to user with format text, image or buttons...
- Custom action: use when you want to make an API call or query a database.
- Forms: use when you expect the assistant to ask for a specific set of information
All action are defined in domain.yml<br>
Using variables (slots, entity) in response (write in domain.yml):
```
responses:
  utter_greet:
  - text: "Hey, {name}. How are you?"
```
Response with button format:<br>
```
responses:
  utter_greet:
  - text: "Hey! How are you?"
    buttons:
    - title: "great"
      payload: "/mood_great"
    - title: "super sad"
      payload: "/mood_sad"
```

Response with image format:<br>
```
  utter_cheer_up:
  - text: "Here is something to cheer you up:"
    image: "https://i.imgur.com/nGF1K8f.jpg"
```

Calling Responses from Custom Actions<br>
```
from rasa_sdk.interfaces import Action

class ActionGreet(Action):
    def name(self):
        return 'action_greet'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_greet")
        return []
```

Form (write in domain.yml): 
```
forms:
  restaurant_form:
    required_slots:
        cuisine:
          - type: from_entity
            entity: cuisine
        num_people:
          - type: from_entity
            entity: number
```
Activate form:
```
rules:
- rule: Activate form
  steps:
  - intent: request_restaurant
  - action: restaurant_form
  - active_loop: restaurant_form
```
Deactivate form:
```
rules:
- rule: Submit form
  condition:
  # Condition that form is active.
  - active_loop: restaurant_form
  steps:
  # Form is deactivated
  - action: restaurant_form
  - active_loop: null
  - slot_was_set:
    - requested_slot: null
  # The actions we want to run when the form is submitted.
  - action: utter_submit
  - action: utter_slots_values
```
## **3. MODELS**
save trained models or loaded model from other stories
## **4. TESTS**
### 4.1 test_stories.yml
use the same format as stories.yml in data for training
```
stories:
- story: greet and ask language
- steps:
  - user: |
      hey
    intent: greet
  - action: utter_greet
  - user: |
      what language do you speak
    intent: faq/language
  - action: utter_faq
```
## **5. OTHER FILES**

### 5.1. Model Configuration (config.yml)
Defines the components and policies that your model will use to make predictions based on user input. 
Rasa suggests some configuration for user ro train NLU model.
Format:
```
	language: en
	pipeline:		# Select suggested config feature here
	policies:
	  - name: MemoizationPolicy
		max_history: 5
		epoch: 5
```
### 5.2 credentials.yml
Add channels, callback, websocket for your bot

### 5.3 domain
Define all which your assistant operates, include:
- intents, entities, slots, responses, forms, and actions.
- configuration for conversation sessions
Can define in single file (domain.yml) or many file (in a folder).

Define intents: <br>
```
	intents:
		use_entities:
		- name
		- first name
		ignore_entities:	#these don't impact the next action predictions
		- localtion
		- age
```

Define entities: <br>
```
	entities:
	- name
	- date
	- address

```

Define slots <br>
```
	slots:
		slot_name:
			type: text/bool/categorical/float/list/any
			influence_conversation: True	#true if you want to incluence the next prediction
```
you can custom type of slot by extending ```rasa.shared.core.slots import Slot``` and save it as a module
### 5.4 endpoints.yml
Usage:
- Tracker stores: store assistant's conversations history.
- Add event brokers.
- pull/load model from Disk/Server/Cloud
- lock stores to process messages of conversation in the right order