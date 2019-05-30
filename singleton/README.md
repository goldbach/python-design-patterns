# Singleton

Ensures a class has only one instance. And provides a global access.
In HFDP, this is implemented by making the constructor a private method.

### onlyone.py 

We'll do it a little bit differnt by wraping our class into another class. When instantiating,
we return the inner class instance (or create it, if called for the first time)

### borg.py

This implementation is the Borg. It is not in HFDP nor the videos.
Key idea is that we want to share state between instances
rather than having one instance only. Instances are not the same, but the share the data.

