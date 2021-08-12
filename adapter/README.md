# Adapter Pattern

Inspired by <https://www.youtube.com/watch?v=2PKQtcJjYvc>

Christofer mentions an example from a 3rdparty nodeJS library that changed order of function arguments in a new major version relase.

We have a Client that uses the old version and dont want to rewrite all the logic there.

We'll write an adapter to the new version and wrap the new version with this adapter.

It is key to the Adapter pattern that it does not add new functionality but only adapt to something you know or have already. You use an Adapter to fix a problem (in your code)

Another example of the Adapter: Python 3 differs from Python 2 in that many buildin functions return iterators instead of lists. Hence you sometimes had to add list(...). I.e the list() acts as an adapter.
