# Instalování Pythonu 3.5

Operační systém ev3dev je založený na Debian 9, tudíž se nedá divit že pracujeme na archaické Python verzi. Je možné pracovat s nejnovější Python verzí při vývoji ale je to taky bolest v zadeli.

## Pyenv-win

Pokud ještě nemáte nainstalovaný Python tak není co řešit. Pokud jo, tak se hodí tenhle pretty cool software jménem [pyenv-win](https://github.com/pyenv-win/pyenv-win). Ten umožňuje spravovat několik Python verzí na jednom počítači.


### Instalace
- download le pyenv-win: https://github.com/pyenv-win/pyenv-win/archive/master.zip
- make folder named `.pyenv` in user folder (C:\Users\\<uživatelský jméno>)
- extract zip to `.pyenv` folder
- add environment variables so it doesn't fucking break
```powershell
[System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('PYENV_ROOT',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
```

- add pyenv to your path so it isn't a pain to run
```powershell
[System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('path', "User"),"User")
```
- BAM, you're done ᕕ(ᐛ)ᕗ


### Instalace Pythonu

Otevřete terminál a nainstalujte Python 3.5, verzi na ev3dev.

```
pyenv install 3.5
```

A hotovo.

Popřípadě si můžete ještě nainstalovat verzi na celej počítač

```bash
pyenv install 3.13.0 # Nejnovější verze při psaní tohodle
```

a nastavte ji jako globální

```
pyenv global 3.13.0
```

