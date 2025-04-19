import re
import random
import long_responses as long
from datetime import datetime

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words)) if recognised_words else 0

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    return int(percentage * 100) if has_required_words or single_response else 0


def check_all_messages(message, full_msg):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        highest_prob_list[bot_response] = message_probability(
            message, list_of_words, single_response, required_words
        )

    # Standard conversational responses
    response('Hey there! How can I help you today?', ['hello', 'hi', 'hey'], single_response=True)
    response('Goodbye! Take care.', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing great! How about you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re most welcome!', ['thank', 'thanks'], single_response=True)

    # Custom FAQs
    response('My name is CodePal, your friendly assistant.', ['your', 'name'], required_words=['name'])
    response('I was created by an awesome developer 😎', ['who', 'made', 'you'], required_words=['who', 'made'])
    response('I can tell jokes, do math, chat with you, and give advice! 😄', ['what', 'can', 'you', 'do'], required_words=['what', 'do'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['eat'])

    # Jokes
    response(long.get_joke(), ['tell', 'joke'], required_words=['joke'])

    # Simulated weather
    response("It looks like a pleasant day! Perfect for a walk. ☀️", ['weather', 'outside'], required_words=['weather'])

    # Time-based greetings
    now = datetime.now().hour
    if 5 <= now < 12:
        response('Good morning! 🌞', ['morning'], single_response=True)
    elif 12 <= now < 18:
        response('Good afternoon! ☀️', ['afternoon'], single_response=True)
    elif 18 <= now < 22:
        response('Good evening! 🌇', ['evening'], single_response=True)

    # Calculator feature (matches basic math expressions)
    if re.search(r'[\d+\-*/(). ]+', full_msg):
        try:
            result = eval(full_msg, {"__builtins__": {}})
            return f"The answer is: {result}"
        except:
            pass

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return long.unknown() if highest_prob_list[best_match] < 20 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    return check_all_messages(split_message, user_input.lower())


# Main loop
if __name__ == '__main__':
    print("ChatBot 🤖: Hi there! I’m CodePal. Ask me anything, or type 'bye' to exit.")
    while True:
        user_input = input('You: ')
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("ChatBot 🤖: It was great chatting! Have a wonderful day! 👋")
            break
        print('ChatBot 🤖:', get_response(user_input))
