
```shell

usage: ada-hub [-h] [-v | -d | -q | -s] [-W | -w] [-D DATA_DIR]
               [-C CONFIG_DIR]
               {credits,cli,gui} ...

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Instruct the logger to output all messages below debug
                        level to the console
  -d, --debug           Instruct the logger to output all messages it has to
                        the console
  -q, --quiet           Instruct the logger to suppress all logger messages
                        below WARNING level from being output to the console
  -s, --silent          Instruct the logger to suppress all logger messages
                        from being output to the console unless they are
                        describing a fatal exception.
  -W, --write-all       Write all files, regardless of location until
                        permission fail
  -w, --write-data-dir  Write all files and directories in the configured data
                        directory structure. By default this directory is
                        /home/taylor/Inspyre-Softworks/AdaHub/
  -D DATA_DIR, --data-dir DATA_DIR
                        Provide the filesystem-location of your application's
                        data directory, or the destination you want the
                        program to create a data-directory in.
  -C CONFIG_DIR, --config-dir CONFIG_DIR
                        Provide the filesystem-location of your application's
                        configuration directory, or the destination you want
                        the program to create a configuration directory in.

Sub-Commands:
  Valid sub-commands for ada-hub

  {credits,cli,gui}
    credits             Print out the credits for all external
                        services/software used to make Ada Hub
    cli                 Run a quick query using the command line (no GUI)
    gui                 Start the program with the full GUI

```

![image](https://user-images.githubusercontent.com/43686206/86574646-c5291100-bf3b-11ea-9611-7bb72f66448d.png)
