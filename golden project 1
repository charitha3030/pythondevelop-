import time

def calculate_typing_speed(text, time_taken):
    words = text.split()
    num_words = len(words)
    typing_speed = num_words / time_taken
    return typing_speed

def run_typing_test():
    text = "Many of life’s failures are people who did not realize how close they were to success when they gave up."
    print("Type the following text:")
    print(text)
    input("Press Enter when you are ready.")
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    time_taken = end_time - start_time
    typing_speed = calculate_typing_speed(text, time_taken)
    print("Time taken:", round(time_taken, 2), "seconds")
    print("Your typing speed:", round(typing_speed, 2), "words per second")

run_typing_test()
