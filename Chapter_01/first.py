import pyjokes #type: ignore

# 1. Fetch a random programmer joke
joke = pyjokes.get_joke()

# 2. Print the joke to the terminal
print(joke)


print(pyjokes.get_joke())
