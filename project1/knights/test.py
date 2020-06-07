from logic_fds import *
# import termcolor

# termcolor.cprint(f"{symbol}: YES", "green")


testing = 'harry'

def main():
    if testing == 'rain':
        rain = Symbol("rain")
        out = Symbol("out")
        # in = Not(out)

        knowledge = And(
            Implication(Not(rain), out),
            Not(out)
        )

        def really_check(query):
            string_query = str(query)
            result = str(model_check(knowledge, query))
            print("The statement " + string_query + " turns out to be " + result + ".")
        really_check(rain)
    elif testing == 'harry':
        rain = Symbol("rain")
        hagrid = Symbol("hagrid")
        dumbledore = Symbol("dumbledore")

        knowledge = And(
            Implication(Not(rain), hagrid),
            Or(hagrid, dumbledore),
            Not(And(hagrid, dumbledore)),
            dumbledore
        )

        print(model_check(knowledge, rain))
    elif testing == 'mastermind':
        colors = ["red", "blue", "green", "yellow"]
        symbols = []
        for i in range(4):
            for color in colors:
                symbols.append(Symbol(f"{color}{i}"))

        knowledge = And()

        # Each color has a position.
        for color in colors:
            knowledge.add(Or(
                Symbol(f"{color}0"),
                Symbol(f"{color}1"),
                Symbol(f"{color}2"),
                Symbol(f"{color}3")
            ))

        # Only one position per color.
        for color in colors:
            for i in range(4):
                for j in range(4):
                    if i != j:
                        knowledge.add(Implication(
                            Symbol(f"{color}{i}"), Not(Symbol(f"{color}{j}"))
                        ))

        # Only one color per position.
        for i in range(4):
            for c1 in colors:
                for c2 in colors:
                    if c1 != c2:
                        knowledge.add(Implication(
                            Symbol(f"{c1}{i}"), Not(Symbol(f"{c2}{i}"))
                        ))

        knowledge.add(Or(
            And(Symbol("red0"), Symbol("blue1"), Not(Symbol("green2")), Not(Symbol("yellow3"))),
            And(Symbol("red0"), Symbol("green2"), Not(Symbol("blue1")), Not(Symbol("yellow3"))),
            And(Symbol("red0"), Symbol("yellow3"), Not(Symbol("blue1")), Not(Symbol("green2"))),
            And(Symbol("blue1"), Symbol("green2"), Not(Symbol("red0")), Not(Symbol("yellow3"))),
            And(Symbol("blue1"), Symbol("yellow3"), Not(Symbol("red0")), Not(Symbol("green2"))),
            And(Symbol("green2"), Symbol("yellow3"), Not(Symbol("red0")), Not(Symbol("blue1")))
        ))

        knowledge.add(And(
            Not(Symbol("blue0")),
            Not(Symbol("red1")),
            Not(Symbol("green2")),
            Not(Symbol("yellow3"))
        ))

        for symbol in symbols:
            if model_check(knowledge, symbol):
                print(symbol)


if __name__ == "__main__":
    main()