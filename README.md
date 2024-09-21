# Search-Replace-Body-Pos
This is to help fix txt. file captions made with auto captioners that uses a lot of the own subject body position, that can be tricky for inference and training with models like Flux.

## Getting started
* cd into this directory after cloning the repo
* start the app
```
py SR.py
```

It will ask for the input folder (will scan on the subfolders as well) on the cmd/powershell command. Press enter.
It will output a report.

I also adjusted it to add after each substitution a string to help visualize manually each substitution made. You should remove this <!###-----------###> with another SR program like Notepad++ or Taggui.
