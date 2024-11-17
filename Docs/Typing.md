# Typování

Typování umožňuje IDEčkám/editorům jednodušeji rozpoznat typy variables/funkcí a umožňuje autocompletion/Intellisense.

Type hinting v Python 3.5 je ale taková trochu mixed bag. Před Python 3.12 se věci dělali všelijak a nebylo to tak unified jako v nejnovějších verzí.

## Funkce

Typování funkcí a argumentů se může dělat takto:

```py
def myFunction(name: str) -> int: # Typ argumentu name jsme definovali jako string
    print("Hello " + name + "!")

    # Zároveň jsme pomocí "-> int" definovali return type jako integer
    return 0

myFunction("John") # Výstup: Hello John!
```

## Variables

Variables se typujou komentářem s typem 

```py
name = "John" # type: str

print(name.split("h")) # Výstup: ['Jo', 'n']
```
