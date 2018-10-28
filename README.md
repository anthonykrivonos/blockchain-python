# Blockchain - Python

Straightforward and concurrent blockchain implementation in Python 3.

## What's inside?

This project consists of a server script (`server.py`), client code (`client.py`), data models for `block`s and and the `blockchain`, as well as both a client thread (`models/clientthread.py`) and a broadcast thread (`models/broadcastthread.py`).

![Blockchain](https://www.investors.com/wp-content/uploads/2018/01/STock-blockchain-01-shutt.jpg)

## Getting Started

### Installing and Running

1. Clone this repository.
2. Open a terminal window and `cd` to the project.
2. Start the server with `python server.py`.
3. Open a new tab in the terminal, and make sure the project is still the root.
3. Start the client with `python client.py`.
4. In the same tab as the client, input commands as follows:

```
-f ### -t ### -a ###
```

where the `###` after each respective command indicates:
- `-f`: fromValue
- `-t`: toValue
- `-a`: transactionAmount

## Contributing

If you'd like to improve and/or expand the content of this library, feel free to submit pull requests. If you experience any issues with this code, please let me know promptly.

## Authors

* **Anthony Krivonos** - *Developer* - [Portfolio](https://anthonykrivonos.com)

* **Jeremy De La Cruz** - *Teammate* - [GitHub](https://github.com/Jeremy523)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* *Coral Health* for providing the [Code your own blockchain in less than 200 lines of Go!](https://medium.com/@mycoralhealth/code-your-own-blockchain-in-less-than-200-lines-of-go-e296282bcffc) tutorial, which this project is a rough translation of, with numerous extras.
* Vicki Shao for all the support and flames! 🔥
