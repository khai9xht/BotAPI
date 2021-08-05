# **RASA STRUCTURE**

## **DATA**
### nlu.yml
### rules.yml
### stories.yml


## **ACTIONS**

## **MODELS**

## **TESTs**
### test_stories.yml

## **OTHER FILES**

### config.yml

### credentials.yml

### domain
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
### endpoints.yml
