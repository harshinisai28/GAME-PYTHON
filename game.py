
import random

from pyscript import document
from pyodide.ffi import create_proxy


# Generate the secret number
target = random.randint(1, 100)
attempts = 0
finished = False


def check_guess(event):
    global attempts, finished

    message = document.querySelector("#message")
    guess_input = document.querySelector("#guess")
    attempts_display = document.querySelector("#attempts")

    if finished:
        message.innerText = "Game over! Click Play Again to restart."
        return

    user_input = guess_input.value.strip()

    if not user_input:
        message.innerText = "Please enter a number!"
        return

    try:
        userChoice = int(user_input)
    except ValueError:
        message.innerText = "Please enter a valid whole number!"
        return

    if userChoice < 1 or userChoice > 100:
        message.innerText = "Enter a number between 1 and 100!"
        return

    # Count valid guesses
    attempts += 1
    attempts_display.innerText = str(attempts)

    # Original number-guessing logic
    if userChoice == target:
        message.innerText = (
            f"Success! Correct Guess! "
            f"You found {target} in {attempts} attempts."
        )
        finished = True

    elif userChoice < target:
        message.innerText = (
            "Your number was too small. Take a bigger guess."
        )

    else:
        message.innerText = (
            "Your number was too big. Take a smaller guess."
        )

    guess_input.value = ""

    if not finished:
        guess_input.focus()


def new_game(event):
    global target, attempts, finished

    target = random.randint(1, 100)
    attempts = 0
    finished = False

    document.querySelector("#guess").value = ""
    document.querySelector("#attempts").innerText = "0"
    document.querySelector("#message").innerText = (
        "New game started! Guess a number between 1 and 100."
    )

    document.querySelector("#guess").focus()


# Connect the HTML buttons to Python
check_proxy = create_proxy(check_guess)
restart_proxy = create_proxy(new_game)

document.querySelector("#check").addEventListener(
    "click", check_proxy
)

document.querySelector("#restart").addEventListener(
    "click", restart_proxy
)
