# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.22.4",
# ]
# ///

import marimo

__generated_with = "0.23.0"
app = marimo.App()


@app.cell
def _():
    def __gen(str):
        for x in str.split(' '):
            yield x
    string = "Tausend mal berührt"
    # g = __gen(string)
    # h = (x for x in string.split(' '))
    exerpt = "# Assignment 2: Mining Itemsets (Part III) ## Apriori Algorithm under the Hood In part III of the assignment, we are going to continue our exploration in mining frequent itemsets. Specifically, we are going to examine a few key steps in the Apriori algorithm. First, let's import the packages and dependencies that will be used in this part of the assignment."
    thing = __gen(exerpt)
    next(thing)
    return exerpt, string, thing


@app.cell
def _(thing):
    next(thing)
    return


@app.cell
def _(exerpt, string):
    h = (x for x in string.split(' '))
    jen = h(exerpt)
    next(jen)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
