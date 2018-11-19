# gym_speak

The gym_speak is a nlp/chatbot/ai that allows a human to give instructions to an AI as well as the correct answer.
The agent then runs and checks to see the difference between outputs

## Speak

The task initializes a bot, we reward the based on the loss function which is applied.
In order to get a better score, the agent needs to respond similar to the correct response.

## SpeakWordClose

The objective of the SpeakWordClose task, allows the bot to gain points if any word in the sentence is correct.
These frequent rewards make the task much more accessible.

## SpeakSentClose

The objective of the SpeakSentClose task is the sum of the loss per word. The agent is rewarded for each word, but wrong words are negative.
The agent uses a hand-coded policy, the difficulty in this task is getting a correct sentence, not just a correct word.

# Installation

```bash
cd gym_speak
pip install -e .
```
