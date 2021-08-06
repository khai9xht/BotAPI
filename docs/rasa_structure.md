# **RASA STRUCTURE**

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
{
  "text": "I want to fly from [Berlin]{"entity": "city"} to [San Francisco]{"entity": "city"} .",
  "intent": "book_flight",
  
}
```

```
### 1.2 rules.yml
### 1.3 stories.yml


## **2. ACTIONS**

## **3. MODELS**

## **4. TESTS**
### 4.1 test_stories.yml

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