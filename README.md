# Project ρίζα (Riza)

> An intelligence unit for human-machine conversation handling.

---

## Synopsis

TBD

## Conversation Model

The conversation is designed based on a probabilistic 
state machine, consisting `States` and `Actions`.

- `States` are user's inputs.
- `Actions` are bot's response to the user's input.

```
  user input0
      \_______action#1====> user input1
      /\ 
     /  \______action#2====> user input2
    /                           /     | \____
  action#3            _________/      |      \
  /                action#5        action#4   action#1
user input3<=======/                  |
                                 user input4

```

Each of the action taken on a users' input is coupled 
with some confidence value. The more confidence value, 
the more likelihood the bot would take such action 
in response to the particular user's input.

Even more complicated, we can't expect the user's next 
input to always remain the same once the bot takes an action 
in response to the user's previous input. That is, 
the use's inputs are most of the time multiple.

---

## Prerequisites

> The project runs on Python 3.4.

We use  the following NLP toolkits / libraries:

- [x] [Thailang4r](https://github.com/veer66/thailang4r)
- [x] [Jitar](https://github.com/danieldk/jitar)

For scientific operations / machine learning:

- [x] [Sci-kit Learn, preferrable 0.17.1+](http://scikit-learn.org/)


> **NOTE:** Make sure you've added Jitar' JAR directory 
to your Java CLASSPATH correctly. Otherwise, the text part of speech 
tagging won't function.

---

## Run the ρίζα

TBD

---

## Licence

The project is licenced under [GNU Public Licence 3.0](http://www.gnu.org/licenses/gpl-3.0.en.html).